import mido

mid = mido.MidiFile("..\midi_filer\Fur Elise.mid", clip="True")
print(mid.tracks)