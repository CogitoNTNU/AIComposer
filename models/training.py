import os
import numpy as np
from models.get_model import get_model
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NUM_NOTES, BATCH_SIZE
from dataprocessing.generator import generator

from tensorflow.keras.callbacks import ModelCheckpoint


def train(data_filepath, epochs=1, model_filename="model"):
    with open(data_filepath, "rb") as f:
        data = np.load(f, allow_pickle=True)
        total_steps = 0
        for dat in data:
            total_steps += dat.shape[0]

    gen = generator(data, batch_size=BATCH_SIZE)
    out = gen.__next__()
    model = get_model(input_shape=(SEQUENCE_LENGTH - 1, NUM_NOTES * 3),
                      output_shape=(NUM_NOTES * 3))

    model_checkpoint_callback = ModelCheckpoint(
        filepath=os.path.join(MODELS_FOLDER, "version{epoch:02d}"),
        monitor='accuracy',
        mode='max',
        save_best_only=True,
        verbose=True)

    model.fit(gen, epochs=epochs, batch_size=BATCH_SIZE,
              steps_per_epoch=total_steps // BATCH_SIZE,
              callbacks=[model_checkpoint_callback])

    os.makedirs(MODELS_FOLDER, exist_ok=True)
    model.save(os.path.join(MODELS_FOLDER, model_filename))
