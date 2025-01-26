import wikipedia
from typing import Optional

class WebSearch:
    def __init__(self):
        wikipedia.set_lang("en")
    
    def search(self, query: str) -> str:
        try:
            # First attempt direct search
            result = wikipedia.summary(query, sentences=2)
            return result
        except wikipedia.exceptions.DisambiguationError as e:
            # Handle multiple matches
            return wikipedia.summary(e.options[0], sentences=2)
        except wikipedia.exceptions.PageError:
            # Try search suggestions
            suggestions = wikipedia.search(query, results=1)
            if suggestions:
                return wikipedia.summary(suggestions[0], sentences=2)
            return f"I found multiple interesting topics about {query}. Could you be more specific?"
