from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
import time
import plotly.express as px
import pandas as pd
import spacy

load_dotenv()
nlp = spacy.load("en_core_web_sm")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="Langchain Demo", layout="wide", initial_sidebar_state="expanded")
st.title("🌟 Langchain Demo with Mixtral API")

if "history" not in st.session_state:
    st.session_state["history"] = []
if "input_text" not in st.session_state:
    st.session_state["input_text"] = ""
if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()
if "response_times" not in st.session_state:
    st.session_state["response_times"] = []
if "responses" not in st.session_state:
    st.session_state["responses"] = []
if "all_text" not in st.session_state:
    st.session_state["all_text"] = ""

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "💬 Chat",
        "📈 Show Analytics"
    ]
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

if page == "💬 Chat":
    st.title("💬 Ask Your Question")
    st.markdown("Feel free to ask anything and get instant responses!")

    input_text = st.text_input("Enter your question:", key="user_input_key", value=st.session_state["input_text"])

    llm = ChatGroq(model="mixtral-8x7b-32768", temperature=0)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    st.subheader("📜 Chat History")
    history_box = st.empty()  

    if input_text:
        start_time = time.time()
        response = chain.invoke({"question": input_text})
        response_time = time.time() - start_time
        
        st.session_state["responses"].append(response)
        st.session_state["response_times"].append(response_time)
        st.session_state["history"].append({"prompt": input_text, "response": response})
        st.session_state["input_text"] = ""

        st.session_state["all_text"] += f" {input_text} {response}"

    with history_box.container():
        for entry in st.session_state["history"]:
            st.markdown(f"<div style='background-color:#f0f0f0;padding:10px;border-radius:10px;color:black'>"
                        f"You: {entry['prompt']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='background-color:#e0ffe0;padding:10px;border-radius:10px;color:black'>"
                        f"Assistant: {entry['response']}</div>", unsafe_allow_html=True)
            st.markdown("---")

if page == "📈 Show Analytics":
    end_time = time.time()
    total_time = end_time - st.session_state["start_time"]
    avg_response_time = (sum(st.session_state["response_times"]) / len(st.session_state["response_times"])) if st.session_state["response_times"] else 0

    st.subheader("📊 Session Analytics")
    st.write(f"**Total Duration:** {total_time:.2f} seconds")
    st.write(f"**Average Response Time:** {avg_response_time:.2f} seconds")

    index = list(range(len(st.session_state["response_times"])))
    values = st.session_state["response_times"]
    df = pd.DataFrame({"x": index, "y": values})
    fig = px.line(df, x="x", y="y", title="Response Time Graph")
    st.plotly_chart(fig)

    doc = nlp(st.session_state["all_text"])
    total_words = len([token.text for token in doc if not token.is_punct])
    stop_words = len([token.text for token in doc if token.is_stop])
    non_stop_words = total_words - stop_words

    st.write(f"**Total Words (excluding punctuation):** {total_words}")
    st.write(f"**Stop Words:** {stop_words}")
    st.write(f"**Non-Stop Words:** {non_stop_words}")

    word_counts = pd.DataFrame({
        "Type": ["Stop Words", "Non-Stop Words"],
        "Count": [stop_words, non_stop_words]
    })
    fig_word_counts = px.bar(word_counts, x="Type", y="Count", title="Word Count with and without Stop Words")
    st.plotly_chart(fig_word_counts)
