import pyttsx3

class SpeechSynthesizer:
    def __init__(self, config):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', config.get('speech.synthesis.rate', 150))
        self.engine.setProperty('volume', 1.0)
        
        # Set a clear voice
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)  # Index 0 for male, 1 for female

    def speak(self, text: str):
        print(f"A: {text}")  # Terminal output
        self.engine.say(text)
        self.engine.runAndWait()
