from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import MyTool
# Initialize the LLM with Google Generative AI
def initialize_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        verbose=False,
        temperature=0.5,
        google_api_key="AIzaSyC2nfQvZ5aUWt6CCRY-93eifxMNTVpfgLg"
        )
tool = MyTool.MyTool()
# Initialize the agents
def create_agents(llm, tool):
    html_expert = Agent(
        role='Senior HTML Developer',
        goal='Write only HTML (without CSS) code for the following topic: handling a digital library',
        verbose=False,
        memory=False,
        backstory=(
            "Driven by your expertise in HTML coding, you're at the forefront of "
            "innovation, eager to write different creative and advanced HTML templates for "
            "a perfect user experience."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[tool]
    )

    css_expert = Agent(
        role='Senior CSS Developer',
        goal='Generate a CSS file for a given HTML template for a perfect user interface and experience',
        verbose=False,
        memory=True,
        backstory=(
            "Driven by your expertise in CSS coding and your passion for art, you're at the forefront of "
            "innovation, eager to personalize an HTML template with creative and advanced user interface designs "
            "for a perfect user experience."
        ),
        llm=llm,
        allow_delegation=False,
        tools=[tool]
    )

    return html_expert, css_expert

# Define the tasks
def create_tasks(html_expert, css_expert):
    html_task = Task(
        description=(
            "Create an HTML template for the homepage of a digital library. "
            "The template should include sections for a search bar, featured books, "
            "The template should include the link of css file that will be created by css_expert"
            "new arrivals, and user login. Ensure the design is responsive and visually appealing. "
            "Save the template as 'homepage.html' in the '/home/riane/CollectiveIntelligence/Project1/' directory."
        ),
        expected_output='/home/riane/CollectiveIntelligence/Project1/homepage.html',
        agent=html_expert,
    )

    css_task = Task(
        description=(
            "Generate the CSS file for the HTML template created by htmlExpert to enhance user interface and experience. "
            "Ensure the CSS styling aligns with modern design principles and usability standards. "
            "Save the CSS file as 'style.css' in the '/home/riane/CollectiveIntelligence/Project1/' directory."
        ),
        expected_output='/home/riane/CollectiveIntelligence/Project1/style.css',
        agent=css_expert,
    )

    return html_task, css_task

# Initialize the crew
def initialize_crew(agents, tasks):
    return Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential
    )


