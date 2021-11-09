from music21 import converter, corpus, instrument, midi, note, chord, pitch

#list of all instruments in file
def list_of_instruments(midi):
    part_of_stream=midi.parts.stream()
    all_instu=[]
    for inst in part_of_stream:

        all_instu.append(inst.partName);
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

