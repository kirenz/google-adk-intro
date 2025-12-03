from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="You answer questions.",
    instruction="You are a helpful assistant that can search the web and provide information.",
    tools=[google_search],
)