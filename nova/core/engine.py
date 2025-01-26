from typing import Optional
import random
import pyjokes
from ..speech.recognizer import SpeechRecognizer
from ..speech.synthesizer import SpeechSynthesizer
from ..skills.weather import WeatherSkill
from ..skills.time_manager import TimeManager
from ..skills.web_search import WebSearch
from .config import NovaConfig

class NovaEngine:
    def __init__(self):
        self.config = NovaConfig()
        self.recognizer = SpeechRecognizer(self.config)
        self.synthesizer = SpeechSynthesizer(self.config)
        self.weather_skill = WeatherSkill(self.config)
        self.time_manager = TimeManager(self.config)
        self.web_search = WebSearch()
        self.is_running = True
    def start(self):
          self.synthesizer.speak("Hello, I am NOVA. Say 'Hey Nova' to start!")
        
          while self.is_running:
              text = self.recognizer.listen()
            
              if text and "hey nova" in text.lower() or "nova" in text.lower():
                  self.synthesizer.speak("I'm listening! What can I help you with?")
                  command = self.recognizer.listen()
                  if command:
                      self.handle_command(command)
                      # Keep the conversation going
                      self.synthesizer.speak("What else would you like to know?")
            
              elif text and any(word in text.lower() for word in ['goodbye', 'bye', 'stop', 'exit']):
                  self.stop()
            
              elif text:  # Handle direct commands without wake word
                  self.handle_command(text)

    def handle_command(self, command: str):
        if not command:
            return
        
        command = command.lower().strip()
    
        # Time queries - Handle these first and directly
        if any(word in command for word in ['time', 'clock']):
            time_response = self.time_manager.get_time()
            self.synthesizer.speak(time_response)
            return
    
        # Weather queries
        if any(word in command for word in ['weather', 'temperature']):
            self.synthesizer.speak("Getting the latest weather information...")
            weather = self.weather_skill.get_weather("Karnataka")
            self.synthesizer.speak(weather)
            return
    
        # Joke requests
        if 'joke' in command:
            joke = pyjokes.get_joke()
            self.synthesizer.speak(joke)
            return
    
        # Web search - with error handling
        if any(word in command for word in ['who', 'what', 'how', 'tell', 'search']):
            try:
                query = command.replace('who is', '').replace('what is', '').replace('tell me about', '').strip()
                self.synthesizer.speak(f"Looking up information about {query}")
                result = self.web_search.search(query)
                self.synthesizer.speak(result)
            except:
                self.synthesizer.speak("I'm having trouble accessing that information right now. Is there something else I can help you with?")
            return
    
        # Default conversation
        self.synthesizer.speak("I can tell you the time, weather, jokes, or search for information. What would you like to know?")
    def _extract_search_query(self, command: str) -> str:
        # Remove question words and get the actual query
        question_words = ['who is', 'what is', 'how to', 'tell me about', 'when did', 'why is']
        query = command
        for word in question_words:
            query = query.replace(word, '')
        return query.strip()

    def stop(self):
        self.synthesizer.speak("Goodbye! Have a great day!")
        self.is_running = False
