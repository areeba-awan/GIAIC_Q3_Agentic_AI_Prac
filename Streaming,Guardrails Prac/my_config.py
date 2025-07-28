from agents import OpenAIChatCompletionsModel, AsyncOpenAI, RunConfig
from dotenv import load_dotenv # for api or env file
import os
_: bool = load_dotenv()

# Get the Gemini API key from environment variable
GEMINI_API_KEY = os.environ.get("GOOGLE_API_KEY")

client = AsyncOpenAI(  # client or external_client works same
    api_key = GEMINI_API_KEY,
    base_url = 'https://generativelanguage.googleapis.com/v1beta/openai/',
)
model = OpenAIChatCompletionsModel(       # model or external_model are same
    model = "gemini-2.5-flash",
    openai_client = client,
)

config = RunConfig(
    model = model,  
    model_provider = client,
    tracing_disabled = True,
)
# >>>>>>>>> Configuration Done >>>>>>>>> :)