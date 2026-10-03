from app.state_machine.states import PaymentState


def detect_inconsistency(
    razorpay_state: PaymentState,
    merchant_state: PaymentState,
    order_status: str,
    fulfillment_status: str,
) -> dict:
    """
    Compare payment state across different systems.
    """

    inconsistencies = []

    if razorpay_state != merchant_state:
        inconsistencies.append("RAZORPAY_MERCHANT_MISMATCH")

    if razorpay_state == PaymentState.CAPTURED and order_status != "PAID":
        inconsistencies.append("CAPTURED_BUT_ORDER_NOT_PAID")

    if razorpay_state == PaymentState.CAPTURED and fulfillment_status != "STARTED":
        inconsistencies.append("CAPTURED_BUT_FULFILLMENT_NOT_STARTED")
        
    if not inconsistencies:
         severity = "NONE"
    elif any(
                item in inconsistencies
                for item in [
            "RAZORPAY_MERCHANT_MISMATCH",
            "CAPTURED_BUT_ORDER_NOT_PAID",
        ]
        ):
            severity = "CRITICAL"
    else:
        severity = "HIGH"

    return {
        "is_inconsistent": len(inconsistencies) > 0,
        "severity": severity,
        "inconsistencies": inconsistencies,
    }