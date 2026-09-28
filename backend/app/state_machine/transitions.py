from app.state_machine.states import PaymentState

VALID_TRANSITIONS = {
    PaymentState.CREATED: {
        PaymentState.AUTHORIZED,
        PaymentState.FAILED,
    },
    PaymentState.AUTHORIZED: {
        PaymentState.CAPTURED,
        PaymentState.FAILED,
    },
    PaymentState.CAPTURED: set(),
    PaymentState.FAILED: set(),
    
}