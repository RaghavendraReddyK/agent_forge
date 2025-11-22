from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    Evaluate a simple math expression and return the result.
    Use this tool for arithmetic like: 2+2, 10*4, 50/5, etc.
    """
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"
    