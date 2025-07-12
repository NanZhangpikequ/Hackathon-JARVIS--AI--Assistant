import speech_recognition as sr

def recognize_audio(file_path):
    # Recognizes and transcribes speech from an audio file
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Speech not recognized"
        except sr.RequestError:
            return "Speech recognition failed"
