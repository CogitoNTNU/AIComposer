from models.predict import predict_new_song, continue_song
from config import CONVERTED_PATH, PREDICTED_SONG_FOLDER

#predict_new_song(temperature=0.8, note_frequency=1, batch_size=20,
#                 model="least_loss", predict_folder=PREDICTED_SONG_FOLDER)
continue_song(temperature=0.8, note_frequency=1.3, batch_size=20, model="least_loss",
               song_folder=CONVERTED_PATH, predict_folder=PREDICTED_SONG_FOLDER,
               include_input_in_song=True)