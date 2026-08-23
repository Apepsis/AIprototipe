"""
Wake word detector.
Phase 1 implementation: detects activation phrase locally.
Future: integrate openWakeWord/Picovoice model.
"""

WAKE_WORD = "hey luna"


def detect_wake_word(text):
    if not text:
        return False

    return WAKE_WORD in text.lower()
