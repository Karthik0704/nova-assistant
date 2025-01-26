import numpy as np
import sounddevice as sd
from threading import Thread
import queue

class WakeWordDetector:
    def __init__(self, config):
        self.config = config
        self.wake_word = config.get('assistant.wake_word', 'hey nova').lower()
        self.is_activated = False

    def detect_wake_word(self, command: str) -> bool:
        if self.wake_word in command.lower():
            self.is_activated = True
            return True
        return False

    def is_wake_word_active(self) -> bool:
        return self.is_activated

    def reset_activation(self):
        self.is_activated = False