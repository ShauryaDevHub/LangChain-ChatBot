## Integrate our code OpenAI API
import os
from constants import openai_key
from langchain.llms import OpenAI 

import streamlit as st
from langchain import PromptTemplate #to create specific category promppt
from langchain.chains import LLMChain
from langchain.chains import  SequentialChain
from langchain.memory import ConversationBufferMemory
#capable of receiving user input, 
#formatting it using a PromptTemplate, and then passing this formatted response to the LLM. 
os.environ["OPENAI_API_KEY"]=openai_key

# streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic you want")

## OPENAI LLMS
llm=OpenAI(temperature=0.8)



if input_text:
    st.write(llm(input_text))



first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell, me about celebrity {name} "

 
)

person_memory = ConversationBufferMemory(input_key='name', memory_key='chat_history')
dob_memory = ConversationBufferMemory(input_key='person', memory_key='chat_history')
descr_memory = ConversationBufferMemory(input_key='dob', memory_key='description_history')
#creating llm chain
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='person')

second_input_prompt = PromptTemplate(
    input_variables=['person'],
    template="when was {person} born "

 
)

chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob')

third_input_prompt = PromptTemplate(
    input_variables=['dob'],
    template="when was {dob} born "

 
)

chain3=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='description')

parent_chain=SequentialChain(chains=[chain,chain2,chain3],input_variables=['name'],output_variables=['person','dob','description'],verbose=True)

if input_text:
    st.write(parent_chain({'name':input_text}))

    with st.expander('Person Name'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events'): 
        st.info(descr_memory.buffer)


