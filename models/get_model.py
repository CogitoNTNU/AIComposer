from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input, Masking, Flatten

HIDDEN_SIZE = 128


def get_model(input_shape, output_shape):
    model = Sequential()
    model.add(LSTM(128, input_shape=input_shape))
    model.add(Flatten())
    model.add(Dense(output_shape, activation="sigmoid"))

    model.compile(loss='mean_squared_error', optimizer='adam')

    return model