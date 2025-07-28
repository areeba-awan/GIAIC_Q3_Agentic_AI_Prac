# class 06
# GIthub : https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/14_tracing

# official docs
# https://openai.github.io/openai-agents-python/tracing/

# TRACING DASHBOARD LINK:  https://platform.openai.com/traces

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

# Note : Tracing Agent ko Check krne k liye open ai ki api key buy krni paregi 
# uske bina ye logs me record ni hoga iska kaam