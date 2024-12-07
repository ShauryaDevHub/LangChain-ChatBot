## Integrate our code OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI 

import streamlit as st
from langchain import PromptTemplate

os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

## OPENAI LLMS
llm=OpenAI(temperature=0.8)



if input_text:
    st.write(llm(input_text))



first_inout_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell, me about {name} "
)