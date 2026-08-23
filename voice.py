from faster_whisper import WhisperModel
import sounddevice as sd
from scipy.io.wavfile import write


model = WhisperModel(
    "small",
    device="cuda",
    compute_type="float16"
)


def listen():

    filename = "input.wav"
    duration = 5
    samplerate = 16000

    print("🎤 Escuchando...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1
    )

    sd.wait()

    write(
        filename,
        samplerate,
        audio
    )

    segments, info = model.transcribe(filename)

    text = ""

    for segment in segments:
        text += segment.text

    return text