from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI

# Set gemini pro as llm
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose = False,
                             temperature = 0.5,
                             google_api_key="AIzaSyC2nfQvZ5aUWt6CCRY-93eifxMNTVpfgLg")

htmlExpert = Agent(
    role='Senior HTML Developer',
    goal='Write only html (without CSS) code for the following topic : handling a digital library',
    verbose=False,
    memory=False,
    backstory=(
        "Driven by your expertise in html coding, you're at the forefront of "
        "innovation, eager to write different creative and advanced html templates for "
        "a perfect user experience."
    ),
    llm=llm,  # Use GenerativeModel from Google Generative AI
    allow_delegation=False
)

cssExpert = Agent(
    role='Senior CSS Developer',
    goal ='Generate a CSS file for a given HTML template for a perfect user interface and experience',
    verbose =False,
    memory=False,
    backstory=(
        "Driven by your expertise in CSS coding and your passion for art, you're at the forefront of "
        "innovation, eager to personalize an HTML template with creative and advanced user interface designs "
        "for a perfect user experience."
    ),
    llm=llm,
    allow_delegation=False
)
# Define Tasks
htmlTask = Task(
    description=(
        "Create an HTML template for the homepage of a digital library. "
        "The template should include sections for a search bar, featured books, "
        "new arrivals, and user login. Ensure the design is responsive and visually appealing."
    ),
    expected_output='An HTML file named "homepage.html" with a well-structured layout.',
    agent=htmlExpert,
)
cssTask = Task(
    description=(
        "Generate the CSS file for the HTML template created by htmlExpert to enhance user interface and experience. "
        "Ensure the CSS styling aligns with modern design principles and usability standards."
    ),
    expected_output='the HTML template gived by the HTMLExpert and a CSS file named style.css with improved user interface and experience.',
    agent=cssExpert,
)

# Define Crew
crew = Crew(
    agents=[htmlExpert, cssExpert],
    tasks=[htmlTask, cssTask],
    process=Process.sequential  # Sequential execution of tasks
)

# Kick off the crew and execute the tasks
result = crew.kickoff()
print(result)