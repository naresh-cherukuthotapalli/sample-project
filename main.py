from fastapi import FastAPI
from schemas.workflow_schema import Workflow
from agents.executor import execute_workflow
from dotenv import load_dotenv
import os

# Initialize FastAPI app
app = FastAPI(title="PromptForge")

# Load environment variables from .env file
load_dotenv()

# Optional: Preload email credentials (not mandatory here anymore)
EMAIL_USERNAME = os.getenv("EMAIL_USER")       # Corrected key
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")       # Corrected key

# Route to run workflow
@app.post("/run-workflow")
def run_workflow(workflow: Workflow):
    result = execute_workflow(workflow)
    return {"results": result}
