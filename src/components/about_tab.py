import streamlit as st

class AboutTab:
    @staticmethod
    def render():
        st.markdown("""
        # About Us
        
        **Subject:** AI-assisted IFC Processor and Viewer
        
        ## 🔍 Problem Statement
        The complexity of building data represented in Industry Foundation Classes (IFC) 
        models poses challenges in accurately identifying the properties of various elements 
        (e.g., precast walls). The use of abbreviations and shorthand notations in naming 
        conventions contributes to confusion and misinterpretation, resulting in 
        inefficiencies for processing officers.
        
        ## 💡 Solution
        Develop an intelligent IFC File Processor and viewer to enhance the processing 
        and usability of IFC files:
        
        * Efficiently extracts building data
        * Converts it into a structured JSON format
        * Transforms building information into searchable AI embeddings
        * Provides interactive chatbot interface
        """)
