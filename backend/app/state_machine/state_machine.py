from app.state_machine.states import PaymentState
from app.state_machine.transitions import VALID_TRANSITIONS
from app.state_machine.event_mapper import map_event_to_state

class PaymentStateMachine:

    def __init__(self, initial_state: PaymentState = PaymentState.CREATED):
        self.current_state = initial_state

    def can_transition(self, new_state: PaymentState) -> bool:
        return new_state in VALID_TRANSITIONS[self.current_state]


    def transition(self, new_state: PaymentState) -> bool:
        if not self.can_transition(new_state):
            return False
        self.current_state = new_state
        return True

    def process_event(self, event_type: str) -> bool:
        next_state = map_event_to_state(event_type)
        if next_state is None:
            return False

        return self.transition(next_state)