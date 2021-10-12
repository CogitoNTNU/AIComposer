import numpy as np

SEQUENCE_LENGTH = 100

def generator(data_filepath):
    with open(data_filepath, "rb") as f:
        data = np.load(f)

