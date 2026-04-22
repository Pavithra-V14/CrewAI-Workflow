from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from tools import get_search_tool
load_dotenv()
def get_llm():
    return LLM(
        model="groq/llama-3.1-8b-instant",  
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.4,
        max_tokens=500
    )

def create_agents():
    llm = get_llm()
    search_tool = get_search_tool()
    research_agent = Agent(
        role="Real-Time Research Analyst",
        goal="Find latest and accurate information",
        backstory="Expert in web search and real-time data",
        tools=[search_tool],
        llm=llm,    
        verbose=False
    )
    writer_agent = Agent(
        role="Technical Writer",
        goal="Write structured explanations",
        backstory="Expert in documentation",
        llm=llm,
        verbose=True
    )
    return research_agent, writer_agent