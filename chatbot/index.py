import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import time
import streamlit as st
from dotenv import load_dotenv
import time

# Initialize the language model and output parser
llm = Ollama(model="llama2")
output_parser = StrOutputParser()


prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)



# Streamlit app
def main():
    st.title("Topic Search App")
    input_text = st.text_input("Search the topic you want")
    if input_text:
        # Create the chain and invoke it with the user input
        startTime = time.time() 
        chain = prompt | llm | output_parser
        result = chain.invoke({"question": input_text})
        resultTime = time.time()
        st.write(result)
        endTime = time.time()
        st.divider()
        st.write("The time taken is {restime} and final time {finaltime}".format(restime = str(resultTime -startTime ), finaltime = str(endTime - startTime)))


if __name__ == "__main__":
    main()

