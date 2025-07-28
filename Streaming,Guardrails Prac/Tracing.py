
import os
from agents import Agent, Runner, function_tool
from dotenv import load_dotenv
_: bool = load_dotenv()
from my_config import config 

@function_tool
async def fetch_weather (city : str)-> str:
    return f"The weather in {city } is sunny"


simple_agent = Agent(
    name = "Tracing Agent",
    instructions = "You are helpful assistant",
    tools = [fetch_weather]
)

result = Runner.run_sync(simple_agent, "What is the weather in karachi?",run_config = config)
print("result >>>>> ",result.final_output)
