# Já a classe narrativa precisa ter um atributo que indique a fase atual e
# um método que controle quando irá mudar.
# É preciso tb ter um método que rode apenas os eventos com a flag correspondente à fase atual.

# March 30th, 2025 - HEAVY WORK IN PROGRESS...
import event

from chapter_phase_options import ChapterPhaseOptions

class WrongChapterPhase(Exception):
    pass

class Chapter:
    def __init__(self, current_phase):
        self.current_phase = current_phase

    def phase_change(self, new_phase):
        self.current_phase = new_phase

    def call_event(self, event_param=event.SingleEvent()):
        event = event_param
        if event.chapter_phase != self.current_phase:
            raise WrongChapterPhase("Event's and Chapter's phases don't match.")


# TESTS
chapter_1 = Chapter(current_phase=ChapterPhaseOptions.INTRODUCTION)