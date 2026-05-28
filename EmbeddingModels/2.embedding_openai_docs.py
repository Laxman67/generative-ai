from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = ["Delhi is the capital of India", "Kolkata is the capital of west Bengal"]
embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

result = embedding.embed_documents(documents)

print(str(result))
