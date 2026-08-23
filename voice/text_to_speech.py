import subprocess


def speak(text):
    """Basic TTS placeholder.

    Designed to be replaced by Piper TTS or another offline engine.
    """

    print("🔊 Luna:", text)

    # Future integration:
    # piper --model luna.onnx --output_file voice.wav
