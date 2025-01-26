import re
from typing import Tuple

class CommandProcessor:
    def __init__(self):
        self.patterns = {
            'weather': [
                r'weather (?:in|at|for)? (.+)',
                r'what\'s the weather (?:like )?(?:in|at|for)? (.+)',
                r'how\'s the weather (?:in|at|for)? (.+)'
            ],
            'time': [
                r'what(?:\'s|\s+is) the time',
                r'current time',
                r'time now'
            ],
            'date': [
                r'what(?:\'s|\s+is) (?:the )?date',
                r'what day is it',
                r'today\'s date'
            ]
        }

    def process(self, text: str) -> Tuple[str, dict]:
        text = text.lower().strip()
        
        for intent, patterns in self.patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text)
                if match:
                    params = match.groups() if match.groups() else ()
                    return intent, {'params': params}
        
        return 'unknown', {}
