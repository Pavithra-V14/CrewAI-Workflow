from crewai_tools import SerperDevTool

def get_search_tool():
    tool = SerperDevTool()
    tool.name = "search"   
    tool.n_results = 3
    return tool