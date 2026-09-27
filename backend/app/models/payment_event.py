from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class PaymentEvent(Base):
    __tablename__ = "payment_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True, 
        autoincrement=True,
    )

    event_id: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )#Unique webhook/event ID

    payment_id: Mapped[str] = mapped_column(
        String(100),
        ForeignKey("payments.payment_id"),
        nullable=False,
        index=True,
    )#Which payment this event belongs to

    event_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )#Type of the event, e.g., payment.captured, payment.failed, etc.

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )#Razorpay / merchant / order / fulfillment

    event_timestamp: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )#When event actually happened

    processing_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )#received / processing / processed / failed

    payload: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )#raw event data

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )#when it was stored in our DB