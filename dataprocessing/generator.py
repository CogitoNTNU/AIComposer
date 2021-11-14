import numpy as np
import os
from random import choice, shuffle, randint
from config import SEQUENCE_LENGTH, MIDI_ARR_SIZE, NUM_NOTES

def load_song(path):
    with open(path, "rb") as f:
        data = np.load(f)
        data = data.reshape((-1, NUM_NOTES * MIDI_ARR_SIZE))
    return data

def replace_song(songs, indices, song_index, path):
    songs[song_index] = load_song(path)
    indices[song_index] = list(range(len(songs[song_index])))
    shuffle(indices[song_index])

def generator(datapath="", batch_size=64, songs_in_memory=1000):

    paths = os.listdir(datapath)

    x_train_array = []
    y_train_array = []

    songs = []
    indices = []
    for i in range(songs_in_memory):
        songs.append(load_song(os.path.join(datapath, choice(paths))))
        indices.append(list(range(len(songs[-1]))))
        shuffle(indices[-1])

    while True:


        song_index = randint(0, songs_in_memory-1)
        song_array = songs[song_index]

        note_index = indices[song_index].pop()
        if not len(indices[song_index]):
            replace_song(songs, indices, song_index, os.path.join(datapath, choice(paths)))

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

