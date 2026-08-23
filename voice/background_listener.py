from voice.wake_word import detect_wake_word
from voice.listener import listen_command


class LunaListener:
    """Always-on listener controller.

    The lightweight wake word stage runs first.
    Full transcription is only activated after activation.
    """

    def __init__(self, wake_word="hey luna"):
        self.wake_word = wake_word

    def start(self, callback):

        print("🌙 Luna esperando activación...")

        while True:

            activated = detect_wake_word(self.wake_word)

            if activated:
                print("Luna activada")

                command = listen_command()

                if command:
                    callback(command)
