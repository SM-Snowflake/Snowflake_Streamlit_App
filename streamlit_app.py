import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 Omega 3 & Blueberry Oatmeal\n'
              '🥗 Kale, Spinach & Rocket Smoothie\n'
              '🐔 Hard-boiled Free-Range Egg\n'
              '🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)

#Adding a pick list, so that customers can pick the fruits they want to include
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))

#display the table on the page
streamlit.dataframe(my_fruit_list)

