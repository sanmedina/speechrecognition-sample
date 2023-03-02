import json

from client_libretranslate import detect_language, select_to_translate, translate
import speech_recognition as sr


def _detect_text() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    result = r.recognize_vosk(audio)
    result_dict = json.loads(result)
    return result_dict["text"]


def main():
    recognized_text = _detect_text()
    print("Recognized text:", recognized_text)
    detected_language = detect_language(recognized_text)
    to_translate = select_to_translate(detected_language)
    translation = translate(recognized_text, detected_language, to_translate)
    print("Translation:", translation)


if __name__ == "__main__":
    main()
