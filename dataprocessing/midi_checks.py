from music21 import converter, corpus, instrument, midi, note, chord, pitch

def is_piano(file):
    instruments = instrument.partitionByInstrument(file)
    for ins in instruments.recurse().parts:
        if ins.partName == "Piano":
            print("piano")
            return True
    print("nope")
    return False

fil = converter.parse("..\midi_filer\March of the Trolls.mid")

is_piano(fil)

#instrumentPart = instrument.partitionByInstrument(file)

#print(len(instrumentPart.recurse().parts))
#

