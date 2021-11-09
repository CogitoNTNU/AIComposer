import os
import random
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from dataprocessing.numpy_to_midi import numpy_to_midi
from dataprocessing.generator import generator
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NOTE_IND, NUM_NOTES, VEL_IND


def predict(input_array, input_model_filepath, time_steps=1, threshold=0.5,
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
        output = model.predict(np.array([current_input]))
        output = output[0].reshape(NUM_NOTES, 3)
        print("step", index, "of", time_steps, ": max value for this step is ", output.max())

        if not use_random_choice:
            output = np.where(output > threshold, 1, 0)
        else:
            uniform = np.random.uniform(0.05, threshold, (NUM_NOTES,1))
            output = np.where(output**2 > np.repeat(uniform, 3, axis=1), 1, 0)

        output = output.flatten()

        index += 1
        predicted_song.append(output)

        # Add output to new input and remove first timestep in old input to make space
        current_input = np.array([*current_input[1:], output])
    return np.array(predicted_song)


def predict_new_song(threshold, model="most_accurate",
                     output_image="predicted_music.png",
                     output_midi="predicted_music.mid"):
    input_arr = np.ones((SEQUENCE_LENGTH - 1, NUM_NOTES, 3))
    input_arr = input_arr.reshape((SEQUENCE_LENGTH - 1, NUM_NOTES * 3)) #simulerer en sequence

    prediction = predict(input_arr,
                         os.path.join(MODELS_FOLDER, model),
                         threshold=threshold, time_steps=400)

    prediction_reshaped = prediction.reshape(
        (- 1, NUM_NOTES, 3))
    cv2.imwrite(output_image,
                prediction_reshaped[:, :, NOTE_IND].T * 255)
    numpy_to_midi(prediction_reshaped, output_midi)


def continue_song(threshold, model="most_accurate",
                  song_folder="E:\datasets\midi\converted",
                  output_image="predicted_music.png",
                  output_midi="predicted_music.mid"):
    gen = generator(song_folder, 1)
    prediction = predict(gen.__next__()[0][0],
                         os.path.join(MODELS_FOLDER, model),
                         threshold=threshold, time_steps=400,
                         include_input_in_song=True)

    prediction_reshaped = prediction.reshape(
        (- 1, NUM_NOTES, 3))
    cv2.imwrite(output_image,
                prediction_reshaped[:, :, NOTE_IND].T * 255)
    numpy_to_midi(prediction_reshaped, output_midi)
