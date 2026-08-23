import sounddevice as sd


def record_audio(duration=5, samplerate=16000):
    print("🎤 Grabando comando...")

    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1
    )

    sd.wait()

    return audio
