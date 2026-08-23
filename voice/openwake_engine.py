"""OpenWakeWord engine for Luna.

Detects the wake phrase before activating Whisper.
"""

import openwakeword
from openwakeword.model import Model


class WakeEngine:
    def __init__(self, wake_phrase="hey luna"):
        self.wake_phrase = wake_phrase.lower()
        self.model = Model()

    def detect(self, audio_frame):
        predictions = self.model.predict(audio_frame)

        for name, score in predictions.items():
            if self.wake_phrase in name.lower() and score > 0.5:
                return True

        return False
