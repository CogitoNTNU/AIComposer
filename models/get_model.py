from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import LSTM, Dense, Input, Masking, Flatten, Dropout, Concatenate, BatchNormalization
from tensorflow.keras.optimizers import Adam


def get_model(input_shape, output_shape):
    model = Sequential()
    model.add(Masking(mask_value=1.,
                                      input_shape=(input_shape)))
    model.add(LSTM(256, input_shape=input_shape))
    optimizer = Adam(learning_rate=0.0001)
    model.compile(optimizer=optimizer, loss='binary_crossentropy',
                  metrics=['accuracy'])
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.4))
    model.add(Dense(output_shape, activation="sigmoid"))
    return model

def get_model2(input_shape, output_shape):
    ord = Input(input_shape)
    out = LSTM(384, name="lstm_0", return_sequences=True, activation="relu")(
        ord)
    out = Concatenate(axis=2, name="concatenate_0")([out, ord])
    out = Dropout(0.2,name="dropout_0", trainable=True)(out)
    out = LSTM(384,name="lstm_1", trainable=True, activation="relu")(out)
    out = Dense(128, activation='relu', name="dense_0")(out)
    out = BatchNormalization(name="batch_normalization_0")(out)
    out = Dense(output_shape, activation='sigmoid', name="dense_1")(out)
    model = Model(ord, out)
    optimizer = Adam(learning_rate=0.001)
    model.compile(optimizer=optimizer, loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

def generateModel9(training = True,trainable = True):
    ord = Input(shape=(49,))
    out = LSTM(512,name="lstm_0", return_sequences=True, trainable=trainable)(e)
    #e = Flatten(name="flatten_0")(e)
    out = Concatenate(axis=2, name="concatenate_0")([out,e])
    out = Dropout(0.2,name="dropout_0", trainable=True)(out)
    out = LSTM(512,name="lstm_1", trainable=True, return_sequences=True)(out)

    out = Concatenate(axis=2, name="concatenate_1")([out, e])
    out = LSTM(512, name="lstm_2", trainable=trainable)(out)

    out = Dense(1024, activation='relu',name="dense_0")(out)
    out = BatchNormalization(name="batch_normalization_0")(out)
    out = Dense(VOCABULARY_SIZE, activation='sigmoid', name="dense_1")(out)
    model = Model(ord, out)
    optimizer = optimizers.Adam(learning_rate=LEARNING_RATE)
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    return model