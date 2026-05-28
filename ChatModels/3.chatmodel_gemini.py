from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


print("Initializing ChatOpenAI model...")

chat_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chat_model_response = chat_model.invoke("Write a mail to company for full stack Role ?")
print( chat_model_response.content)
