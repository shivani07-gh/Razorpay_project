from app.state_machine.states import PaymentState
from app.state_machine.state_machine import PaymentStateMachine
from app.state_machine.timeline import build_timeline


def reconstruct_state(events):
    """
    Reconstruct payment state and record invalid events.
    """

    timeline = build_timeline(events)

    state_machine = PaymentStateMachine()
    invalid_events = []

    for event in timeline:
        success = state_machine.process_event(event.event_type)

        if not success:
            invalid_events.append(event.event_type)

    return {
        "final_state": state_machine.current_state,
        "invalid_events": invalid_events,
    }