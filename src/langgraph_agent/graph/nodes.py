from .state import AgentState
from ..llm.model import get_model

model = get_model()


def assistant_agent(state: AgentState):

    response = model.invoke(state["messages"])

    return {
        "messages": [response]
    }