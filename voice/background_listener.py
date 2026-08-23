"""
Luna resident listener.

Flow:
Microphone -> Wake word -> Speech recognition -> Agent -> TTS
"""

import time

from voice.wake_word import detect_wake_word
from voice.listener import listen_command
from voice.text_to_speech import speak


class LunaListener:

    def __init__(self, agent_callback):
        self.agent_callback = agent_callback
        self.running = False
        self.wake_phrase = "hey luna"

    def start(self):
        self.running = True
        print("🌙 Luna esperando activación...")

        while self.running:

            if detect_wake_word(self.wake_phrase):
                print("🎤 Luna activada")

                command = listen_command()

                if command:
                    response = self.agent_callback(command)
                    speak(response)

            time.sleep(0.1)

    def stop(self):
        self.running = False
