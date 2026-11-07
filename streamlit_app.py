import gettext
import glob
import os
import re
from pathlib import Path

import pandas as pd
import streamlit as st
from viewer_i18n import choose_language
from language_constants import LANGUAGE_FLAG_DICTIONARY
from PIL import Image

st.set_page_config(layout="wide")

languages = sorted(path.name for path in Path("content").iterdir() if path.is_dir())
if "language" not in st.session_state:
    st.session_state.language = choose_language(
        st.query_params.get("language"),
        st.context.headers.get("Accept-Language", "en"),
        languages,
    )


def update_params():
    # Preserve unrelated parameters and keep language/day links shareable.
    st.query_params["language"] = st.session_state.language
    st.query_params["challenge"] = st.session_state.get("day", "Day1")


selected_language = st.sidebar.selectbox(
    "Language / 언어", languages, key="language", on_change=update_params,
    format_func=lambda code: f"{LANGUAGE_FLAG_DICTIONARY.get(code, '')} {code}",
)
_ = gettext.translation(
    "messages", localedir="locale", languages=[selected_language], fallback=True
).gettext


def format_day(label):
    return _("Day {day}").format(day=int(re.search(r'\d+', label).group()))


md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob1(f"content/{selected_language}", "*.md")]
)

placeholder = st.empty()
with placeholder:
    st.write(_("Day {day}").format(day=1))
placeholder.empty()

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))
st.markdown(_("# 30 Days of Streamlit"))

days_list = [f"Day{x}" for x in md_files]

requested_day = st.query_params.get("challenge")
if requested_day in days_list:
    st.session_state.day = requested_day
elif st.session_state.get("day") not in days_list:
    st.session_state.day = days_list[0]

selected_day = st.selectbox(
    _("Start the Challenge 👇"), days_list, key="day", on_change=update_params,
    format_func=format_day
)

with st.expander(_("About the #30DaysOfStreamlit")):
    st.markdown(_(
        """
    The **#30DaysOfStreamlit** is a coding challenge designed to help you get started in building Streamlit apps.
    
    Particularly, you'll be able to:
    - Set up a coding environment for building Streamlit apps
    - Build your first Streamlit app
    - Learn about all the awesome input/output widgets to use for your Streamlit app
    """
    ))

# Sidebar
st.sidebar.header(_("About"))
st.sidebar.markdown(_(
    "[Streamlit](https://streamlit.io) is a Python library that allows the creation of interactive, data-driven web applications in Python."
))

st.sidebar.header(_("Resources"))
st.sidebar.markdown(_(
    """
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Book](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
"""
))

st.sidebar.header(_("Deploy"))
st.sidebar.markdown(_(
    "You can quickly deploy Streamlit apps using [Streamlit Community Cloud](https://streamlit.io/cloud) in just a few clicks."
))

# Display content
for day in days_list:
    if selected_day == day:
        st.markdown(_("# 🗓️ Which {day_num}").format(day_num=int(re.search(r'\d+', day).group())))
        with open(f"content/{selected_language}/{day}.md", "r", encoding="utf-8") as f:
            st.markdown(f.read())
        if os.path.isfile(f"content/{selected_language}/figures/{day}.csv"):
            st.markdown("---")
            st.markdown(_("### Figures"))
            df = pd.read_csv(f"content/{selected_language}/figures/{day}.csv", engine="python")
            for i in range(len(df)):
                st.image(f"content/{selected_language}/images/{df.img[i]}")
                st.info(f"{df.figure[i]}: {df.caption[i]}")
