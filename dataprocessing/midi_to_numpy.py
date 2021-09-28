import numpy as np # linear algebra
import pandas as pd
from music21 import converter, corpus, instrument, midi, note, chord, pitch

from find_midi_files import get_midi_files



#list of all instruments in file
def list_of_instruments(midi):
    part_of_stream=midi.parts.stream()
    all_instu=[]
    for inst in part_of_stream:
        aux=inst;
        all_instu.append(aux);
    return all_instu


# open midi file
def open_midi(path):
    midi_file=midi.midiFile()
    midi_file.open(path)
    midi_file.read()
    return midi.translate.midiFileToStream(midi_file)


#checking if piano is there.Boolean function
def correct_file(all_instu):
    for i in range(len(all_instu)):
        if(all_instu[i]!="Piano" or all_instu[i]!="None"):
            return False
    return True









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
