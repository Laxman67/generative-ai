from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()


print("Initializing ChatOpenAI model...")

# llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Pro",task="text-generation")
# llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Flash",task="text-generation")
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash", task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("Who is PM of India ?")
print(result.content)
