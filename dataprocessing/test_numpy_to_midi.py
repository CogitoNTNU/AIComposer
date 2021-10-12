from mido import MidiFile, MidiTrack, Message

def numpy_to_midi(array, output_path='test_output.mid'):
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

numpy_to_midi("..\")