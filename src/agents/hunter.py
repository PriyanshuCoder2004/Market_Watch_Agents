from vertexai.generative_models import GenerativeModel, Tool
from src.config import MODEL_NAME
from src.tools.scraper_tool import scraper_tool_decl, get_competitor_price_func
from src.tools.search_tool import search_tool_decl, search_news_func

class HunterAgent:
    def __init__(self):
        # Bind tools to the model
        self.tools = Tool(
            function_declarations=[scraper_tool_decl, search_tool_decl]
        )
        self.model = GenerativeModel(MODEL_NAME, tools=[self.tools])
        
        # Map function names to actual Python functions
        self.func_map = {
            "get_competitor_price": get_competitor_price_func,
            "search_news": search_news_func
        }

    def research(self, company: str, url: str):
        chat = self.model.start_chat()
        
        # Prompt designed to trigger tool usage
        prompt = f"Find the latest price for {company} from {url} and search for recent news about them."
        
        response = chat.send_message(prompt)
        
        # Handle Function Calling Loop
        # Note: Gemini returns a 'function_call' part if it wants to use a tool
        part = response.candidates[0].content.parts[0]
        
        results = {}
        
        # Simple handling for the first function call request (Sequential)
        if part.function_call:
            fn_name = part.function_call.name
            fn_args = part.function_call.args
            
            if fn_name in self.func_map:
                # Execute the tool
                tool_result = self.func_map[fn_name](**fn_args)
                results['tool_data'] = tool_result
                
                # In a full loop, you would feed this back to the model. 
                # For this demo, we just return the tool data directly.
                return tool_result
        
        # Fallback if no tool triggered
        return {"raw_text": response.text}