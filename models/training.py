import os
import numpy as np
from models.get_model import get_model
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NUM_NOTES, BATCH_SIZE
from dataprocessing.generator import generator
from tensorflow.keras.callbacks import ModelCheckpoint

def train(data_filepath, epochs=1, model_filename="model"):
    gen = generator(data_filepath, batch_size=BATCH_SIZE)

    model = get_model(input_shape=(SEQUENCE_LENGTH-1, NUM_NOTES*3), output_shape=(NUM_NOTES*3))

    model_checkpoint_callback = ModelCheckpoint(
        filepath=os.path.join(MODELS_FOLDER, "most_accurate"),
        monitor='accuracy',
        mode='max',
        save_best_only=True,
        verbose=True)
    model.fit(gen, epochs=epochs, steps_per_epoch=1000//BATCH_SIZE, batch_size=BATCH_SIZE, callbacks=[model_checkpoint_callback])

    os.makedirs(MODELS_FOLDER, exist_ok=True)
    model.save(os.path.join(MODELS_FOLDER, model_filename))