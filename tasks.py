from crewai import Task

def create_tasks(research_agent, writer_agent):

    research_task = Task(
    description=(
        "Use ONLY the provided Serper search tool to find latest information about {topic}. "
        "Do NOT use any other tool names like brave_search or browser. "
        "Return key insights with examples."
    ),
    agent=research_agent,
    expected_output="Latest insights with examples"
    )

    writing_task = Task(
        description=(
            "Convert the research on {topic} into structured format: "
        ),
        agent=writer_agent,
        expected_output="Well-structured explanation"
    )

    return [research_task, writing_task]