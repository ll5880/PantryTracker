import json
import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta
import IO

# Set up the app
st.title("Welcome to your Pantry")

# make the columns
col1, col2 = st.columns(2)
with col1:
    st.subheader("Items expired or Out of Stock")
    df = pd.DataFrame(IO.load_data())
    currentDate = pd.to_datetime(datetime.date.today())
    empty_items = df[df['Expiration Date'] == currentDate]
    st.dataframe(empty_items)
with col2:
    st.subheader("Items close to expiring or Low in stock")
    df = pd.DataFrame(IO.load_data())
    currentDate = datetime.datetime.now()
    low_items = df.query('Quantity == 2')
    st.dataframe(low_items)

# side bar info
with st.sidebar: 
    st.page_link("main.py", label="Home")
    st.page_link("pages/managePantry.py", label="Manage Your Pantry")
    