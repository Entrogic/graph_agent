from langgraph.graph import StateGraph, START, END

from langgraph_agent import graph
from .state import AgentState
from .nodes import assistant_agent


def build_graph():
    
    graph = StateGraph(AgentState)

    graph.add_node("assistant", assistant_agent)

    graph.add_edge(START, "assistant")
    graph.add_edge("assistant", END)

    return graph.compile()
