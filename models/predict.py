import os
import random
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from dataprocessing.numpy_to_midi import numpy_to_midi
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NOTE_IND, NUM_NOTES


def predict(input_array, input_model_filepath, time_steps=1, threshold=0.5):
    model = load_model(input_model_filepath)

    current_input = input_array
    for i in range(time_steps):
        output = model.predict(np.array([current_input]))
        print(output.max())
        output = np.where(output > threshold, 1, 0)
        current_input = np.array([*current_input[1:], output[0]])
    return current_input


def predict_new_song(threshold, model="most_accurate", output_image="predicted_music.png",
                     output_midi="predicted_music.mid"):
    input_arr = np.zeros((SEQUENCE_LENGTH - 1, NUM_NOTES, 3))
    random_note = random.randint(40, 70)
    input_arr[-4:, random_note, 0] = 1
    input_arr[-3:, random_note, 1] = 1
    input_arr[-4, random_note, 2] = 1
    input_arr = input_arr.reshape((SEQUENCE_LENGTH - 1, NUM_NOTES * 3))

    prediction = predict(input_arr,
                         os.path.join(MODELS_FOLDER, model),
                         threshold=threshold, time_steps=99)

    prediction_reshaped = prediction.reshape(
        (SEQUENCE_LENGTH - 1, NUM_NOTES, 3))

    cv2.imwrite(output_image,
                prediction_reshaped[:, :, NOTE_IND].T * 255)
    numpy_to_midi(prediction_reshaped, output_midi)
