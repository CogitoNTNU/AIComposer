import numpy as np
from random import shuffle
from config import SEQUENCE_LENGTH
def generator(datapath="", batch_size=64):
    with open(datapath, "rb") as f:
        data = np.load(f, allow_pickle=True)
        data = [song.reshape((-1, 128*3)) for song in data]

    x_train_array = []
    y_train_array = []

    while True:
        # Gets all possible combinations of song index and predicted note indices
        indices = []
        for i, song_array in enumerate(data):
            for j in range(len(song_array)):
                indices.append((i, j))

        # Randomized indices
        shuffle(indices)

        # Iterate through index pairs
        for index_pair in indices:
            song, note_index = index_pair
            song_array = data[song]

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

