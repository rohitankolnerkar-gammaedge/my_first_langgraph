from app.helper.check_constraint import check_constraint
from app.llm import get_llm
from app.prompts.prompt_summary import get_summary_prompt
from langchain_core.output_parsers import StrOutputParser
from app.helper.guardrails import output_guardrails
out=output_guardrails()
async def join_node(state):
    merged_dict = {}
    merged_text = ""
    needs_retry = []

    
    for ans_dict in state["answers"]:
        merged_dict.update(ans_dict)

        for question, answer in ans_dict.items():
            if check_constraint(answer):
                merged_text += f"{question}\n{answer}\n\n"
            else:
                needs_retry.append(question)

    
    if needs_retry:
        return {
            "merged_answers": merged_dict,
            "needs_retry": needs_retry
        }

    
    llm = get_llm(max_tokens=1024)
    prompt =get_summary_prompt()   
    chain = prompt | llm | StrOutputParser()

    print("\n\n Generating Final Summary Report:\n")

    final_report = ""

    async for chunk in chain.astream({"content": merged_text}):
        print(chunk, end="", flush=True)
        final_report += chunk
    if not  (out.validate_length(final_report) and out.validate_structure(final_report)):
        print("summary not fulfill condition")
    else:
        print("\n\n Final Summary Completed.\n")

    return {
        "merged_answers": merged_dict,
        "final_report": final_report,
        "needs_retry": []
    }