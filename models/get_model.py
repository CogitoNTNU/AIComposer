from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Concatenate, Input, BatchNormalization
from tensorflow.keras.optimizers import Adam
from config import LEARNING_RATE


def get_model(input_shape, output_shape):
    ord = Input(shape=input_shape)
    out = LSTM(512,name="lstm_0", return_sequences=True)(ord)
    out = Concatenate(axis=2, name="concatenate_0")([out,ord])
    out = Dropout(0.2,name="dropout_0", trainable=True)(out)
    out = LSTM(512,name="lstm_1", trainable=True, return_sequences=True)(out)

    out = Concatenate(axis=2, name="concatenate_1")([out, ord])
    out = LSTM(512, name="lstm_2", trainable=True)(out)

    out = Dense(1024, activation='relu',name="dense_0")(out)
    out = Dense(output_shape, activation='sigmoid', name="dense_1")(out)
    model = Model(ord, out)
    optimizer = Adam(LEARNING_RATE)
    model.compile(loss='binary_crossentropy', optimizer=optimizer,  metrics=["accuracy"])

    return model