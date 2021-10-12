import numpy

from midi_to_numpy import convert_file
from numpy_to_midi import numpy_to_midi

first_arr = convert_file("..\midi_filer\Gold_Silver_Rival_Battle.mid")

numpy_to_midi(first_arr)

second_arr = convert_file("test_output.mid")

print("First:")
print(first_arr.shape)
print("Second:")
print(second_arr.shape)

comparison = numpy.equal(first_arr,second_arr)

note_comp = comparison[:,:,0]

for i in range(len(note_comp)):
    for j in range(len(note_comp[i])):
        if note_comp[i,j] == False:
            print("Feil på timestep:"+str(i)+" note:"+str(j))


print("DONE")