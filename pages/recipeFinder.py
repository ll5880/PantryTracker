import streamlit as st
from openai import OpenAI
import openai
from streamlit_chat import message
import IO
import api_key

def get_items_from_pantry():
    df = IO.load_data("pantry_inventory.csv")
    # get items where quantity is not low / expired
    full_items = df.query('Quantity != 0')
    # only get a list of the items names
    full_items_names = full_items["Item Name"]
    # return that 
    return full_items_names


api_key = api_key.api_key

st.title("Find Recipes base on your pantry!")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    client = OpenAI(api_key=api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
