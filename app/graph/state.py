from typing import TypedDict, List, Dict, Optional,Annotated
import operator


class ReportState(TypedDict):
    
    topic: str
    sub_questions: List[str]
    question_agent_map=Dict[str,str]
    answers: Annotated[List[Dict[str, str]], operator.add]
    retry_counts: Dict[str, int]
    needs_retry: List[str]
    final_report: Optional[str]