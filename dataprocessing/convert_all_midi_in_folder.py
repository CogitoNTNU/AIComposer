import numpy as np
from dataprocessing import find_midi_files, midi_to_numpy
from config import SEQUENCE_LENGTH

def convert_all_midi_files_in_folder(folder_path, output_filename="data.h5"):
    paths = find_midi_files.get_midi_files(folder_path)
    numpy_song_list = []
    max_length = 0
    for path in paths:
        print(path)
        try:
            numpy_arr = midi_to_numpy.convert_file(path, save_note_image=True)[0:SEQUENCE_LENGTH]
            if len(numpy_arr) > max_length:
                max_length = len(numpy_arr)
            numpy_song_list.append(numpy_arr)
        except Exception as e:
            print(e)

    numpy_song_list = np.array([np.pad(numpy_song, ((0, max_length-len(numpy_song)),(0,0), (0,0)), "constant", constant_values=(0)) for numpy_song in numpy_song_list])

    with open(output_filename, "wb") as f:
        np.save(f, numpy_song_list)