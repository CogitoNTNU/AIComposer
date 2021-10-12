from mido import MidiFile, MidiTrack, Message

def numpy_to_midi(array, output_path='test_output.mid'):
    """
    This function takes in a numpy array and converts it to midi file
    :param array: the numpy array to convert
    :param output_path: Where to save the new midi file
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    ticks_per_beat = mid.ticks_per_beat
    ticks_per_measure = 4 * ticks_per_beat
    ticks_per_sample = int(ticks_per_measure / 16)

    curr_notes = [0 for _ in range(128)]
    abs_time = 0
    last_time = 0

    for i, time_step in enumerate(array):
        print(i, sum(time_step))
        for j, note_arr in enumerate(time_step):
            volume = int(note_arr[2] * 127)
            if (note_arr[0] and not curr_notes[j]):
                delta_time = abs_time - last_time
                track.append(Message('note_on', note=j, velocity=volume,
                                     time=delta_time))
                last_time = abs_time
                curr_notes[j] = 1
            elif note_arr[0] and not note_arr[1] and curr_notes[j]:
                delta_time = abs_time - last_time
                track.append(Message('note_off', note=j, time=delta_time))
                delta_time = 0
                track.append(Message('note_on', note=j, velocity=volume,
                                     time=delta_time))
                last_time = abs_time
            elif (curr_notes[j] and not note_arr[0]):
                delta_time = abs_time - last_time
                track.append(Message('note_off', note=j, time=delta_time))
                last_time = abs_time
                curr_notes[j] = 0
        abs_time += ticks_per_sample
    mid.save(output_path)
