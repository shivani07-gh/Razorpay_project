from app.ai.context import InvestigationContext, build_root_cause_input
from app.ai.root_cause import RootCauseResult, investigate_root_cause


def investigate(context: InvestigationContext) -> RootCauseResult:
    """
    Run the root cause investigation pipeline.
    """

    root_cause_input = build_root_cause_input(context)

    return investigate_root_cause(root_cause_input)