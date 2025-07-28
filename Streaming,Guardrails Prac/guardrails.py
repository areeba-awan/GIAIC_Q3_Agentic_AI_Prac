# CLASS 06 

# GITHUB : STEP 13 https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first/13_guardrails

# OFFICAL DOCS : https://openai.github.io/openai-agents-python/guardrails/

# GUARDRAILS :

# THERE ARE 2 TYPES OF GUARDRAILS

# 1 INPUT GUARDRAILS
# 2 OUTPUT GUARDRAILS

# EXAMPLE (INPUT GUARDRAILS)

from agents import Agent, Runner, input_guardrail, RunContextWrapper, TResponseInputItem, GuardrailFunctionOutput
from my_config import config


@input_guardrail
async def math_guardrail(
    wrapper : RunContextWrapper[None], agent : Agent , input:str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    
    #user_type = wrapper.context.user_type
    print("input >>>>>" , input)
    user_type = "user"
    guardrail_instance = GuardrailFunctionOutput(
        output_info = "Guardrail is failed due to user type",
        tripwire_triggered = False 
        #user_type != "admin" # user_type != admin True , False
    )
    return guardrail_instance


simple_agent = Agent(
    name = "Simple Agent",
    instructions= "you are helpful assistant",
    input_guardrails=[math_guardrail], # Parameter of Input Guardrails
)

result = Runner.run_sync(simple_agent , "Hi how are you?" , run_config= config)

#print("Guardrail output_info:", result.input_guardrail_results)  # Guardrail ka result print karein
print("\n 🎀 Final output:", result.final_output)
#print(result.final_output)


# Note : To call the input guardrail function u must add decorator @input_guardrail in the starting of function

# HOMEWORK : OUTPUT GUARDRAILS