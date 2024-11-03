import json
import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta
import os

# Load data from json file
def load_data(file):
    if os.path.basename(file) == "pantry_inventory.csv":
        return pd.read_csv(file, parse_dates=['Expiration Date'])
    else:
        # assumes its reading the grocery list
        return pd.read_csv(file)

# Save data to CSV file
def save_data(df, file):
    df.to_csv(file, mode='a', header=False, index=False)