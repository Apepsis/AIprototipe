"""
Resident Luna assistant controller.

Flow:
Microphone -> Wake Word -> Recorder -> Whisper -> Agent -> TTS
"""


class LunaService:

    def __init__(self, agent=None, speech=None, tts=None, wake_engine=None):
        self.agent = agent
        self.speech = speech
        self.tts = tts
        self.wake_engine = wake_engine
        self.running = False

    def start(self):
        self.running = True
        print("Luna listening mode activated")
        print("Waiting for: Hey Luna")

    def handle_command(self, text):
        if not text:
            return None

        if self.agent:
            response = self.agent.run(text)
        else:
            response = text

        if self.tts:
            self.tts.speak(response)

        return response

    def stop(self):
        self.running = False
