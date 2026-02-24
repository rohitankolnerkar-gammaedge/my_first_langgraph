from app.llm import get_llm
from app.graph.state import ReportState
from langchain_core.output_parsers import StrOutputParser
from app.prompts.prompt_agent import get_agent_prompt

llm=get_llm()
def agent_b(state:ReportState):
    question=state['sub_questions'][1]
    prompt = get_agent_prompt()
    chain=prompt | llm| StrOutputParser()
    response=chain.invoke({'question':question})
    

    return {
        "answers": [
            {question: response}
        ]
    }

