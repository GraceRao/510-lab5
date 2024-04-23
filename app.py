import streamlit as st
import pandas as pd
import psycopg2
import os

st.set_page_config(
    page_title="Book Search & Filter App",
    page_icon="📚",
    layout="centered",
)
