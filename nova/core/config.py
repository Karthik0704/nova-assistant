import yaml
from pathlib import Path
from typing import Dict, Any

class NovaConfig:
    def __init__(self):
        self.config_path = Path("config/settings.yaml")
        self.settings = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            return self._create_default_config()
        
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def _create_default_config(self) -> Dict[str, Any]:
        default_config = {
            'assistant': {
                'name': 'NOVA',
                'wake_word': 'hey nova',
                'language': 'en-US'
            },
            'speech': {
                'recognition': {
                    'engine': 'google',
                    'timeout': 5,
                    'energy_threshold': 4000
                },
                'synthesis': {
                    'engine': 'pyttsx3',
                    'voice_id': None,
                    'rate': 150
                }
            },
            'system': {
                'timezone': 'UTC'
            },
            'apis': {
                'weather_key': 'YOUR_API_KEY'
            }
        }
        
        self.config_path.parent.mkdir(exist_ok=True)
        with open(self.config_path, 'w') as f:
            yaml.dump(default_config, f)
        
        return default_config

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self.settings
        
        try:
            for k in keys:
                if isinstance(value, dict):
                    value = value.get(k)
                else:
                    return default
                if value is None:
                    return default
            return value
        except (KeyError, AttributeError):
            return default
