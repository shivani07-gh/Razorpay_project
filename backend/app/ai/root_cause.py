from dataclasses import dataclass

@dataclass
class RootCauseInput:
    payment_id: str
    razorpay_state: str
    merchant_state: str
    order_status: str
    fulfillment_status: str
    inconsistencies: list[str]

@dataclass
class RootCauseResult:
    root_cause: str
    evidence: list[str]
    confidence: float  

def investigate_root_cause(data: RootCauseInput) -> RootCauseResult:
    """
    Investigate the likely root cause using deterministic evidence.
    """

    if (
        "RAZORPAY_MERCHANT_MISMATCH" in data.inconsistencies
        and data.razorpay_state == "CAPTURED"
        and data.merchant_state == "FAILED"
    ):
        return RootCauseResult(
            root_cause="Merchant webhook processing failure",
            evidence=[
                "Razorpay state is CAPTURED",
                "Merchant state is FAILED",
            ],
            confidence=0.95,
        )

    if "CAPTURED_BUT_ORDER_NOT_PAID" in data.inconsistencies:
        return RootCauseResult(
            root_cause="Order system was not updated after payment capture",
            evidence=[
                "Razorpay state is CAPTURED",
                "Order status is UNPAID",
            ],
            confidence=0.90,
        )

    return RootCauseResult(
        root_cause="Unknown",
        evidence=data.inconsistencies,
        confidence=0.50,
    )
