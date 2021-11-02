import numpy as np
import os
from random import choice, randint, shuffle
from config import SEQUENCE_LENGTH

def load_song(path):
    with open(path, "rb") as f:
        data = np.load(f)
        data = data.reshape((-1, 128*3))
    return data

def generator(datapath="", batch_size=64):

    paths = os.listdir(datapath)

    x_train_array = []
    y_train_array = []


    while True:
        song_array = load_song(os.path.join(datapath, choice(paths)))

        length = song_array.shape[0]
        indices = list(range(length))
        shuffle(indices)

        for note_index in indices:
            start_index = note_index-(SEQUENCE_LENGTH-1)
            if (start_index < 0):
                values_before_predicted = song_array[:note_index]
                length = len(values_before_predicted)
                difference = (SEQUENCE_LENGTH-1) - length
                values_before_predicted = np.pad(values_before_predicted, ((difference, 0), (0, 0)), constant_values=0)
            else:
                values_before_predicted = song_array[start_index:note_index]

            x_train_array.append(values_before_predicted)
            y_train_array.append(song_array[note_index])

            if (len(x_train_array) == batch_size):
                yield (np.array(x_train_array), np.array(y_train_array))
                x_train_array = []
                y_train_array = []

