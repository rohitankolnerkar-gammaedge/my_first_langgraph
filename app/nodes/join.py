from app.helper.check_constraint import check_constraint
def join_node(state):
    merged_dict = {}
    merged_text = ""
    needs_retry=[]
    for d in state["answers"]:
        merged_dict.update(d)
        for q, a in d.items():
            if not check_constraint(a):
                needs_retry.append(a)
            merged_text += f"{q}\n{a}\n\n"

    return {
        "merged_answers": merged_dict,
        "final_report": merged_text,
        "needs_retry": needs_retry
    }