"""
Speech recognition layer.
Uses faster-whisper only when voice mode is activated.
"""

from faster_whisper import WhisperModel


class SpeechRecognizer:

    def __init__(self):
        self.model = WhisperModel(
            "small",
            device="cuda",
            compute_type="float16"
        )

    def transcribe(self, audio_file):

        segments, info = self.model.transcribe(audio_file)

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()
