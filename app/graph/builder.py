from langgraph.graph import StateGraph, END

from app.graph.state import ReportState
from app.nodes.decomposer import decomposer_node
from app.nodes.agent_a import agent_a
from app.nodes.agent_b import agent_b
from app.nodes.agent_c import agent_c
from app.nodes.join import join_node
from app.nodes.retry import retry
def build_graph():
    graph = StateGraph(ReportState)
    graph.add_node("decomposer", decomposer_node)
    graph.add_node("agent_a", agent_a)
    graph.add_node("agent_b", agent_b)
    graph.add_node("agent_c", agent_c)
    graph.add_node('retry',retry)
    graph.add_node('join',join_node)


    graph.set_entry_point("decomposer") 


    graph.add_edge("decomposer", "agent_a")
    graph.add_edge("decomposer", "agent_b")
    graph.add_edge("decomposer", "agent_c")
    graph.add_edge("agent_a", 'join')
    graph.add_edge("agent_b", 'join')
    graph.add_edge("agent_c", 'join')
    graph.add_edge("join", "retry")
    graph.add_edge("retry", "join")
    graph.add_edge("join", END)


    return graph.compile()