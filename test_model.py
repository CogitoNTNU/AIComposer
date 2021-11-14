from models.predict import predict_new_song, continue_song
from config import CONVERTED_PATH
predict_new_song(temperature=0.8, note_frequency=1, model="most_accurate")
#continue_song(temperature=1, note_frequency=1, model="most_accurate", song_folder=CONVERTED_PATH, include_input_in_song=True)