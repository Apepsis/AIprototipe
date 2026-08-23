"""
Text to speech abstraction for Luna.

Prepared for Piper TTS integration.
"""


def speak(text):
    """Speak Luna response.

    Current version keeps a simple interface.
    Replace internals with Piper TTS for offline voice output.
    """

    print("🔊 Luna:", text)
