import os
import numpy as np
from models.get_model import get_model
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NUM_NOTES


def train(data_filepath, epochs=1, model_filename="model"):
    with open(data_filepath, "rb") as f:
        data = np.load(f)

    data_shape = data.shape
    data = data.reshape(
        (data_shape[0], data_shape[1], data_shape[2] * data_shape[3]))

    x_train = data[:, 0:SEQUENCE_LENGTH - 1]
    y_train = data[:, SEQUENCE_LENGTH - 1]

    model = get_model(input_shape=x_train[0].shape, output_shape=(NUM_NOTES*3))

    model.fit(x_train, y_train, validation_split=0.1, epochs=epochs)

    os.makedirs(MODELS_FOLDER, exist_ok=True)
    model.save(os.path.join(MODELS_FOLDER, model_filename))