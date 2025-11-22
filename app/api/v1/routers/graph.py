from fastapi import APIRouter
from app.core import types
from app.core.graph_engine.graph_builder import initial_state, build_agent, build_graph

router = APIRouter(prefix="/graph", tags=["AgentChat"])

graph = build_graph()

@router.post("/ask")
def chat(usermessage:types.Usermessage):
    state=initial_state(usermessage.message)
    result_state = graph.invoke(state)
    final_msg = result_state["messages"][-1].content
    
    return {"result" : final_msg}