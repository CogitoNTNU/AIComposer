from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input, Masking, Flatten



def get_model(input_shape, output_shape):
    model = Sequential()
    model.add(LSTM(32, input_shape=input_shape))
    model.add(Flatten())
    model.add(Dense(output_shape, activation="sigmoid"))

    model.compile(loss='binary_crossentropy', optimizer='adam')

    return model