from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set LangChain tracing and API key
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize Streamlit app UI
st.set_page_config(page_title="Langchain Demo", layout="wide")
st.title("Langchain Demo With LLAMA2 API")

# Initialize a list to keep track of past prompts and responses
if "history" not in st.session_state:
    st.session_state["history"] = []

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit sidebar
st.sidebar.title("Ask Your Question")
input_text = st.sidebar.text_input("Enter your question:", key="user_input_key")

# Ollama LLaMA2 model
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Display past prompts and responses in a box
st.subheader("Chat History")
history_box = st.empty()  # Placeholder for the history box

if input_text:
    try:
        # Run the input through the chain and get the response
        response = chain.invoke({"question": input_text})
        
        # Save the prompt and response to the session history
        st.session_state["history"].append({"prompt": input_text, "response": response})
        
        # Display the updated chat history
        with history_box.container():
            for entry in st.session_state["history"]:
                st.markdown(f"**You:** {entry['prompt']}")
                st.markdown(f"**Assistant:** {entry['response']}")
                st.markdown("---")
        
        # Clear the input box after submission
        st.sidebar.text_input("Enter your question:", key="user_input_key", value="")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    # Display existing chat history if no new input
    with history_box.container():
        for entry in st.session_state["history"]:
            st.markdown(f"**You:** {entry['prompt']}")
            st.markdown(f"**Assistant:** {entry['response']}")
            st.markdown("---")
