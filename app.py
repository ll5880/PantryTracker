import json
import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta
import IO
import manageExpired 
    
st.logo("/Users/lucielim/personal-Projects/PantryTracker/Screenshot 2024-11-02 at 22-44-58 DALL·E 2024-11-02 22.44.26 - A modern 2D logo for a product called 'Flavor Savor ' a pantry tracking app. The design features a stylized pantry or shelf icon with neatly organized.webp (WEBP Image 1024 × 1024 pix[...].png")
 
# Set up the app
st.title("Welcome to your Pantry")

# make the columns
col1, col2 = st.columns(2)
with col1:
    st.subheader("Items expired or Out of Stock")
    df = pd.DataFrame(IO.load_data("pantry_inventory.csv"))
    empty_items = manageExpired.get_gone_items()
    st.dataframe(empty_items)
with col2:
    st.subheader("Items close to expiring or Low in stock")
    low_items = manageExpired.get_low_stock()
    st.dataframe(low_items)

# upcoming grocery list
st.subheader("Upcoming Grocery List")
st.dataframe(IO.load_data("grocery_list.csv"))

st.button("Add low items to grocery list", on_click=manageExpired.add_expired_items())
st.download_button(
    label="Download Grocery List as csv",
    data=(pd.DataFrame(IO.load_data("grocery_list.csv"))).to_csv(index=False).encode('utf-8'),
    file_name="groceryList.csv",
    mime="text/csv",
)

# side bar info
with st.sidebar: 
    st.page_link("app.py", label="Home")
    st.page_link("pages/managePantry.py", label="Manage Your Pantry")
    st.page_link("pages/recipeFinder.py", label="Find Recipes")
    