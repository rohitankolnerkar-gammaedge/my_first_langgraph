from app.graph.builder import build_graph

def main():
    graph = build_graph()

    topic = input("Enter your research topic: ")

    initial_state = {
        "topic": topic,
        "sub_questions": [],
        "answers": {},
        "retry_counts": {},
        "needs_retry": [],
        "final_report": None,
    }

    result = graph.invoke(initial_state)

    print("\nFinal State:")
    print(result)


if __name__ == "__main__":
    main()