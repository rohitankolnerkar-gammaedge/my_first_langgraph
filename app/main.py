from app.graph.builder import build_graph
from pprint import pprint  

def main():
    graph = build_graph()

    topic = input("Enter your research topic: ")

    initial_state = {
        "topic": topic,
        "sub_questions": [],
        "answers": [],
        "retry_counts": {},
        "needs_retry": [],
        "final_report": None,
    }

    result = graph.invoke(initial_state)

  
    print("\n===== FINAL STATE =====\n")
    pprint(result)

    print("\n===== FINAL REPORT =====\n")
    if result.get("final_report"):
        print(result["final_report"])
    else:
        print("No final report generated yet.")


if __name__ == "__main__":
    main()