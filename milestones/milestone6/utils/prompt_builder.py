"""Utility functions for building LLM prompts."""

from typing import List, Dict, Any


def build_summary_prompt(conversation_text: str) -> str:
    """
    Builds a prompt for summarizing a conversation.
    
    Args:
        conversation_text: The formatted conversation text
        
    Returns:
        The complete prompt for the LLM
    """
    return f"""Summarize the following conversation concisely in 2-3 sentences:

{conversation_text}

Summary:"""


def build_rag_prompt(query: str, context_docs: List[Dict[str, Any]], history_text: str) -> str:
    """
    Builds the RAG prompt with system instructions, history, context, and query.
    
    Args:
        query: User's question
        context_docs: List of context documents
        history_text: Formatted chat history
        
    Returns:
        The complete prompt for the LLM
    """
    context_str = "\n\n".join([f"Source {i+1}:\n{doc['content']}" for i, doc in enumerate(context_docs)])
    
    system_prompt = """You are an intelligent assistant for EBLA Computer Consultancy. 
Your goal is to answer user questions accurately based ONLY on the provided context.
If the answer is not in the context, say "I don't have enough information to answer that."

Instructions:
1. Use the provided Context to answer the question.
2. Use the Chat History to understand the conversation flow (e.g., if the user says "it", know what they refer to).
3. Be concise, professional, and helpful.
4. Do not hallucinate or make up information.
"""

    return f"""{system_prompt}

---
Chat History:
{history_text}
---

---
Context Information:
{context_str}
---

User Question: {query}

Answer:"""