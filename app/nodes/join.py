from app.helper.check_constraint import check_constraint
from app.graph.state import ReportState
def join_node(state:ReportState):
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

    return {
        "merged_answers": merged_dict,
        "final_report": merged_text,
        "needs_retry": needs_retry
    }