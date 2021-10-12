from midi_to_numpy import convert_file
from numpy_to_midi import numpy_to_midi

first_arr = convert_file("..\midi_filer\Zelda_Overworld.mid")

numpy_to_midi(first_arr)

second_arr = convert_file("test_output.mid")

comparison = first_arr == second_arr
equal_arrays = comparison.all()

note_comp = comparison[:,:,0]

print("DONE")