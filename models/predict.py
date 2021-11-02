import numpy as np
from tensorflow.keras.models import load_model

def predict(input_array, input_model_filepath, time_steps=1, threshold=0.5):
    model = load_model(input_model_filepath)
    output_array = []
    current_input = input_array
    for i in range(time_steps):
        output = model.predict(np.array([current_input]))
        print(np.max(output))
        output = output[0]
        if np.max(output) < threshold:
            num_top = 12
            ind = np.argpartition(output, -num_top)[-num_top:]
            output = np.zeros(output.shape)
            output[ind] = 1
        else:
            output = np.where(output > threshold, 1, 0)
        output_array.append(output)
        current_input = np.array([*current_input[1:], output])
    return np.array(output_array)

