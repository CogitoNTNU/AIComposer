# Where the trained models are saved
MODELS_FOLDER = "saved_models"

# How many time steps to train on at a time
SEQUENCE_LENGTH = 500

# The batch size to train with
BATCH_SIZE = 128

# The training learning rate
LEARNING_RATE = 0.0001333

# The number of epochs to train
EPOCHS = 2000

# The number of steps pr epochs
STEPS_PR_EPOCHS = 1000000

# Total number of different notes. Midi files supports 128
NUM_NOTES = 128

# How many quarter notes pr time step
Q_RATIO = 4

# Which index the note pitch has in the training array
NOTE_IND = 0

# Which index the "continue note" has in the training array
FROM_PREV_IND = 1

# How large each note array is
MIDI_ARR_SIZE = 2

# Where the midi files process_data.py uses are stored
MIDI_FOLDER = f"E:\datasets\midi" # "/Users/theodorforgaard/Downloads/lmd_matched/C/F"

# Where to store the files converted by process_data.py
CONVERTED_PATH = f"E:\datasets\midi\converted" # "./converted"

# Where the predicted songs are to be stored
PREDICTED_SONG_FOLDER = "predicted"

# Where to store image representations of the converted midi files
NOTE_IMAGE_FILE_FOLDER = "note_imgs"

# Full list: https://soundprogramming.net/file-formats/general-midi-instrument-list/
# Note: midos instruments are 0 indexed, this list is not.
instruments = {
    "piano": 0,
    "acoustic guitar": 24,
    "electric guitar": 26,
    "distortion guitar": 30,
    "acoustic bass": 32,
    "electric bass": 33,
    "violin": 40,
    "contrabass": 43,
    "choir aahs": 52, # Good one
    "voice oohs": 53,
    "flute": 73,
    "whistle": 78,
    "fiddle": 110,
    "steel drums": 114,
    "bird tweet": 123,
    "gunshot": 127, # :O

}

# Which instrument to use when converting from numpy to midi
INSTRUMENT = instruments["gunshot"]