"""
Wake word engine for Luna.

This module isolates wake-word detection from the AI core.
The implementation uses a lightweight placeholder interface so the
engine can later be connected to openWakeWord/Porcupine models.
"""


class WakeEngine:

    def __init__(self, wake_word="hey luna"):
        self.wake_word = wake_word.lower()

    def detect(self, text):
        if not text:
            return False

        return self.wake_word in text.lower()
