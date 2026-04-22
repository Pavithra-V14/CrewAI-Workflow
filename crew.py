from crewai import Crew
from agents import create_agents
from tasks import create_tasks

def run():
    research_agent, writer_agent = create_agents()
    tasks = create_tasks(research_agent, writer_agent)
    crew = Crew(
        agents=[research_agent, writer_agent],
        tasks=tasks,
        verbose=False
    )
    result = crew.kickoff(
        inputs={"topic": "AI"}
    )
    print("\n-----------FINAL OUTPUT-----------\n")
    print(result)

if __name__ == "__main__":
    run()