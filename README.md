# Automatic-Speech-Recognition

Create the following directories for your model and audio files:
  - data/audio_examples to place your .wav audio files
  - data/models for the DeepSpeech model files
  - data/transcriptions will be automatically created, which generates the output transcript files

### Installation Requirements

#### Install DeepSpeech
pip3 install deepspeech-gpu
pip3 install tensorflow-gpu==1.15

#### Download pre-trained English model files (Used Version 0.8.1)
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.pbmm

curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.8.1/deepspeech-0.8.1-models.scorer


