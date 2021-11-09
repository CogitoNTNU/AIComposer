from models.training import train
from config import CONVERTED_PATH
train(CONVERTED_PATH, epochs=20, continue_training=False)