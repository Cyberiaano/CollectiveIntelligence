from agents import initialize_crew,create_agents,create_tasks,initialize_llm
from MyTool import MyTool

# Main function to run the code
def main():
    llm = initialize_llm()
    tool = MyTool()

    html_expert, css_expert = create_agents(llm, tool)
    html_task, css_task = create_tasks(html_expert, css_expert)

    crew = initialize_crew([html_expert, css_expert], [html_task, css_task])
    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    main()
