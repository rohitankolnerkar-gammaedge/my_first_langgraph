from app.llm import get_llm
from app.graph.state import ReportState
from langchain_core.output_parsers import StrOutputParser
from app.prompts.prompt_agent import get_agent_prompt

llm = get_llm()

async def agent_b(state: ReportState):
    question = state['sub_questions'][1]
    prompt = get_agent_prompt()
    chain = prompt | llm | StrOutputParser()

    print("\n\n Agent B generating answer:\n")
    print(f"\n{question}\n")

    response = ""

    async for chunk in chain.astream({'question': question}):
        print(chunk, end="", flush=True)  
        response += chunk

    print("\n\n Agent B finished.\n")

    return {
        "answers": [{question: response}],
        "question_agent_map": {question: agent_b}
    }