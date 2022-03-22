# AI Composer

AI Composer is a student project with a simple task: Create an AI using a keras LSTM model that composes new instrumental music. 

Our project is divided into three parts:
* Data processing
* LSTM model Training
* Pygame Application / song generation

## Requirements
* python 3.8

Optional:
* Cuda + cuDNN for GPU training

## installation
Run ```pip install -r requirements.txt```

## Prepare data
The generator our model uses for training can only process .h5 files. 
To facilitate this you first need a dataset of midi files. 
You then need to set up config.py with the correct values.
#### config values
You can change these values in config.py.
```
# Where the midi files process_data.py uses are stored
MIDI_FOLDER = your dataset path

# Where to store the files converted by process_data.py
CONVERTED_PATH = your converted dataset path
```
#### running
Run process_data.py to start the processing. 
 
## Training
We strongly advise training on a GPU, as it greatly accelerates the training speed.
#### config values
Our training process uses these config values when training. 
```
# Where the trained models are saved
MODELS_FOLDER = your model path

# How many time steps to train on at a time
SEQUENCE_LENGTH = your length

# The batch size to train with
BATCH_SIZE = your batch size

# The training learning rate
LEARNING_RATE = your learning rate

# The number of epochs to train
EPOCHS = your number of epochs

# The number of steps pr epochs
STEPS_PR_EPOCHS = your number of steps pr epochs

# Where to store the files converted by process_data.py
CONVERTED_PATH = your converted files
```
#### running
Run training.py to start the training. 
 
The model will be saved to MODELS_FOLDER/model when done. 
It will also at the end of every epoch save the most accurate model to MODELS_FOLDER/most_accurate and the model with the
 least loss to MODELS_FOLDER/least_loss.
 
 ## Test model
 Run test_model.py to test the model
 
 You can alter the python file to choose whether to create a new song from scratch or
  continue from a song in your CONVERTED_PATH dataset.
  
  
  You can also change the temperature and note frequency of the predicted songs. 
  A higher temperature will mean a more creative and chaotic end song, 
  while a higher note frequency will simply mean more notes.
 
## Results
https://soundcloud.com/espen-fosseide/sets/ai-generated-music?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
