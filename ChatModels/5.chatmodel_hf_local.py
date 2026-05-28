from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()


llm = HuggingFacePipeline.from_model_id(model_id="deepseek-ai/DeepSeek-V4-Flash",task="text-generation",pipeline_kwargs={"max_length": 2048,"temperature": 0.7})

model = ChatHuggingFace(llm=llm)

result= model.invoke("Who is Capital of India ?")
print(result.content)

