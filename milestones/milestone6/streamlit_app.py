"""
EBLA RAG Chat Application
This Streamlit app provides a chat interface for querying EBLA documents using RAG (Retrieval-Augmented Generation).
"""

import streamlit as st
from config import settings
from repositories.database.db_connection import SessionLocal
from services.rag_service import RAGService
from schemas.chat_schema import ChatRequest

st.set_page_config(page_title="EBLA RAG Chat", layout="wide")
st.title("💬 EBLA RAG Assistant")

# Initialize session state
if "session_id" not in st.session_state:
    st.session_state.session_id = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sources" not in st.session_state:
    st.session_state.sources = []

# Layout: Chat on left, Documents on right
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Chat")
    
    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # User input
    if prompt := st.chat_input("Ask about EBLA documents..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Process with RAG
        db = SessionLocal()
        try:
            chat_request = ChatRequest(
                query=prompt,
                session_id=st.session_state.session_id,
                collection_name=settings.default_collection_name,
                top_k=settings.default_top_k,
            )
            
            rag_service = RAGService(db)
            response = rag_service.process_chat(chat_request)
            
            st.session_state.session_id = response.session_id
            st.session_state.sources = response.sources
            
            # Add bot response
            st.session_state.messages.append({"role": "assistant", "content": response.answer})
        
        finally:
            db.close()
        
        st.rerun()  

with col2:
    st.subheader("📚 Retrieved Documents")
    
    if st.session_state.sources:
        for idx, src in enumerate(st.session_state.sources, start=1):
            with st.expander(f"📄 Doc {idx} (Score: {src.score:.4f})"):
                st.caption(f"**Source:** {src.metadata.get('source', 'Unknown')}")
                st.text(src.content[:500])  # First 500 characters
    else:
        st.info("Ask a question to see documents!")
    
    # Show session ID
    if st.session_state.session_id:
        st.caption(f"**Session ID:** `{st.session_state.session_id}`")