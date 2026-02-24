# app/nodes/retry.py
from app.graph.state import ReportState

def retry(state: ReportState):
    if not state.get("needs_retry"):
        return state

    for failed_question in state["needs_retry"]:
       
        state["retry_counts"][failed_question] = state["retry_counts"].get(failed_question, 0) + 1

        
        if state["retry_counts"][failed_question] > 2:
            print(f"Skipping {failed_question}, retry limit exceeded")
            continue

       
        agent = state["question_agent_map"][failed_question]
        corrected_ans = agent(state)

      
        for i, ans_dict in enumerate(state["answers"]):
            if failed_question in ans_dict:
                state["answers"][i] = corrected_ans["answers"][0]

    state["needs_retry"].clear()
    return state