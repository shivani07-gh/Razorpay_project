from datetime import datetime
from app.models.base import Base
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    payment_id: Mapped[str] = mapped_column(
        String(100),
        unique=True, 
        index=True,
        nullable=False,
    )

    order_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    amount: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    razorpay_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    merchant_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    order_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    fulfillment_status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )