import os
import numpy as np
from models.get_model import get_model
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NUM_NOTES
import random
def train(data_filepath, epochs=1, model_filename="model"):
    with open(data_filepath, "rb") as f:
        data = np.load(f, allow_pickle=True)

    training_data_x = []
    training_data_y = []
    num_songs = len(data)
    for i, song in enumerate(data):
        print("song", i, "of", num_songs)
        song_length = len(song)
        print(song_length)
        sample = random.sample(range(0,song_length-SEQUENCE_LENGTH), (song_length-SEQUENCE_LENGTH)//4)
        for i in sample:
            y = i-(SEQUENCE_LENGTH-1)
            if y < 0:
                difference = -y
                song = np.pad(song, ((difference,0),(0,0), (0,0)), "constant", constant_values=(1))

            i = max(0, i)
            x_song = song[i:i+SEQUENCE_LENGTH-1]
            y_song = song[i+SEQUENCE_LENGTH]
            training_data_x.append(x_song)
            training_data_y.append(y_song)

    c = list(zip(training_data_x, training_data_y))

    random.shuffle(c)

    training_data_x, training_data_y = zip(*c)
    training_data_x = np.array(training_data_x)
    training_data_y = np.array(training_data_y)
    
    x_shape = training_data_x.shape
    y_shape = training_data_y.shape

    training_data_x = training_data_x.reshape((x_shape[0], x_shape[1], x_shape[2] * x_shape[3]))
    training_data_y = training_data_y.reshape((y_shape[0], y_shape[1] * y_shape[2]))

    print(training_data_x.shape)
    print(training_data_y.shape)
    model = get_model(input_shape=training_data_x[0].shape, output_shape=(NUM_NOTES*3))

    model.fit(training_data_x, training_data_y, validation_split=0.1, epochs=epochs)

    os.makedirs(MODELS_FOLDER, exist_ok=True)
    model.save(os.path.join(MODELS_FOLDER, model_filename))