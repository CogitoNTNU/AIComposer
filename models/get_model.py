from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from config import LEARNING_RATE


def get_model(input_shape, output_shape):
    model = Sequential()
    model.add(LSTM(512, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(512))
    model.add(Dense(256, activation="relu"))
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(output_shape, activation="sigmoid"))

    optimizer = Adam(LEARNING_RATE)
    model.compile(loss='binary_crossentropy', optimizer=optimizer,  metrics=["accuracy"])

    return model