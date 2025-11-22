from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END
from app.core.tools.calculator import calculator
from app.core.tools.weather_man import weather_repoter
from app.core.llm_models import gemini_model as llm

# from app.core import tools,llm_models
# from tools import calculator
# from llm_models import gemini_model as llm

def initial_state(message: str):
    return {
        "messages": [HumanMessage(content=message)]
    }

def build_agent():
    tools = [calculator,weather_repoter]
    model = llm.get_model()
    system_prompt = """
    You are a clean REACT agent.

    Rules:
    - Think step-by-step before answering.
    - Use tools when needed.
    - Follow the tool schema exactly.
    - Final output should be clean and clear.
    OUTPUT FORMATE 
    **status - indicates the weather the task was completed
    **reasults - tool output in a clean and clear way
    **tools_called - show all the tools used
    """
    agent = create_react_agent(
        model=model,
        tools=tools,
        prompt=system_prompt
    )
    
    return agent

def build_graph():
    graph = StateGraph(dict)          # State = dict
    react_agent = build_agent() # a runnable graph node

    # Node name: "react_agent"
    graph.add_node("react_agent", react_agent)

    # Trigger always goes to the agent node
    graph.set_entry_point("react_agent")

    # Agent node completes → workflow END
    graph.add_edge("react_agent", END)

    return graph.compile()
