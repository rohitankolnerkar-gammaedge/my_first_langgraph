from typing import TypedDict, List, Dict, Optional,Annotated,Callable
import operator


class ReportState(TypedDict):
    
    topic: str
    sub_questions: List[str]
    question_agent_map: Annotated[
    Dict[str, Callable[['ReportState'], 'ReportState']],
    operator.or_
]
    answers: Annotated[List[Dict[str, str]], operator.add]
    retry_counts: Dict[str, int]
    needs_retry: List[str]
    final_report: Optional[str]