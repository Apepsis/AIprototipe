import subprocess


class PiperTTS:
    def __init__(self, voice_model="voices/en_US-lessac-medium.onnx"):
        self.voice_model = voice_model

    def speak(self, text):
        subprocess.run([
            "piper",
            "--model",
            self.voice_model,
            "--output_file",
            "response.wav"
        ], input=text.encode())
