from app.graph.state import ReportState


def retry(state: ReportState):


    if not state.get("needs_retry"):
        return {}

    updated_retry_counts = dict(state.get("retry_counts", {}))
    updated_answers = list(state.get("answers", []))

    remaining_retry_questions = []

    for failed_question in state["needs_retry"]:

       
        current_count = updated_retry_counts.get(failed_question, 0) + 1
        updated_retry_counts[failed_question] = current_count

        
        if current_count > 2:
            print(f"Skipping {failed_question}, retry limit exceeded")
            continue

        
        agent = state["question_agent_map"].get(failed_question)
        if not agent:
            continue

        
        corrected_ans = agent(state)

        
        if corrected_ans and corrected_ans.get("answers"):
            new_answer_dict = corrected_ans["answers"][0]

            for i, ans_dict in enumerate(updated_answers):
                if failed_question in ans_dict:
                    updated_answers[i] = new_answer_dict
                    break

        
        remaining_retry_questions.append(failed_question)

    return {
        "answers": updated_answers,
        "retry_counts": updated_retry_counts,
        "needs_retry": remaining_retry_questions,
    }