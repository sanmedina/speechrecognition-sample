from datetime import datetime
import traceback

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print(datetime.now())
    print('say something')
    audio = r.listen(source)
    print(datetime.now())


# Doesn't work well
try:
    print('recognizing...')
    print(datetime.now())
    print("Sphinx thinks you said:", f"'{r.recognize_sphinx(audio)}'")
    print(datetime.now())
except Exception:
    traceback.print_exc()


# Works well
try:
    print('recognizing...')
    print(datetime.now())
    print("Vosk thinks you said:", f"'{r.recognize_vosk(audio)}'")
    print(datetime.now())
except Exception:
    traceback.print_exc()


# Doesn't work
try:
    print('recognizing...')
    print(datetime.now())
    print("Tensorflow thinks you said:", f"'{r.recognize_tensorflow(audio)}'")
    print(datetime.now())
except Exception:
    traceback.print_exc()
