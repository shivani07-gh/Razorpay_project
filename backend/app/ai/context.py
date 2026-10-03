from dataclasses import dataclass
from app.ai.root_cause import RootCauseInput

@dataclass
class InvestigationContext:
    payment_id: str
    razorpay_state: str
    merchant_state: str
    order_status: str
    fulfillment_status: str
    timeline: list[str]
    inconsistencies: list[str]

def build_root_cause_input(context: InvestigationContext) -> RootCauseInput:
    return RootCauseInput(
        payment_id=context.payment_id,
        razorpay_state=context.razorpay_state,
        merchant_state=context.merchant_state,
        order_status=context.order_status,
        fulfillment_status=context.fulfillment_status,
        inconsistencies=context.inconsistencies,
    )    