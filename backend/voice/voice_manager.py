"""
Voice Manager
Coordinates all voice components.
"""

from backend.voice.listener import Listener
from backend.voice.recognizer import Recognizer
from backend.voice.speaker import Speaker
from backend.voice.wakeword import WakeWord


class VoiceManager:

    def __init__(self):
        self.listener = Listener()
        self.recognizer = Recognizer()
        self.speaker = Speaker()
        self.wakeword = WakeWord()

    def initialize(self):
        print("[VOICE] Voice Manager Initialized")

    def speak(self, text: str):
        self.speaker.speak(text)

    def listen(self):
        return self.listener.listen()

    def recognize(self, audio):
        return self.recognizer.recognize(audio)