import os
from dotenv import load_dotenv
import vertexai 

def setup_environment():
    load_dotenv()
    project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
    location = os.getenv("GOOGLE_CLOUD_REGION", "us-central1")
    
    if not project_id:
        raise ValueError("Please set GOOGLE_CLOUD_PROJECT in .env file")
        
    vertexai.init(project=project_id, location=location)
    
# Global Model Config
MODEL_NAME = "gemini-2.0-flash-001" # Fast and efficient for tools