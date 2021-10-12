import tensorflow as tf
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np
from music21 import converter, instrument, note, chord
import glob
from keras.utils import np_utils


vocab = 7 #hvor mange unike variabler


def generate_model(vocab):
    model = tf.keras.Sequential()


    model.add(Embedding(vocab, 64, input_length=len(network_input[0])))
    model.add(LSTM(128))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(vocab, activation='softmax'))

    model.compile(
        optimizer='rmsprop',
        loss='categorical_crossentropy'
    )
    
    return model

model = generate_model()

model.fit(network_input, network_output, epochs=5)
model.save_weights("hgfhyf")  #filnavn