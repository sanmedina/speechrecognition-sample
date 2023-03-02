from client_libretranslate import detect_language, select_to_translate, translate


def main():
    texts = ["Hola mundo.", "Hello world!"]
    for text in texts:
        detected_language = detect_language(text)
        to_translate_language = select_to_translate(detected_language)
        translation = translate(text, detected_language, to_translate_language)
        print(translation)


if __name__ == "__main__":
    main()
