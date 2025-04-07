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
        if not isinstance(current_phase, ChapterPhaseOptions):
            raise ValueError(f"Invalid chapter phase: {current_phase}")  # Raises an error if current_phase is not in ChapterPhaseOptions
        self.current_phase = current_phase

    def phase_change(self, new_phase):
        self.current_phase = new_phase

    def call_event(self, event_param=None):
        if event_param is None:
            event_param = event.SingleEvent()
        if event_param.chapter_phase != self.current_phase:
            raise WrongChapterPhase("Event's and Chapter's phases don't match.")

        


# TESTS
chapter_1 = Chapter(current_phase=ChapterPhaseOptions.INTRODUCTION)
print(chapter_1.current_phase)