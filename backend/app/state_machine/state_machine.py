from app.state_machine.states import PaymentState
from app.state_machine.transitions import VALID_TRANSITIONS

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