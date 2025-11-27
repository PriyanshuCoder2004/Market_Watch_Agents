import json
import os
from datetime import datetime

MEMORY_FILE = "market_memory_bank.json"

class MemoryBank:
    def __init__(self):
        self._load_memory()

    def _load_memory(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def get_last_entry(self, key: str):
        """Retrieves the last known state for a company."""
        return self.data.get(key)

    def save_entry(self, key: str, value: dict):
        """Updates the memory bank."""
        record = {
            "timestamp": datetime.now().isoformat(),
            "data": value
        }
        self.data[key] = record
        
        with open(MEMORY_FILE, 'w') as f:
            json.dump(self.data, f, indent=4)