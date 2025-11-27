from vertexai.generative_models import FunctionDeclaration

# 1. The Actual Python Function
def search_news_func(query: str):
    """Mock function to simulate Google Search."""
    print(f"   [Tool Execution] Searching Google for: {query}...")
    return [
        "TechCorp announces new AI features.",
        "TechCorp CEO discusses pricing strategy in Q3.",
        "Competitors worry about TechCorp's market dominance."
    ]

# 2. The Tool Definition for Gemini
search_tool_decl = FunctionDeclaration(
    name="search_news",
    description="Search Google for recent news headlines.",
    parameters={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The search query"}
        },
        "required": ["query"]
    },
)