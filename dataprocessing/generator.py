from config import SEQUENCE_LENGTH, NUM_NOTES
import random
import numpy as np

def generator(data, batch_size,sequence_length = SEQUENCE_LENGTH, num_notes = NUM_NOTES):

    index_tuples = []
    for i, song in enumerate(data):
        for j in range(len(song)):
            index_tuples.append((i,j))

    x_train_array = []
    y_train_array = []

    while True:
        random.shuffle(index_tuples)
        print("EPOCH")
        for index_tuple in index_tuples:
            song_index, sequence_end_index = index_tuple
            song = data[song_index]
            y = sequence_end_index-(sequence_length-1)
            difference = 0
            if y < 0:
                difference = -y
                song = np.pad(song, ((difference,0),(0,0), (0,0)), "constant", constant_values=(1))

            sequence_end_index = max(0, sequence_end_index)
            x_song = song[sequence_end_index-(sequence_length-1)+difference:sequence_end_index+difference]
            y_song = song[sequence_end_index+difference]
            x_train_array.append(x_song)
            y_train_array.append(y_song)

            if len(x_train_array) == batch_size:
                yield np.array(x_train_array).reshape((batch_size, sequence_length-1, num_notes*3)), np.array(y_train_array).reshape((batch_size, num_notes*3))
                x_train_array = []
                y_train_array = []