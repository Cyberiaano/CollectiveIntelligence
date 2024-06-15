import yaml
from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq 
@CrewBase
class FinancialAnalystCrew():
    agents_config_path = '/home/riane/CollectiveIntelligence/Project3/src/financial_analyst_crew/config/agents.yaml'
    tasks_config_path = '/home/riane/CollectiveIntelligence/Project3/src/financial_analyst_crew/config/tasks.yaml'

    def __init__(self) -> None:
        self.llm = ChatGroq(
            model_name="mixtral-8x7b-32768",
            temperature=0,
            groq_api_key= "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"
        )
        # Load YAML configuration files
        with open(self.agents_config_path, 'r') as f:
            self.agents_config = yaml.safe_load(f)
        with open(self.tasks_config_path, 'r') as f:
            self.tasks_config = yaml.safe_load(f)

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],
            llm=self.llm
        )

    @agent
    def company_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['company_analyst'],
            llm=self.llm
        )

    @task
    def research_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_company_task'],
            agent=self.company_researcher()
        )

    @task
    def analyze_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_company_task'],
            agent=self.company_analyst()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.company_researcher(), self.company_analyst()],
            tasks=[self.research_company_task(), self.analyze_company_task()],
            process=Process.sequential,
            verbose=2
        )
