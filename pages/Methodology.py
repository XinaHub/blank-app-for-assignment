import streamlit as st
from auth import check_password  # 👈 import your password checker

if not check_password():
    st.stop()

st.set_page_config(page_title="Methodology", page_icon="📊")

st.title("📊 Flowchart")

st.image("flowchart1.png", caption="Methodology", use_container_width=True)
