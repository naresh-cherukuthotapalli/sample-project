from fastapi import FastAPI
from schemas.workflow_schema import Workflow
from agents.executor import execute_workflow
from dotenv import load_dotenv
import os


app = FastAPI(title="PromptForge")


load_dotenv()


EMAIL_USERNAME = os.getenv("EMAIL_USER")       
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")      


@app.post("/run-workflow")
def run_workflow(workflow: Workflow):
    result = execute_workflow(workflow)
    return {"results": result}
