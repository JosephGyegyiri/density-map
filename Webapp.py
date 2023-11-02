import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import plotly.express as px

st.set_page_config(layout="wide")

markdown = """
# Atlanta Crime Cluster Dashboard

Welcome to the Atlanta Crime Cluster Dashboard! 🚓🔍

This interactive dashboard provides insights into crime data in Atlanta, Georgia. The data is sourced from the Atlanta Police Department (2020 data) and is presented in a visually appealing and informative way.

## About This App

This app is designed to help you better understand crime patterns in Atlanta and make informed decisions. It's a valuable tool for law enforcement, city planners, and anyone interested in the safety of Atlanta.

Feel free to explore the various features and analyses provided in this dashboard. If you have any questions or feedback, please don't hesitate to reach out.

Enjoy your exploration! (Joseph Gyegyiri, 2022)
"""
markdown2 = """
         Joseph Gyegyiri is a graduate student of Florida Atlantic University, pursuing a masters in civil engineering with a concentartion in Geomatics and Transportation Engineering.
         He aspire to be a geospatial analyst/developer where he would utilize geospatial science and engineering for a better world
         """


st.sidebar.title("About")
st.sidebar.markdown(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.sidebar.write("About Author")
logo2 = 'https://josephgyegyiri.github.io/assets/images/out.jpg'
st.sidebar.image(logo2)
st.sidebar.markdown(markdown2)

st.title("Atlanta Crime Cluster")


@st.cache_data
def load_data():
    df = pd.read_csv('https://raw.githubusercontent.com/JosephGyegyiri/density-map/main/atl.csv')
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    return df






with st.expander("See source code"):
    with st.echo():
        custom_colors = {
    "Type1": "#FF0000",  
    "Type2": "#0000FF",  
    "Type3": "#00FF00",  
    "Type4": "#FFA500",  
    "Type5": "#800080",  
    "Type6": "#FFFF00", 
    "Type7": "#000000",  
}

        m = leafmap.Map(
            location=[33.7791, -84.388],  # Set the initial center
            zoom_start=13,  # Set the initial zoom level
        )

        crime = load_data()
        #m.add_geojson(regions, layer_name='US Regions')
        m.add_points_from_xy(
            crime,
            x="longitude",
            y="latitude",
            color_column='crimetype',
            icon_names=['gear', 'map', 'leaf', 'globe', 'star', 'cloud', 'fire'],
            spin=True,
            add_legend=True,
        )

m.to_streamlit(height=800)

# Time series chart of each crime type per month
with st.expander("Crime Counts"):
    st.write("Crime Counts")
    
    # Handle date format inconsistencies
    agg_data = crime.groupby('crimetype')['crimetype'].count().reset_index(name='Count')

    fig = px.bar(agg_data, x='crimetype', y='Count', color='crimetype', title = 'Crime Types Distribution' , labels={'x': "Crime Type", 'y':"Number of Incidents"},
                 template= 'plotly_white')
    fig.update_xaxes(tickangle=-45)
    st.plotly_chart(fig)

    

with st.expander("Crime per Day of the Week"):
    st.write("Crime per Day of the Week")
    
    day_of_week_counts = crime['day occurred'].value_counts().sort_index()
    day_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_of_week_counts.index = day_labels  # Replace index with day names for plotting
    
    # Create a bar plot using Seaborn
    fig, ax = plt.subplots()
    sns.barplot(x=day_labels, y=day_of_week_counts, ax=ax, palette="Blues")
    ax.set_ylabel('Number of Crimes')
    ax.set_xlabel('Day of the Week')
    ax.set_title('Crime Counts by Day of the Week')
    st.pyplot(fig)
