from crewai import Agent,Task,Crew,Process
from crewai.project import CrewBase,agent,crew,task
from langchain_google_genai import ChatGoogleGenerativeAI

@CrewBase
class FinancialAnalystCrew():
    agents_config='config/agents.yaml'
    task_config= 'config/tasks.yaml'
    def __init__(self) -> None :
        self.llm=ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        verbose=False,
        temperature=0.5,
        google_api_key="AIzaSyC2nfQvZ5aUWt6CCRY-93eifxMNTVpfgLg"
        )
    @agent
    def company_researcher(self)-> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],
            llm=self.llm
        )
    @agent
    def company_analyst(self)-> Agent:
        return Agent(
            config=self.agents_config['company_analyst'],
            llm=self.llm
        )
    @task
    def  research_compant_task(self) -> Task :
        return Task(
            config=self.task_config['research_company_task'],
            agent=self.company_researcher()
        )
    @task
    def  analyze_compant_task(self) -> Task :
        return Task(
            config=self.task_config['analyze_company_task'],
            agent=self.company_analyst()
        )
    @crew
    def crew(self)-> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose=2
        )
    