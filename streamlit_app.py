import streamlit as sl
import pandas as pd

sl.title('This is just a begining of the Streamlit new cool App')

sl.header('Healthy Choices Menu')

sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale, Spinach & Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado & Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#set index to the specific col
my_fruit_list.my_fruit_list.set_index('Fruit')

# Pick list
sl.multiselect("Pick some fruits: ", list(my_fruit_list.index))

sl.dataframe(my_fruit_list)
