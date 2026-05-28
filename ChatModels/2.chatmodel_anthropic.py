from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()


print("Initializing ChatOpenAI model...")

chat_model = ChatAnthropic(model="claude-2", temperature=0.9)
chat_model_response = chat_model.invoke("Write a mail to company for full stack Role ?")
print( chat_model_response.content)
