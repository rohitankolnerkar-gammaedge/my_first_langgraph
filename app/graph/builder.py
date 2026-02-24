from langgraph.graph import StateGraph, END

from app.graph.state import ReportState
from app.nodes.decomposer import decomposer_node
from app.nodes.agent_a import agent_a


def build_graph():
    graph = StateGraph(ReportState)
    graph.add_node("decomposer", decomposer_node)
    graph.add_node("agent_a", agent_a)
    graph.set_entry_point("decomposer") 
    graph.add_edge("decomposer", "agent_a")
    graph.add_edge("agent_a", END)
    return graph.compile()