import speech_recognition as sr
from ..core.config import NovaConfig

class SpeechRecognizer:
    def __init__(self, config: NovaConfig):
        self.config = config
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = config.get('speech.recognition.energy_threshold', 4000)
        self.timeout = config.get('speech.recognition.timeout', 5)

    def listen(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = self.recognizer.listen(source, timeout=self.timeout)
                text = self.recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                print("Listening timed out")
                return ""
            except sr.UnknownValueError:
                print("Could not understand audio")
                return ""
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return ""
