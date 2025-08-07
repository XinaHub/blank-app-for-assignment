import streamlit as st
from auth import check_password  # 👈 import your password checker

if not check_password():
    st.stop()

st.set_page_config(page_title="Flowchart", page_icon="📊")

st.title("📊 Analysis Page")
st.write("Flowchart.")
