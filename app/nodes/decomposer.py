from typing import Dict
from langchain_core.prompts import ChatPromptTemplate
from app.llm import get_llm
from app.graph.state import ReportState
from langchain_core.output_parsers import StrOutputParser
from app.prompts.prompt_decomposer import get_decomposer_prompt

llm = get_llm()

def decomposer_node(state: ReportState) -> Dict:
    topic = state["topic"]

    prompt = get_decomposer_prompt()
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"topic": topic})
    lines = str(response).strip().split("\n")
    sub_questions = [line.split(". ", 1)[-1].strip() for line in lines if line.strip()
    ]
    retry_counts = {q: 0 for q in sub_questions}

    return {
        "sub_questions": sub_questions,
        "retry_counts": retry_counts
    }
       