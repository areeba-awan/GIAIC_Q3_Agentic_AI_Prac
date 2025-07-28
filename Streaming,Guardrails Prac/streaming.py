# STREAMING : 

# Streaming lets you subscribe to updates of the agent run as it proceeds.
# This can be useful for showing the end-user progress updates and partial responses.

# METHOD 
# Runner.run_streamed()

# EVENT IN STREAMING : => An action perform by an Agent (koi b action perform hona)

# THERE ARE 3 TYPES OF EVENTS IN STREAMING 

# 1 RAW RESPONSE EVENT 
# 2 RUN ITEM STREM EVENT :
# 3 AGENT UPDATED STREAM EVENT :

# SYNTAX 1 (RAW RESPONSE EVENT)

import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner
from  my_config  import config

async def main():
    agent = Agent(
        name="Joker",
        instructions="You are a helpful assistant.",
    )

    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.",run_config = config)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance (event.data,ResponseTextDeltaEvent):
        #  print ("\n[Event Type]", event)
        #  print(event)
        #  print("event>>>>>>",event) 
          print(event.data.delta, end = "",flush=True) # flush means immediately response

if __name__ == "__main__":
    asyncio.run(main())

# EXAMPLE 2 

# Type of Event (Run item Stream Event and Agent Events)

# SYNTAX 


import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner,function_tool, ItemHelpers
from  my_config  import config
import random


@function_tool
def how_many_jokes() -> int:
    # return random.randint(1, 20)
      return 20

async def main():
        agent = Agent(
        name="Joker",
        instructions="First call the `how_many_jokes` tool, then tell that many jokes.",
        tools=[how_many_jokes],
        )

        result = Runner.run_streamed(agent, input="Please Call the tool and tell me jokes.",run_config= config)
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance (event.data,ResponseTextDeltaEvent): # 1st event
                continue
            elif event.type == "agent_updated_stream_event": # -> 2nd Event
                print(f"Agent updated :, {event.new_agent.name}")
                continue
            # elif event.type == "run_item_stream_event":   # -> 3rd Event
            #     print("event.item",event.item.type)
            #     if event.item.type == "tool_call_item":
            #      print("-- Tool was called")
            #     elif event.item.type == "tool_call_output_item":
            #         print(f"-- Tool output: {event.item.output}")
            #     elif event.item.type == "message_output_item":
            #         print(f"-- Message output:\n {ItemHelpers.text_message_output(event.item)}")


if __name__ == "__main__":
    asyncio.run(main())
