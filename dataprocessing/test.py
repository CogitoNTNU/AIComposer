from music21 import *
from music21 import converter, instrument, midi, note
from find_midi_files import get_midi_files
import numpy as np
import matplotlib.pyplot as plt


NUM_NOTES = 128
Q_RATIO = 4
NOTE_IND = 0
FROM_PREV_IND = 1
VEL_IND = 2

if __name__ == "__main__":
    midi_files = get_midi_files("../midi_filer")
    midi_file = midi_files[1]
    print(midi_file)
    file = converter.parse(midi_file)

    instruments = file.parts
    time_signs = []
    durations = []

    for instrument in instruments:
        print(instrument.partName)

        time_signs.append(instrument.getTimeSignatures()[0])
        durations.append(instrument.duration)

    print(time_signs)
    print(durations)

    time_steps = int(durations[0].quarterLength * Q_RATIO)
    test_arr = np.zeros((time_steps, NUM_NOTES, 3))

    for instr in instruments:
        arr_ind = 0

        for thisNote in instr.flat.notesAndRests:

            duration = thisNote.duration

            if type(thisNote) == note.Note:
                pitch = thisNote.pitch.midi
                vol = thisNote.volume.realized

                stop_ind = arr_ind + int(duration.quarterLength * Q_RATIO)

                test_arr[arr_ind:stop_ind, pitch, NOTE_IND] = 1
                test_arr[arr_ind + 1:stop_ind, pitch, FROM_PREV_IND] = 1
                test_arr[arr_ind:stop_ind, pitch, VEL_IND] = vol

                arr_ind = stop_ind

            if type(thisNote) == chord.Chord:
                stop_ind = arr_ind + int(duration.quarterLength * Q_RATIO)

                for n in thisNote.notes:
                    pitch = n.pitch.midi
                    vol = n.volume.realized

                    test_arr[arr_ind:stop_ind, pitch, NOTE_IND] = 1
                    test_arr[arr_ind + 1:stop_ind, pitch, FROM_PREV_IND] = 1
                    test_arr[arr_ind:stop_ind, pitch, VEL_IND] = vol

                arr_ind = stop_ind

            else:
                arr_ind += int(duration.quarterLength * Q_RATIO)

    plt.imshow(test_arr[:, :, NOTE_IND].T, interpolation="none")
    plt.show()

    # file.plot()
