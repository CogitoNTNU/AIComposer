
from music21 import converter, instrument, midi
from find_midi_files import get_midi_files
import numpy as np

if __name__ == "__main__":
    midi_files = get_midi_files("../midi_filer")
    file = converter.parse(midi_files[11])
    # print(file.__dict__)
    # print(type(file))
    instruments = file.parts
    time_signs = []
    durations = []
    for instrument in instruments:
        print(instrument.partName)

        time_signs.append(instrument.getTimeSignatures()[0])
        durations.append(instrument.duration)

    print(time_signs)
    print(durations)

    time_steps = int(durations[0].quarterLength * 16)
    test_arr = np.empty((time_steps, 1))
    for thisNote in instruments[0].flat.notesAndRests:
        print(thisNote)
        print(thisNote.fullName)
        print(thisNote.duration)

