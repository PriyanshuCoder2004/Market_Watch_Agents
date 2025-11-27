from vertexai.generative_models import GenerativeModel
from src.config import MODEL_NAME

class AnalystAgent:
    def __init__(self):
        # Analyst doesn't need tools, just high reasoning capability
        self.model = GenerativeModel(MODEL_NAME)

    def write_report(self, company, current_data, historical_context):
        prompt = f"""
        You are a Senior Market Analyst. Write a brief executive summary for {company}.
        
        1. NEW DATA FOUND: {current_data}
        2. HISTORICAL CONTEXT: {historical_context if historical_context else "No history available."}
        
        Task:
        - Compare the new price/status to the history.
        - Highlight any changes (e.g., Price increase, new features).
        - If no history exists, establish this as the baseline.
        """
        
        response = self.model.generate_content(prompt)
        return response.text