import os
import credentials
os.environ["OPENAI_API_KEY"] = credentials.api_key

from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

llm = OpenAI(temperature=0.7)
     
#text = "what are the 5 most expensive capital cities?"
#print(llm(text))

#prompt = PromptTemplate(
 #   input_variables=["input"],
  #  template = "Which are the 5 most {input} capital cities?"
#)

#print(prompt.format(input="popular"))
     

prompt=PromptTemplate(
    input_variables=["country"],
    template="where is the capital of {country}"
)
     
chain = LLMChain(llm=llm, prompt=prompt)

val = input("Enter a country: ")

print(chain.run(val))
