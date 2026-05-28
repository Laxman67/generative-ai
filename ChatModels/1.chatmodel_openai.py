from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


print("Initializing ChatOpenAI model...")

chat_model = ChatOpenAI(model="gpt-4o", temperature=0,max_completion_tokens=30)
chat_model_response = chat_model.invoke("Write a mail to company for full stack Role ?")
print( chat_model_response.content)
