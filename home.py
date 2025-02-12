import streamlit as st

intro_page = st.Page(
    "pages/introduction.py",
    title="Introduction",
    icon=":material/account_circle:",
    default=True,
)

predictions = st.Page(
    "pages/predict.py",
    title="Prediction",
    icon=":material/leaderboard:",
)

# Navigation
pg = st.navigation(
    {
        "Final Project": [intro_page, predictions],
    }
)

# Run the navigation
pg.run()