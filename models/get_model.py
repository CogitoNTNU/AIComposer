from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input, Masking, Flatten, Dropout
from tensorflow.keras.optimizers import Adam


def get_model(input_shape, output_shape):
    model = Sequential()
    model.add(Masking(mask_value=1.,
                                      input_shape=(input_shape)))
    model.add(LSTM(128, input_shape=input_shape, return_sequences=True))
    model.add(LSTM(128, return_sequences=True))
    model.add(LSTM(128))
    model.add(Dropout(0.3))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(output_shape, activation="sigmoid"))

    optimizer = Adam(learning_rate=0.0004)
    model.compile(loss='binary_crossentropy', optimizer=optimizer)

    return model