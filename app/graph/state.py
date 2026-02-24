from typing import TypedDict, List, Dict, Optional


class ReportState(TypedDict):
    
    topic: str
    sub_questions: List[str]
    answers: Dict[str, str]
    retry_counts: Dict[str, int]
    needs_retry: List[str]
    final_report: Optional[str]