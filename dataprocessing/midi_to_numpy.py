import numpy as np # linear algebra
import pandas as pd
from music21 import converter, corpus, instrument, midi, note, chord, pitch

file = converter.parse("..\midi_filer\March of the Trolls.mid")

instrumentPart = instrument.partitionByInstrument(file)

print(len(instrumentPart.recurse().parts))

for ins in instrumentPart.recurse().parts:
    print(ins.partName)
    ins_notes = ins.notesAndRests.stream()
    for some in ins_notes.elements:
        if type(some)==chord.Chord:
            print("Chord",some)
        elif some.name == "rest":
            print("rest")
        else:
            print("Note",some.name)
            print("Note octave",some.octave)
