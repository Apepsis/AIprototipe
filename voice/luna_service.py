"""
Resident Luna assistant controller.

Flow:
Microphone -> Wake Engine -> Speech Recognition -> Agent -> TTS
"""

from voice.wake_engine import WakeEngine


class LunaService:

    def __init__(self, agent=None):
        self.agent = agent
        self.wake_engine = WakeEngine("hey luna")
        self.running = False

    def start(self):
        self.running = True
        print("Luna listening mode activated")

    def stop(self):
        self.running = False

    def process_text(self, text):
        if self.wake_engine.detect(text):
            return "Luna activated"

        return None

    def ask_agent(self, question):
        if self.agent:
            return self.agent.run(question)

        return None
