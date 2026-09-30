from app.state_machine.states import PaymentState


EVENT_TO_STATE = {
    "payment.created": PaymentState.CREATED,
    "payment.authorized": PaymentState.AUTHORIZED,
    "payment.captured": PaymentState.CAPTURED,
    "payment.failed": PaymentState.FAILED,
}


def map_event_to_state(event_type: str) -> PaymentState | None:
    return EVENT_TO_STATE.get(event_type)