import pyttsx3


def test_to_speech(text, lang='english'):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 40)
    engine.setProperty('voice', lang)
    engine.say(text)
    engine.runAndWait()


test_to_speech('Chancellor on brink of second bailout for banks.')
