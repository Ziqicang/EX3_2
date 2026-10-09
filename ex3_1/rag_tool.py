### COMPLETE THE CODE  ###

from rag import retrieve

def rag_tool(query: str) -> str:
    """Retrieve relevant content from university IT policy documents"""
    return retrieve(query)
