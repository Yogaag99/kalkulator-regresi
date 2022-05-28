from math import sqrt
from turtle import textinput
import pandas as pd
import streamlit as st
import numpy as np
import time

st.title("My First App")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

"""
# My first app
Here's our first attempt at using data to create a table:
"""
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})
df

chart_data = pd.DataFrame(
    np.random.randn(20,4),
    columns=['a', 'b', 'c', 'd']
)
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)

if st.checkbox("Show dataframe"):
    chart_data

option = st.sidebar.selectbox(
    'Which number do you like?',
    df['first column']
)

'You Selected: ', option

left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Wohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanation...")

# 'Starting a long computation...'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration {i+1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)

# '...and now we are done!'

text_input = ''
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'hello {text_input}')

st.text('This will appear first')
my_slot1 = st.empty()
my_slot2 = st.empty()
st.text('This will appear last')
my_slot1.text('This will appear second')
my_slot2.line_chart(np.random.randn(20,2))
st.balloons()

data = np.random.randn(10,2)
chart = st.line_chart(data)
time.sleep(1)
data2 = np.random.randn(10,2)
chart.add_rows(data2)

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

name = st.text_input('Name')
if not name:
    st.warning('Please input a name.')
    st.stop()
st.success('Thank you for inputting a name.')

st.error('This is an error')
st.warning('This is a warning')
st.info('This is an info')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)

st.help(pd.DataFrame)