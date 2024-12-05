import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from streamlit_calendar import calendar

# Sample data
events = [
    {"title": "UFC 290", "start": datetime(2023, 7, 8), "end": datetime(2023, 7, 8)},
    {"title": "Bellator 300", "start": datetime(2023, 8, 15), "end": datetime(2023, 8, 15)},
]

fighters = [
    {"name": "Khabib Nurmagomedov", "weight_class": "Lightweight", "record": "29-0"},
    {"name": "Amanda Nunes", "weight_class": "Featherweight/Bantamweight", "record": "22-5"},
    {"name": "Conor McGregor", "weight_class": "Lightweight/Featherweight", "record": "22-6"}
]

# Streamlit app setup
st.set_page_config(page_title="MMA Tracker", page_icon="🥊", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Event Calendar", "Fighter Profiles", "News"])

# Home Page
if selection == "Home":
    st.title("Welcome to MMA Tracker")
    st.write("""
    Here you can find information about upcoming MMA events, fighter profiles, and the latest news in the world of Mixed Martial Arts.
    """)

# Event Calendar
elif selection == "Event Calendar":
    st.title("MMA Event Calendar")
    calendar(events)

# Fighter Profiles
elif selection == "Fighter Profiles":
    st.title("Fighter Profiles")
    for fighter in fighters:
        st.subheader(fighter['name'])
        st.write(f"**Weight Class:** {fighter['weight_class']}")
        st.write(f"**Record:** {fighter['record']}")
        st.markdown("---")

# News Feed
elif selection == "News":
    st.title("MMA News Feed")
    st.write("Here are the latest updates from the MMA world:")
    # Here you would typically fetch real-time data from an API or RSS feed
    st.write("**Conor McGregor hints at return** - McGregor has teased his return to the octagon via Twitter.")
    st.write("**New signing at ONE Championship** - ONE Championship has signed a new heavyweight contender.")
    st.write("**UFC Gym opens in London** - A new UFC Gym has opened its doors in central London.")

# Additional features can be added like:
# - A search function for fighters or events
# - Detailed fight cards for each event
# - Live updates during events (which would require more complex setup)

# Run the app with `streamlit run your_script.py`
