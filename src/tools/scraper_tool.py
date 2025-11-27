from vertexai.generative_models import FunctionDeclaration

# 1. The Actual Python Function (Mock Logic for stability)
def get_competitor_price_func(url: str):
    """Mock function to simulate scraping a website."""
    # In real life: Use requests.get(url) here
    print(f"   [Tool Execution] Scraping {url}...")
    return {
        "price": "$200", 
        "currency": "USD", 
        "in_stock": True,
        "promo": "Summer Sale"
    }

# 2. The Tool Definition for Gemini
scraper_tool_decl = FunctionDeclaration(
    name="get_competitor_price",
    description="Fetch the current price and stock status from a competitor URL.",
    parameters={
        "type": "object",
        "properties": {
            "url": {"type": "string", "description": "The URL to scrape"}
        },
        "required": ["url"]
    },
)