from music21 import *
from music21 import converter, note
from mido import MidiFile
import cv2
import numpy as np
import os
from config import NUM_NOTES, Q_RATIO, NOTE_IND, FROM_PREV_IND, \
    NOTE_IMAGE_FILE_FOLDER, MIDI_ARR_SIZE

def convert_file(filename, save_note_image=False):
    """
    Converts a midi file to numpy
    :param filename: the midi file to convert
    :param save_note_image: whether to save the numpy arrays as an image or not
    :return: A numpy array that represents the midi file
    """
    mid = MidiFile(filename)
    song_length = mid.length
    if song_length > 60*10:
        raise ValueError("File too long")
    elif song_length < 10:
        raise ValueError("File too short")
    file = converter.parse(filename)
    instruments = file.parts
    time_signs = []
    durations = []

    for instrument in instruments:
        time_signs.append(instrument.getTimeSignatures()[0])
        durations.append(instrument.duration)

    time_steps = int(durations[0].quarterLength * Q_RATIO)
    midi_arr = np.zeros((time_steps, NUM_NOTES, MIDI_ARR_SIZE))

    for instr in instruments:
        arr_ind = 0

        for thisNote in instr.flat.notesAndRests:

            duration = thisNote.duration

            if type(thisNote) == note.Note:
                pitch = thisNote.pitch.midi
                arr_ind = int(thisNote.offset * Q_RATIO)
                stop_ind = arr_ind + int(duration.quarterLength * Q_RATIO)
                midi_arr[arr_ind:stop_ind, pitch, NOTE_IND] = 1
                if (stop_ind - arr_ind > 1):
                    midi_arr[arr_ind + 1:stop_ind, pitch, FROM_PREV_IND] = 1

                arr_ind = stop_ind

            if type(thisNote) == chord.Chord:
                arr_ind = int(thisNote.offset * Q_RATIO)
                stop_ind = arr_ind + int(duration.quarterLength * Q_RATIO)

                for n in thisNote.notes:
                    pitch = n.pitch.midi

                    midi_arr[arr_ind:stop_ind, pitch, NOTE_IND] = 1
                    midi_arr[arr_ind + 1:stop_ind, pitch, FROM_PREV_IND] = 1

                arr_ind = stop_ind

            else:
                arr_ind += int(duration.quarterLength * Q_RATIO)

    if save_note_image:
        os.makedirs(NOTE_IMAGE_FILE_FOLDER, exist_ok=True)
        print(os.path.join(NOTE_IMAGE_FILE_FOLDER, filename[:-4] + ".png"))
        cv2.imwrite(os.path.join(NOTE_IMAGE_FILE_FOLDER, os.path.basename(filename[:-4]) + ".png"),
                    midi_arr[:, :, NOTE_IND].T * 255)

    return midi_arr


def save_file(filename, output_filename="processed_songs/song.h5", **kwargs):
    np_arr = convert_file(filename, **kwargs)
    with open(output_filename, "wb") as f:
        np.save(f, np_arr)