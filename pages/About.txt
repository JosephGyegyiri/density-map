import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")



st.write("""

## About This App

This app is designed to help you better understand crime patterns in Atlanta and make informed decisions. It's a valuable tool for law enforcement, city planners, and anyone interested in the safety of Atlanta.

Feel free to explore the various features and analyses provided in this dashboard. If you have any questions or feedback, please don't hesitate to reach out.

Enjoy your exploration! (Joseph Gyegyiri, 2022)
"""
        )

st.write("About Author")

st.write(" ")
st.image('https://media.licdn.com/dms/image/D4E03AQHUL3mFEUHptg/profile-displayphoto-shrink_800_800/0/1668234298036?e=1697673600&v=beta&t=ZTWrHw786rKyoAWueLxq2BBg3MjHTEBZqAj5ahRz7uE')
st.write("""
         Joseph Gyegyiri is a graduate student of Florida Atlantic University, pursuing a masters in civil engineering with a concentartion in Geomatics and Transportation Engineering.
         He aspire to be a geospatial analyst/developer where he would utilize geospatial science and engineering for a better world
         """)
