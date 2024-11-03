import json
import streamlit as st
import pandas as pd
import datetime
from datetime import timedelta
import IO

def get_gone_items():
	df = pd.DataFrame(IO.load_data("pantry_inventory.csv"))
	currentDate = datetime.datetime.now()
	expired_df = df[df['Expiration Date'].dt.date <= currentDate.date()]
	out_of_stock = df.query('Quantity == 0')
	empty_items = pd.concat([expired_df, out_of_stock], ignore_index=True)
	return empty_items

def get_low_stock():
	df = pd.DataFrame(IO.load_data("pantry_inventory.csv"))
	currentDate = datetime.datetime.now()
	# TODO: expired_df = df[df['Expiration Date'].dt.date >= (currentDate - timedelta(days=7))]
	low_stock_items = df.query('Quantity == 2')
	low_items = pd.concat([low_stock_items], ignore_index=True)
	return low_items

def add_expired_items():
	df = pd.DataFrame(IO.load_data("pantry_inventory.csv"))
	gone_items = get_gone_items()
	low_stock_items = get_low_stock()
	#concat 
	total_gone_items = pd.concat([gone_items, low_stock_items], ignore_index=True)
	#drop column
	total_gone_items.drop('Purchase Date', axis=1, inplace=True)
	total_gone_items.drop('Expiration Date', axis=1, inplace=True)
	IO.save_data(total_gone_items, "grocery_list.csv")
	