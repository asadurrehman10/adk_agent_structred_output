from pydantic import BaseModel
from google.adk.agents.llm_agent import Agent

class Enquiry(BaseModel):
    name :str
    email:str
    intrested_in:str
    amount:int

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    output_schema= Enquiry
)
