from typing import Optional
from ..speech.recognizer import SpeechRecognizer
from ..speech.synthesizer import SpeechSynthesizer
from .config import NovaConfig

class NovaEngine:
    def __init__(self):
        self.config = NovaConfig()
        self.recognizer = SpeechRecognizer(self.config)
        self.synthesizer = SpeechSynthesizer(self.config)
        self.is_running = False

    def start(self):
        self.is_running = True
        self.synthesizer.speak(f"Hello, I am {self.config.get('assistant.name')}. How can I help you?")
        
        while self.is_running:
            command = self.recognizer.listen()
            if command:
                self.process_command(command)

    def process_command(self, command: str) -> None:
        if "stop" in command.lower():
            self.stop()
            return

        # Command processing logic will be added here
        self.synthesizer.speak("I heard you say: " + command)

    def stop(self):
        self.is_running = False
        self.synthesizer.speak("Goodbye!")
