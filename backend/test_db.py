from datetime import datetime

from app.core.database import SessionLocal
from app.models.payment import Payment
from app.models.payment_event import PaymentEvent


db = SessionLocal()

try:
    payment = Payment(
        payment_id="pay_test_001",
        order_id="order_test_001",
        amount=50000,
        razorpay_status="CAPTURED",
        merchant_status="FAILED",
        order_status="UNPAID",
        fulfillment_status="NOT_STARTED",
    )

    db.add(payment)
    db.commit()
    db.refresh(payment)

    print("Payment created:", payment.payment_id)

    event = PaymentEvent(
        event_id="evt_test_001",
        payment_id=payment.payment_id,
        event_type="payment.captured",
        source="razorpay",
        event_timestamp=datetime.utcnow(),
        processing_status="PROCESSED",
        payload='{"status": "captured"}',
    )

    db.add(event)
    db.commit()
    db.refresh(event)

    print("Event created:", event.event_id)

finally:
    db.close()