import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf) #each pdf file
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
    

def main():
    load_dotenv()
    st.set_page_config(page_title = "Check PDFs")

    st.header("Check PDFs")
    st.text_input("Enter your question:")

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                #get text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                #get chunks
                
                #create vector store
    

if __name__ == '__main__':
    main()