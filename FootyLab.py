import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import streamlit as st
import altair as alt
from streamlit_ace import st_ace
import streamlit.components.v1 as components
#import folium
#from folium.plugins import HeatMap
#import seaborn as sns

st.set_page_config(
    page_title="One Knox 2013B Yellow Pool Data WebApp | DataRook, Inc.",
    page_icon="./media/footylab_v2_icon.png",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://datarook.com/contact',
        'About': "## This is being custom made by Gus Alvarez for the One Knox 2013B Yellow Pool. Contact gus@datarook.com to learn more"
    }
)

if "user" not in st.session_state:
    st.session_state.user = None
#if "password" not in st.session_state:
#     st.session_state.password = None

ROLES = [None,"Yellow"]
allroles = ["Yellow"]
#playersdeployed = ["Coach Gus", "Kellan", "Dashley", "AyMarri"]
def login():

    st.header("Log in")
    user = st.selectbox("Team", ROLES)
    #password = st.text_input("Password")

    if st.button("Log in"):
        st.session_state.user = user
        #st.session_state.password = password
        st.rerun()


def logout():
    st.session_state.user = None
    #st.session_state.password = None
    st.rerun()


user = st.session_state.user
#password = st.session_state.password

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

BootRoom = st.Page(
    "./coach/1_BootRoom.py",
    title="BootRoom",
    icon=":material/interactive_space:",default=(user == "Yellow")
)
coachGus = st.Page(
    "./coach/coachGus.py", title="Coach's Examples", icon=":material/sports:",default=(user == "Coach Gus")
)
classpage = st.Page(
    "./coach/Class_Page.py",
    title="⚽🧑‍🔬",
    icon=":material/school:"
)


account_pages = [logout_page, settings]
explore_pages = [BootRoom, classpage]
#build_pages = [coachGus]
#deployed_pages = [classpage]

page_dict = {}

#if (st.session_state.user in allroles):
#    page_dict["Build"] = build_pages
if (st.session_state.user in allroles):
    page_dict["Explore"] = explore_pages
#if (st.session_state.user in allroles):
#    page_dict["Deployed"] = deployed_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()

st.logo("./media/footylab_v2_horizontal.png",link="https://datarook.com/")

st.divider()
st.header("Links and Resources")
col1, col2 = st.columns(2)
with col1:
      st.page_link("https://app.veo.co/clubs/datarook-academy/teams/one-knox-2013b-yellow/#recordings", label="Veo Game Footage", icon="🎥")
      #st.subheader("Streamlit ~~Docs~~ Spellbook")
      #st.page_link("https://docs.streamlit.io/develop/api-reference", label="Click me to read about Streamlit ~~methods~~ spells", icon="🪄")
      #uploaded_file = os.path.join(str(pathlib.Path().resolve()), './data/last30days_GPS.csv')
      #with open(uploaded_file) as f:
      #      btn = st.download_button(
       #           label="Download Last 30 Days GPS Data",
        #          data = f,
         #         file_name="gps_data.csv",
          #        mime="text/csv"
           #     )

with col2:
      st.page_link("https://gusalvarez.notion.site/One-Knox-2013B-Yellow-66f6f237836e4599bf025e5becb0db7e", label="Yellow Pool Home", icon="🏡")
      #st.page_link("https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/", label="Emoji Codes!", icon="😎")
      #st.page_link("https://app.veo.co/clubs/datarook-academy/teams/soccer-lab/#recordings", label="Game Footage", icon="🎥")
      #st.page_link("https://forms.gle/7Zn14EdkySSFArir8", label="Day 1 Info Form", icon="📋")
      