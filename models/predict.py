import numpy as np
from tensorflow.keras.models import load_model

def predict(input_array, input_model_filepath, time_steps=1, threshold=0.5):
    model = load_model(input_model_filepath)

    current_input = input_array
    for i in range(time_steps):
        output = model.predict(np.array([current_input]))
        print(output)
        output = np.where(output > threshold, 1, 0)
        current_input = np.array([*current_input[1:], output[0]])
    return current_input

