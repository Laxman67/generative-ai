from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

load_dotenv()
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task="text-generation", temperature=0
# )

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash", task="text-generation"
)
model = ChatHuggingFace(llm=llm)


# Prompt 1  = Detailed Reports
template1 = PromptTemplate(
    template="Write a detailed report about the {topic}", input_variables=["topic"]
)

# Prompt 2 = Summarization

template2 = PromptTemplate(
    template="Write a 5 Line  summary on  the following text \n {text}",
    input_variables=["text"],
)

prompt1 = template1.invoke({"topic": "Mahabaharata"})
result = model.invoke(prompt1)
print(result)

prompt1 = template2.invoke({"text": result.content})
result1 = model.invoke(prompt1)
print(result1.content)
