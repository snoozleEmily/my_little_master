# Já a classe narrativa precisa ter um atributo que indique a fase atual e
# um método que controle quando irá mudar.
# É preciso tb ter um método que rode apenas os eventos com a flag correspondente à fase atual.

import event
import exceptions



class Chapter:
    def __init__(self, current_phase):
        self.current_phase = current_phase

    def phase_change(self, new_phase):
        self.current_phase = new_phase

    def call_event(self, event_param=None):
        if event_param is None:
            event_param = event.SingleEvent()
            