from models.training import train
from config import CONVERTED_PATH
train(CONVERTED_PATH, epochs=2000, continue_training=True)