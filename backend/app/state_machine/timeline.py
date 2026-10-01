from datetime import datetime
from app.models.payment_event import PaymentEvent

def build_timeline(events: list[PaymentEvent]) -> list[PaymentEvent]:
    """
    sort payment events by their timestamp.
    """
    return sorted(
        events,
        key = lambda event: event.event_timestamp
    )
    