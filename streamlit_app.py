import streamlit as sl
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

sl.title('This is just a begining of the Streamlit new cool App')

sl.header('Healthy Choices Menu')

sl.text('🥣 Omega 3 & Blueberry Oatmeal')
sl.text('🥗 Kale, Spinach & Rocket Smoothie')
sl.text('🐔 Hard-Boiled Free-Range Egg')
sl.text('🥑🍞 Avocado & Toast')

sl.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#set index to the specific col
my_fruit_list = my_fruit_list.set_index('Fruit')

# Pick list
fruits_selected = sl.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

sl.dataframe(fruits_to_show)

def get_fruityvice_data(cur_fruit_choice):
  fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + cur_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

sl.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = sl.text_input('What fruit would you like info about?', 'Kiwi')
  if not fruit_choice:
    sl.error('Please select a fruit to get information.')
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    sl.dataframe(back_from_function)
except URLError as e: 
  sl.error()

### STOP
#sl.stop()
#sl.write('The user entered', fruit_choice)

sl.header("Fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
#Add button
if sl.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  sl.dataframe(my_data_rows)

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values (%s)", new_fruit)
    return "Thanks for adding " + new_fruit
    
input_fruit = sl.text_input('What fruit would you like to add?', 'Jackfruit')
if sl.button('Add Fruit to the List'):
  my_cnx = snowflake.connector.connect(**sl.secrets["snowflake"])
  add_fruit = insert_row_snowflake(input_fruit)
  my_cnx.close()
  sl.text(add_fruit)
