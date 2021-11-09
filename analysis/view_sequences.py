import numpy as np
import os
from random import choice, randint, shuffle
#from config import SEQUENCE_LENGTH
SEQUENCE_LENGTH = 100

def load_song(path):
    with open(path, "rb") as f:
        data = np.load(f)
        data = data.reshape((-1, 128*3)) #returner en sequence men den er ikke padded til 100 enda
        #print("her:", data.shape)
    return data

datapath = '/Users/ulisman/Desktop/python copy/cogito/AIComposer/output' #file path to 'output' folder containting the .h5 files

paths = os.listdir(datapath)
n_files = len(paths) #The amount of files we want to extract the first sequence from
print("n filer: ", n_files)

x_train_array = []
y_train_array = []

first_element_of_x_tain = []

for path in paths[:n_files]:
    song_array = load_song(os.path.join(datapath, path))

    length = song_array.shape[0]
    indices = list(range(length))

    for note_index in indices:
        start_index = note_index - (SEQUENCE_LENGTH-1)
        if (start_index < 0):
            values_before_predicted = song_array[:note_index]
            length = len(values_before_predicted)
            difference = (SEQUENCE_LENGTH-1) - length
            values_before_predicted = np.pad(values_before_predicted, ((difference, 0), (0, 0)), constant_values=0)
        else:
            values_before_predicted = song_array[start_index:note_index]

        x_train_array.append(values_before_predicted)
        y_train_array.append(song_array[note_index])
        
    first_element_of_x_tain.append(x_train_array[0]) #the first element of x_train_array in this iteration is the first sequence of that file

predict_arr = np.mean(np.array(x_train_array[:n_files]), axis=0)
print(predict_arr.shape)
