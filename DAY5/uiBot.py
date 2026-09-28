import ollama
import streamlit as st
st.title(":rainbow[ ☠️Welcome to My AI Chat Application]")
with st.sidebar:
    st.header(":blue[Chat Settings 🤖]")
    if st.button("Clear Chat🗑️"):
        st.session_state.messages=[]
        st.success("Chat cleared✌️")
    personalities = {
        "Kid 👧" : "Answer the question like you are explaining to a 5 year old kid in 2 lines only.",
        "Friend 🧑‍🤝‍🧑" : "Answer the question in a friendlly and casual manner. Give me 2 lines only.",
        "Student👩‍🎓 " : "Answer the question in a teacher and friendly manner. Give me 2 lines only."
    }
    personality = st.selectbox("Select a personality", personalities.keys())
    uploaded_file = st.file_uploader("upload a text file...")
    try:
        if uploaded_file:
            st.success("File uploaded successfully")
            context = uploaded_file.read().decode("utf-8")
            if st.button("Display"):
                st.text(context)
    except:
        st.error("Error")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question=st.chat_input("Ask question: ")
st.write(question)
if question:
    st.session_state.messages.append(

    {
        "role" : "user",
        "content": question
    }
)
with st.chat_message("user"):
    st.write(question)
with st.spinner("Thinking...🤔"):
    response = ollama.chat(
        model = "llama3.2:3b",
        messages = [
            {"role": "system","content": personalities[personality]}]
            + st.session_state.messages
)
st.session_state.messages.append(
        {"role": "assistant",
        "content": response["message"]["content"]}
    )
with st.chat_message("assistant"):
    st.write("AI", response["message"]["content"])



