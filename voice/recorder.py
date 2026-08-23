import sounddevice as sd
from scipy.io.wavfile import write


class AudioRecorder:
    def __init__(self, filename="input.wav", seconds=5, rate=16000):
        self.filename = filename
        self.seconds = seconds
        self.rate = rate

    def record(self):
        print("🎤 Escuchando comando...")
        audio = sd.rec(
            int(self.seconds * self.rate),
            samplerate=self.rate,
            channels=1
        )
        sd.wait()
        write(self.filename, self.rate, audio)
        return self.filename
