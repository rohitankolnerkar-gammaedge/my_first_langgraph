from app.llm import get_llm
from app.graph.state import ReportState
from langchain_core.output_parsers import StrOutputParser
from app.prompts.prompt_agent import get_agent_prompt
from app.helper.streaming import StreamBuffer
llm=get_llm()
stream_callback=StreamBuffer()
def agent_c(state:ReportState):
    question=state['sub_questions'][2]
    prompt = get_agent_prompt()
    chain=prompt | llm| StrOutputParser()
   
    chain.invoke(
    {'question': question},
    callbacks=[stream_callback]  )
    full_answer = stream_callback.get_buffered_answer()
    
    return {
            "answers": [{question: full_answer}],
            "question_agent_map":{question:agent_c}
        }
