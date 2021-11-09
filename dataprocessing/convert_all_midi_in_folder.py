import numpy as np
from dataprocessing import find_midi_files, midi_to_numpy
from config import SEQUENCE_LENGTH
from pathlib import Path
import os
def convert_all_midi_files_in_folder(folder_path, output_filename="data", save_individually=False):
    paths = find_midi_files.get_midi_files(folder_path)
    numpy_song_list = []
    count = len(paths)
    for i, path in enumerate(paths):
        print(i, "of",count, ": ", path)
        try:
            numpy_arr = midi_to_numpy.convert_file(path, save_note_image=True)
            if save_individually:
                with open(os.path.join(output_filename, str(Path(os.path.basename(path)).with_suffix(".h5"))), "wb") as f:
                    np.save(f, numpy_arr)
            else:
                numpy_song_list.append(numpy_arr)
        except Exception as e:
            print(e)
    if not save_individually:
        numpy_song_list = np.array(numpy_song_list)
        with open(output_filename,"wb") as f:
            np.save(f, numpy_song_list)
