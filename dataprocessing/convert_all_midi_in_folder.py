import numpy as np
from dataprocessing import find_midi_files, midi_to_numpy
from config import SEQUENCE_LENGTH

def convert_all_midi_files_in_folder(folder_path, output_filename="data.h5"):
    paths = find_midi_files.get_midi_files(folder_path)
    numpy_song_list = []
    file_count = 1 #kan ta bort, er bare for testing
    for path in paths:
        try:
            numpy_arr = midi_to_numpy.convert_file(path, save_note_image=True)
            numpy_song_list.append(numpy_arr)
        except Exception as e:
            print("Exception:", e)

        file_count = file_count + 1#kan ta bort, er bare for testing

    with open(output_filename, "wb") as f:
        np.save(f, numpy_song_list)
