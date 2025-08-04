import streamlit as st
from src.utils.file_loader import FileLoader
from src.utils.embedding import EmbeddingProcessor
from src.utils.ifc_processing import IFCProcessor, check_ifcopenshell_installation, install_ifcopenshell_message
from src.components.api_key_manager import APIKeyManager
from src.components.overview_tab import OverviewTab
from src.components.elements_tab import ElementsTab
from src.components.download_tab import DownloadTab
from src.components.embeddings_tab import EmbeddingsTab
from src.components.load_embeddings_tab import LoadEmbeddingsTab
from src.components.chat_tab import ChatTab

def main():
    st.title("🎈 IFC File Processor")
    st.write(
        "Process and analyze IFC files with ease. Upload your IFC file or use a sample model to get started."
    )

    st.sidebar.title("About Us")
    
    small_font_sidebar = """
    <div style='font-size:12px'>
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
      <li>Deepening understanding and supporting informed design and construction decisions</li>
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

    st.sidebar.markdown(small_font_sidebar, unsafe_allow_html=True)

    # Initialize file loader
    sample_models_dir = "sample_models"
    sample_files = FileLoader.list_sample_models(sample_models_dir)

    # File selection
    selected_sample = st.selectbox(
        "Or select a sample model:",
        ["None"] + sample_files
    )

    # JSON/IFC file uploader
    uploaded_file = st.file_uploader("Upload a JSON or IFC file", type=["json", "ifc"])

    # Load data
    data = None
    if selected_sample != "None":
        sample_file_path = f"{sample_models_dir}/{selected_sample}"
        data = FileLoader.load_sample_file(sample_file_path)
    elif uploaded_file is not None:
        data = FileLoader.load_uploaded_file(uploaded_file)

    if data:
        # Initialize embedding processor
        if 'embedding_processor' not in st.session_state:
            st.session_state.embedding_processor = EmbeddingProcessor()
        embedding_processor = st.session_state.embedding_processor

        # Create tabs
        tab_names = ["Overview", "Building Elements", "Download", "API Key", 
                    "Generate Embeddings", "Load Embeddings", "Chat"]
        tab_overview, tab_elements, tab_download, tab_api, tab_embeddings, \
        tab_load, tab_chat = st.tabs(tab_names)

        # Render each tab
        with tab_overview:
            OverviewTab.render(data)

        with tab_elements:
            ElementsTab.render(data)

        with tab_download:
            DownloadTab.render(data)

        with tab_api:
            APIKeyManager.render(embedding_processor)

        with tab_embeddings:
            st.subheader("Generate & Manage Embeddings")
            selected_model = EmbeddingsTab.render(embedding_processor)
            
            # Process texts for embedding
            texts = []
            if data.get('file_info', {}).get('type') == 'IFC':
                processor = IFCProcessor()
                texts = processor.convert_to_text_chunks(data)
                st.write(f"Found {len(texts)} elements to process")
                
            EmbeddingsTab.process_and_generate(
                texts, 
                embedding_processor, 
                selected_model,
                st.session_state.get('api_key')
            )
            
            if texts:
                EmbeddingsTab.show_text_descriptions(texts)

        with tab_load:
            LoadEmbeddingsTab.render(embedding_processor)

        with tab_chat:
            ChatTab.render(embedding_processor)

if __name__ == "__main__":
    main()
            # For IFC files
