from datetime import datetime
import pytz  # Make sure pytz is installed with: pip install pytz

class TimeManager:
    def __init__(self, config):
        # Get timezone from config or default to India
        self.timezone = pytz.timezone(config.get('system.timezone', 'Asia/Kolkata'))
        
    def get_time(self):
        current = datetime.now(self.timezone)
        time_str = current.strftime("%I:%M %p")
        return f"The current time is {time_str}"
        
    def get_date(self):
        current = datetime.now(self.timezone)
        return f"Today is {current.strftime('%A, %B %d, %Y')}"
