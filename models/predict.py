import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from dataprocessing.numpy_to_midi import numpy_to_midi
from dataprocessing.generator import generator
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NOTE_IND, NUM_NOTES, MIDI_ARR_SIZE
from random import randint

def sample(preds, note_frequency=1, temperature=1):
    total_pred_sum = round(np.sum(preds)*note_frequency)
    if not total_pred_sum:
        preds[:] = 0
        return preds
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(total_pred_sum, preds, 1)[0]
    print(probas)
    over0= np.where(probas > 0)
    preds[:] = 0
    preds[over0] = 1
    return preds

def predict(input_array, input_model_filepath, time_steps=1, temperature=1,note_frequency=1,
            include_input_in_song=False, use_random_choice=False):
    model = load_model(input_model_filepath)
    print(model.summary())
    current_input = input_array
    index = 0
    if include_input_in_song:
        predicted_song = [*current_input]
    else:
        predicted_song = []
    while index < time_steps:
        print(current_input.shape)
        output = model.predict(np.array([current_input]))[0]
        output = sample(output, temperature=temperature, note_frequency=note_frequency)
        print(output)
        # output = output.reshape(NUM_NOTES, MIDI_ARR_SIZE)
        # print("step", index, "of", time_steps, ": max value for this step is ", output.max())
        #
        #
        # if not use_random_choice:
        #     output = np.where(output > threshold, 1, 0)
        # else:
        #     uniform = np.random.uniform(0.05, threshold, (NUM_NOTES,1))
        #     output = np.where(output**2 > np.repeat(uniform, MIDI_ARR_SIZE, axis=1), 1, 0)
        #
        # output = output.flatten()

        index += 1
        predicted_song.append(output)

        # Add output to new input and remove first timestep in old input to make space
        current_input = np.array([*current_input[1:], output])
    return np.array(predicted_song)


def predict_new_song(temperature, note_frequency, model="most_accurate",
                     output_image="predicted_music.png",
                     output_midi="predicted_music.mid"):
    input_arr = np.zeros((SEQUENCE_LENGTH - 1, NUM_NOTES, MIDI_ARR_SIZE))
    input_arr[:, 60:90] = np.random.random((SEQUENCE_LENGTH - 1, NUM_NOTES, MIDI_ARR_SIZE))[:, 60:90]

    #for i in range(4):
    #    random_note = randint(0, NUM_NOTES-1)
    #    input_arr[-4:, random_note, :] = 1
    input_arr = input_arr.reshape((SEQUENCE_LENGTH - 1, NUM_NOTES * MIDI_ARR_SIZE))
    print(input_arr.sum(axis=0))
    prediction = predict(input_arr,
                         os.path.join(MODELS_FOLDER, model),
                         note_frequency=note_frequency,
                         temperature=temperature, time_steps=400)

    prediction_reshaped = prediction.reshape(
        (- 1, NUM_NOTES, MIDI_ARR_SIZE))
    cv2.imwrite(output_image,
                prediction_reshaped[:, :, NOTE_IND].T * 255)
    numpy_to_midi(prediction_reshaped, output_midi)


def continue_song(temperature, note_frequency, model="most_accurate",
                  song_folder="E:\datasets\midi\converted",
                  output_image="predicted_music.png",
                  output_midi="predicted_music.mid", include_input_in_song=True):
    gen = generator(song_folder, 1)

    prediction = predict(gen.__next__()[0][0],
                         os.path.join(MODELS_FOLDER, model),
                         temperature=temperature, note_frequency=note_frequency, time_steps=400,
                         include_input_in_song=include_input_in_song, use_random_choice=False)

    prediction_reshaped = prediction.reshape(
        (- 1, NUM_NOTES, MIDI_ARR_SIZE))
    image = prediction_reshaped[:, :, NOTE_IND]
    if include_input_in_song:
        image[:SEQUENCE_LENGTH] *=128
        image[SEQUENCE_LENGTH:] *= 255
    else:
        image *= 255

    image = image.T
    cv2.imwrite(output_image,
                image)
    numpy_to_midi(prediction_reshaped, output_midi)

