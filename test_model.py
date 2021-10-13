import numpy as np
import os
from models.predict import predict
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NOTE_IND, NUM_NOTES
from dataprocessing.numpy_to_midi import numpy_to_midi
import cv2
import random

SONGS_TO_GENERATE = 100

for i in range(SONGS_TO_GENERATE):
    input_arr = np.zeros((SEQUENCE_LENGTH-1, NUM_NOTES, 3))
    random_note = random.randint(0,NUM_NOTES-1)
    input_arr[-1, random_note ,0] = 1
    input_arr[-1, random_note ,2] = 1
    input_arr = input_arr.reshape((SEQUENCE_LENGTH-1, NUM_NOTES*3))
    input_arr = np.random.rand(*(SEQUENCE_LENGTH-1, NUM_NOTES*3))

    prediction = predict(input_arr, os.path.join(MODELS_FOLDER, "model"), threshold=0.5, time_steps=200)

    prediction_reshaped = prediction.reshape((-1, NUM_NOTES,3))


    cv2.imwrite(f"predicted/{i}predicted_music.png", prediction_reshaped[:, :, NOTE_IND].T*255)
    numpy_to_midi(prediction_reshaped, f"predicted/{i}predicted_music.mid")