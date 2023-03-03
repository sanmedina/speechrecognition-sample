SpeechRecognition & LibreTranslate sample
=========================================

A small sample that shows how to use SpeechRecognition with LibreTranslate. You simply speak a
sentence and the script will try to recognize what you said and translate it with a local service of
LibreTranslate. The main script tries to use the Vosk engine, which is very effective. Only English
and Spanish translations are supported.

There is the `sample_recognition_sample.py` script that tries the engines Sphinx, Vosk and
TensorFlow. The Vosk engine is the only one that works well in this sample.

# Set up

You can use the scripts `build-image.sh` and `run-container.sh` to run locally LibreTranslate.

Run `setup-venv.sh` to a Python virtual environment with all the requirements. Take note that on
Linux, you'll need the development files of PortAudio to access the microphone. If you're on
Ubuntu 20.04, you can install them by running `sudo apt install portaudio19-dev`.

The Vosk engine requires you to download one of their models. Check
https://alphacephei.com/vosk/models, choose one of the models, download it and decompress the files
into a folder called `model` besides `main.py`. Your project should look like the following:

![project-structure](project-structure.png)

The [English lgraph model](https://alphacephei.com/vosk/models/vosk-model-en-us-0.22-lgraph.zip) and
the [Spanish small model](https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip) work
good enough. So, if you want to translate something from Spanish to English, set the small model as
the main one and then run the main script. Set the lgraph as the main model if you wish to translate
from English to Spanish.

# Usage

With the virtual environment activated, run `python3 main.py` and speak any sentence. Alternatively,
use the `run-main.sh` script.
