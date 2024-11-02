import json
import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta

# Load data from json file
def load_data():
    try:
        return pd.read_csv("pantry_inventory.csv", parse_dates=['Expiration Date'])
    except FileNotFoundError:
        return pd.DataFrame(columns=['Item', 'Quantity', 'Purchase Date', 'Expiration Date'])

# Save data to CSV file
def save_data(df):
    df.to_csv("pantry_inventory.csv", mode='a', header=False, index=False)