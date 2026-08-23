# Luna Voice System

## Architecture

Microphone -> Wake Word -> Recorder -> Whisper -> Agent -> Piper TTS

## Local setup

Install:

```
pip install -r requirements_voice.txt
```

Download locally:

- OpenWakeWord model
- Piper voice model

Place models inside:

```
voice/models/
```

Run:

```
python main.py --voice
```
