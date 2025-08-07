import streamlit as st

from auth import check_password  # 👈 import your password checker

if not check_password():
    st.stop()

st.set_page_config(page_title="About Us", page_icon="👥")

st.title("👥 About Us")

small_font_main = """
<div style='font-size:14px'>
We're a team of 3 from BCA’s Construction Productivity and Quality Group (2 from the Digitalisation Dept + 1 from the Buildable Design Dept). We've worked on projects under CORENET X (CX) and encountered some of the common challenges that come with the process. As such, we're exploring how AI can help make the work smoother and less time-consuming — especially when it comes to processing and understanding complex BIM models. 
<br><br>

<h4>🔍 Problem Scope</h4>
<p>The project addresses the challenges associated with interpreting complex building data in Industry Foundation Classes (IFC) models, particularly issues stemming from:</p>
<ol type="a" style="margin-left: 20px;">
  <li>Inconsistent or abbreviated naming conventions</li>
  <li>Difficulty in accurately identifying properties of elements (e.g. precast walls)</li>
</ol>

<h4>🎯 Objectives</h4>
<ol type="a" style="margin-left: 20px;">
  <li>Improve clarity and accuracy in understanding complex IFC model data assisted by AI</li>
  <li>Deepen understanding and supporting informed design and construction decisions</li>
</ol>

<h4>🗂️ Data sources</h4>
<ul style="margin-left: 20px;">
  <li>IFC files containing:
    <ul>
      <li>Building element geometries and properties</li>
      <li>Naming conventions (including abbreviations/shorthand)</li>
    </ul>
  </li>
  <li>Extracted data is structured into:
    <ul>
      <li>JSON format for easy integration and manipulation</li>
      <li>AI embeddings for semantic understanding and searchability</li>
    </ul>
  </li>
</ul>

<h4>🚀 Features</h4>
<ul style="margin-left: 20px;">
  <li><strong>IFC File Processor</strong>:
    <ul>
      <li>Automatically extracts and cleans building data</li>
      <li>Converts information into structured JSON</li>
      <li>Creates AI embeddings to enhance semantic search</li>
    </ul>
  </li>

  <li><strong>Interactive Viewer</strong>:
    <ul>
      <li>Visual representation of building elements</li>
      <li>Highlights selected components and count them by type</li>
    </ul>
  </li>

  <li><strong>AI-Powered Chatbot</strong>:
    <ul>
      <li>Allows users to query data in natural language</li>
      <li>Assists in navigating and understanding complex model details</li>
    </ul>
  </li>
</ul>
</div>
"""

st.markdown(small_font_main, unsafe_allow_html=True)
