from .state import AgentState
from ..llm.model import get_model

model = get_model()


def assistant_agent(state: AgentState) -> AgentState:

    response = model.invoke(state["message"])

    return {"message": state["message"], "response": response}
