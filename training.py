from models.training import train
from config import CONVERTED_PATH, EPOCHS
train(CONVERTED_PATH, epochs=EPOCHS, continue_training=True)