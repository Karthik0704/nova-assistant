import pyttsx3
from ..core.config import NovaConfig

class SpeechSynthesizer:
    def __init__(self, config: NovaConfig):
        self.config = config
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', config.get('speech.synthesis.rate', 150))
        
        voice_id = config.get('speech.synthesis.voice_id')
        if voice_id:
            self.engine.setProperty('voice', voice_id)

    def speak(self, text: str) -> None:
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
