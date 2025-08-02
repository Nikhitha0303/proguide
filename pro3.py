import streamlit as st
#from fpdf import FPDF
import google.generativeai as genai

# ---- Gemini API configuration ----
# For security, you should ideally load your API key from an environment variable.
genai.configure(api_key="AIzaSyBTXbOpIVuvwnmU-NYSkXMB2J46L4sAwjE")  # <-- Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-flash")    # Or "gemini-pro" if you have access

# ---- Streamlit UI Setup ----
st.set_page_config(page_title="AI Project Guide Generator", layout="wide")
st.title("✨ AI Project Guide Generator ✨")

st.markdown("""
Welcome! Enter your AI Project Title and click below to generate:
- 📄 Project Guide  
- 💻 Code Snippets  
- 🎓 Viva Q&A  
- 📚 Documentation
""")

project_title = st.text_input(
    "Enter your Project Title", 
    placeholder="e.g., AI Powered Code Explainer"
)

if project_title:
    # Arrange buttons in a horizontal row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        guide_btn = st.button("Generate Project Guide")
    with col2:
        code_btn = st.button("Generate Code Snippets")
    with col3:
        viva_btn = st.button("Generate Viva Q&A")
    with col4:
        doc_btn = st.button("Generate Documentation")

    # ---- Project Guide ----
    if guide_btn:
        with st.spinner("Generating project guide..."):
            guide_prompt = f"""
You are an expert academic assistant. Generate a clean, professional project guide for the following title:
Project Title: {project_title}
Include ONLY the following in this response:

## Project Description
## Key Features
## Recommended Tech Stack
## Implementation Plan
1. Phase 1: Setup
2. Phase 2: Core Development
3. Phase 3: Testing
4. Phase 4: Deployment
## Future Enhancements
"""
            guide_text = model.generate_content(guide_prompt).text

        st.subheader("📘 Project Guide")
        st.text_area("View Guide", guide_text, height=400)

       
    # ---- Code Snippets ----
    if code_btn:
        with st.spinner("Generating code snippets..."):
            code_prompt = (
                f"Generate code snippets in Python for key modules "
                f"of the project titled '{project_title}'."
            )
            code_text = model.generate_content(code_prompt).text

        st.subheader("💻 Code Snippets")
        st.text_area("View Code Snippets", code_text, height=200)
      

    # ---- Viva Q&A ----
    if viva_btn:
        with st.spinner("Generating viva questions..."):
            viva_prompt = (
                f"Generate viva questions and answers for the project titled '{project_title}'."
            )
            viva_text = model.generate_content(viva_prompt).text

        st.subheader("🎓 Viva Questions & Answers")
        st.text_area("View Viva Q&A", viva_text, height=200)
      #  st.download_button("⬇ Download Viva Q&A", viva_text, file_name="Viva_QA.txt")

    # ---- Documentation ----
    if doc_btn:
        with st.spinner("Generating full documentation..."):
            doc_prompt = (
                f"Generate complete documentation for the project titled '{project_title}'."
            )
            doc_text = model.generate_content(doc_prompt).text

        st.subheader("📚 Full Documentation")
        st.text_area("View Documentation", doc_text, height=200)
       # st.download_button("⬇ Download Documentation", doc_text, file_name="Documentation.txt")

else:
    st.info("👆 Enter a project title to begin.")

