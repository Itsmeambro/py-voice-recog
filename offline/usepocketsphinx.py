import os
import sys
import pyaudio
import pocketsphinx
from pocketsphinx import LiveSpeech

model_dir = "./model"

# Set up the parameters for the LiveSpeech object
speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_dir, 'en-us'),
    lm=os.path.join(model_dir, 'en-us.lm.bin'),
    dic=os.path.join(model_dir, 'cmudict-en-us.dict')
)

print("Starting live speech recognition...")
for phrase in speech:
    print("You said: ", phrase)

