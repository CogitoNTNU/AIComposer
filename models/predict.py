import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from dataprocessing.numpy_to_midi import numpy_to_midi
from dataprocessing.generator import generator
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NOTE_IND, NUM_NOTES, \
    MIDI_ARR_SIZE


def sample(preds, note_frequency=1, temperature=1):
    sampled = []
    for pred in preds:
        included = np.where(pred > 0.9)
        not_included = np.where(pred < 0.03)
        pred[included] = 0
        pred[not_included] = 0
        total_pred_sum = round(np.sum(pred) * note_frequency)

        if not total_pred_sum:
            pred[:] = 0
            pred[included] = 1
            sampled.append(pred)
            continue
        pred = np.asarray(pred).astype('float64')
        pred = np.log(pred) / temperature
        exp_preds = np.exp(pred)
        pred = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(total_pred_sum, pred, 1)[0]
        over0 = np.where(probas > 0)
        pred[:] = 0
        pred[over0] = 1
        pred[included] = 1
        sampled.append(pred)
    return np.array(sampled)


def predict(input_array, input_model_filepath, time_steps=1, temperature=1,
            note_frequency=1,
            include_input_in_song=False):
    batch_size = input_array.shape[0]
    model = load_model(input_model_filepath)
    print(model.summary())
    current_input = input_array
    index = 0
    if include_input_in_song:
        predicted_songs = np.array(current_input)
    else:
        input_shape = input_array.shape
        predicted_songs = np.zeros(
            (batch_size, 1, input_shape[2]))
    while index < time_steps:
        output = model.predict(np.array(current_input))
        output = sample(output, temperature=temperature,
                        note_frequency=note_frequency)
        output = output.reshape((-1, 1, NUM_NOTES * MIDI_ARR_SIZE))

        print(f"{index} of {time_steps}. Average notes predicted this timestep: {output.sum() / batch_size}")
        index += 1
        predicted_songs = np.concatenate((predicted_songs, output), axis=1)

        # Add output to new input and remove first timestep in old input to make space
        current_input = np.concatenate((current_input[:, 1:], output), axis=1)
    return np.array(predicted_songs)


def save_songs_and_images(song_array, folder, include_input_in_songs=False):
    for i, song in enumerate(song_array):
        image = song[:, :, NOTE_IND]
        if include_input_in_songs:
            image[:SEQUENCE_LENGTH] *= 128
            image[SEQUENCE_LENGTH:] *= 255
        else:
            image *= 255

        image = image.T
        midi_path, image_path = os.path.join(folder, f'{i}.mid'), os.path.join(
            folder, f'{i}.png')
        cv2.imwrite(image_path,
                    image)
        numpy_to_midi(song, midi_path)


def predict_new_song(temperature, note_frequency, model="most_accurate",
                     batch_size=1,
                     length=400,
                     predict_folder="predicted"):
    input_arr = np.zeros(
        (batch_size, SEQUENCE_LENGTH - 1, NUM_NOTES, MIDI_ARR_SIZE))
    input_arr[:, :, 60:90] = np.random.random(
        (batch_size, SEQUENCE_LENGTH - 1, NUM_NOTES, MIDI_ARR_SIZE))[:, :,
                             60:90]

    input_arr = input_arr.reshape(
        (batch_size, SEQUENCE_LENGTH - 1, NUM_NOTES * MIDI_ARR_SIZE))
    print(input_arr.shape)
    prediction = predict(input_arr,
                         os.path.join(MODELS_FOLDER, model),
                         note_frequency=note_frequency,
                         temperature=temperature, time_steps=length)

    prediction_reshaped = prediction.reshape(
        (batch_size, - 1, NUM_NOTES, MIDI_ARR_SIZE))
    save_songs_and_images(prediction_reshaped, predict_folder)


def continue_song(temperature, note_frequency, model="most_accurate",
                  batch_size=1,
                  length=400,
                  song_folder="E:\datasets\midi\converted",
                  predict_folder="predicted", include_input_in_song=True):
    gen = generator(song_folder, batch_size)

    prediction = predict(gen.__next__()[0],
                         os.path.join(MODELS_FOLDER, model),
                         temperature=temperature, note_frequency=note_frequency,
                         time_steps=length,
                         include_input_in_song=include_input_in_song)

    os.makedirs(predict_folder, exist_ok=True)
    prediction_reshaped = prediction.reshape(
        (batch_size, - 1, NUM_NOTES, MIDI_ARR_SIZE))
    save_songs_and_images(prediction_reshaped, predict_folder,
                          include_input_in_song)
