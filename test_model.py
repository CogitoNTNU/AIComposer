from models.predict import predict_new_song, continue_song
from config import CONVERTED_PATH
continue_song(0.4, "most_accurate", song_folder=CONVERTED_PATH)