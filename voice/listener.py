"""
Voice controller.
Workflow:
1. Wait for wake word.
2. Activate recording.
3. Send audio to speech recognition.
"""

from .wake_word import detect_wake_word
from .speech_to_text import SpeechRecognizer


class VoiceListener:

    def __init__(self):
        self.recognizer = SpeechRecognizer()

    def process_activation(self, phrase):

        if detect_wake_word(phrase):
            return True

        return False

    def transcribe_command(self, audio_file):
        return self.recognizer.transcribe(audio_file)
