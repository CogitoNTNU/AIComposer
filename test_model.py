import numpy as np
import os
from models.predict import predict
from config import SEQUENCE_LENGTH, MODELS_FOLDER
from dataprocessing.numpy_to_midi import numpy_to_midi

input_arr = np.zeros((SEQUENCE_LENGTH-1, 384))
prediction = predict(input_arr, os.path.join(MODELS_FOLDER, "model"), threshold=0.07, time_steps=99)

prediction_reshaped = prediction.reshape((SEQUENCE_LENGTH-1, 128,3))
print(prediction)

numpy_to_midi(prediction_reshaped, "predicted_music.mid")