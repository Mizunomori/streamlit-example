from collections import namedtuple
import altair as alt
#from tkinter import Image
import math
import streamlit as st
import numpy as np
import time 
import pandas as pd

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.title("SYSEN 5150 HW 1")
st.subheader("Demonstration of data elements") 

st.metric(label="Price", value= "$3.50" ,delta=None, delta_color="normal") 

df = pd.DataFrame( 
    np.random.randn(17,7),columns=('col %d' % i for i in range(7))
) 

st.table(df) 

chart_data = pd.DataFrame(
     np.random.randn(27, 4),
     columns=['a', 'b', 'c', 'd'])

with st.container():
    st.line_chart(chart_data) 

with st.expander(label="Area Chart", expanded= True):
    st.area_chart(chart_data) 


inverter = st.checkbox('Inverter Level')

if inverter: 
    st.write('Inverter data') 



st.image(image = "https://www.theventuremag.com/wp-content/uploads/2018/10/iStock-961433280.jpg", caption='Solar array')

video_file = open('star.mp4', 'rb') 
video_bytes = video_file.read() 
st.video(video_bytes) 

bar = st.progress(0) 
for percent_complete in range(100): 
    time.sleep(0.02)
    bar.progress(percent_complete+1) 

st.error('Invalid site name')

with st.form("Site Info"):
    
    slider_val = st.slider("Number of Inverters")
    checkbox_val = st.checkbox("MPPT")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

#st.experimental_rerun() 

the_table = pd.DataFrame(
    np.random.randn(2, 4),
    columns=('col %d' % i for i in range(4)))

df2 = pd.DataFrame(
    np.random.randn(2, 4),
    columns=('col %d' % i for i in range(4)))
the_table.add_rows(df2) 

st.experimental_show(the_table) 

st.help(np.matrix) 

@st.experimental_memo
def fetch_and_clean_data(url = "https://docs.google.com/spreadsheets/d/1vy0pSDILrhLdsFSS9gaETO1iVAgvKC1R/edit?rtpof=true"):
     # Fetch data from URL here, and then clean it up.
        return data

d1 = fetch_and_clean_data(url = "https://docs.google.com/spreadsheets/d/1vy0pSDILrhLdsFSS9gaETO1iVAgvKC1R/edit#gid=1245828365")
# Actually executes the function, since this is the first time it was
# encountered.

if st.button("Clear All"):
    # Clear values from *all* memoized functions:
    # i.e. clear values from both square and cube
    st.experimental_memo.clear() 

