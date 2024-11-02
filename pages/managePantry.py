import json
import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta
import IO

# load pantry data, df is a dictionary
df = IO.load_data()

st.header("Add a Pantry Item")
with st.form("add_item_form"):
    item_name = st.text_input("Item Name", "")
    quantity = st.number_input("Quantity", min_value=1, value=1)
    purchase_date = st.date_input("Purchase Date", value=datetime.date.today())
    expiration_date = st.date_input("Expiration Date", value=datetime.date.today() + timedelta(days=30))
    
    submitted = st.form_submit_button("Add Item")
    
    if submitted:
        new_item = pd.DataFrame([{
            'Item': item_name,
            'Quantity': quantity,
            'Purchase Date': purchase_date,
            'Expiration Date': expiration_date
        }])
        IO.save_data(new_item)
        st.success(f"{item_name} added to pantry!")
        
# display the pantry items
st.header("Pantry Items")
st.dataframe(IO.load_data())
