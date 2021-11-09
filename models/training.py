import os
import numpy as np
from models.get_model import get_model
from config import SEQUENCE_LENGTH, MODELS_FOLDER, NUM_NOTES, BATCH_SIZE
from dataprocessing.generator import generator
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model
def train(data_filepath, epochs=1, model_filename="model", continue_training=False):
    gen = generator(data_filepath, batch_size=BATCH_SIZE)

    if continue_training:
        model = load_model(os.path.join(MODELS_FOLDER, "most_accurate"))
    else:
        model = get_model(input_shape=(SEQUENCE_LENGTH-1, NUM_NOTES*3), output_shape=(NUM_NOTES*3))

    model_checkpoint_callback_accr = ModelCheckpoint(
        filepath=os.path.join(MODELS_FOLDER, "most_accurate"),
        monitor='accuracy',
        mode='max',
        save_best_only=True,
        verbose=True)
<<<<<<< HEAD
    model.fit(gen, epochs=epochs, steps_per_epoch=10000//BATCH_SIZE, batch_size=BATCH_SIZE, callbacks=[model_checkpoint_callback])
=======
    model_checkpoint_callback_loss = ModelCheckpoint(
        filepath=os.path.join(MODELS_FOLDER, "least_loss"),
        monitor='loss',
        mode='min',
        save_best_only=True,
        verbose=True)

    model.fit(gen, epochs=epochs, steps_per_epoch=4000000//BATCH_SIZE, batch_size=BATCH_SIZE, callbacks=[model_checkpoint_callback_accr, model_checkpoint_callback_loss])
>>>>>>> master

    os.makedirs(MODELS_FOLDER, exist_ok=True)
    model.save(os.path.join(MODELS_FOLDER, model_filename))