import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

## Langsmit tracking..
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

## chatprompt template
prompt = ChatPromptTemplate.from_messages([
    ('system', 'Hey, your are a helpful assistant. Please respond to the question asked..'),
    ('user', 'Questions : {question}')
])


## streamlit framework
st.title('Gemma AI Assistant')
input_text = st.text_input('What questions you have in mind???' )

## ollama Gemma Model
llm = Ollama(model='gemma:2b')
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write('Question : ', input_text)
    st.write('Answer :',chain.invoke({'question':input_text}))
