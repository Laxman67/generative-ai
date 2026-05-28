from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=300)

texts = [
    "Python is a high-level programming language.",
    "Machine learning models use embeddings for semantic search.",
    "FastAPI is a modern web framework for building APIs with Python.",
    "LangChain helps developers build AI-powered applications.",
    "Vector databases store embeddings for similarity search.",
    "NumPy is used for numerical computing in Python.",
    "Pandas is useful for data analysis and manipulation.",
    "Transformers are deep learning models for NLP tasks.",
    "OpenAI provides APIs for AI and language models.",
    "Embeddings convert text into numerical vector representations.",
]

query ='Tell me about Vector?'

doc_embedding = embedding.embed_documents(texts)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embedding)

index,score =sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]


print(query)
print(texts[index])
