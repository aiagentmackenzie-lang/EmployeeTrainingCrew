import os
import sys
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai_tools import FileReadTool, WebsiteSearchTool, SerperDevTool  # Import the tools

# Load API keys from environment variables
# Set these in your environment before running:
# export OPENAI_API_KEY="your-key-here"
# export SERPER_API_KEY="your-key-here"
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY", "")

# Verify API keys are set
if not os.environ["OPENAI_API_KEY"]:
    raise ValueError("OPENAI_API_KEY environment variable not set")
if not os.environ["SERPER_API_KEY"]:
    raise ValueError("SERPER_API_KEY environment variable not set")

# Define tools
file_read_tool = FileReadTool(file_path='memory.txt')  # Use FileReadTool to read from a memory file
website_search_tool = WebsiteSearchTool()  # Use WebsiteSearchTool to gather info from websites
serper_tool = SerperDevTool()  # Use SerperDevTool for web-based research

# Define the Knowledge Specialist agent with the FileReadTool
knowledge_specialist = Agent(
    role='Senior Knowledge and Learning Specialist',
    goal='Deliver comprehensive and precise information directly to employees, leveraging the company\'s extensive knowledge base.',
    backstory="An expert in company policies, training resources, and history.",
    llm=ChatOpenAI(model_name="gpt-4o-mini"),  # Updated to use gpt-4o-mini
    verbose=True,
    memory=True,
    tools=[file_read_tool]  # Add the file read tool
)

# Define the Web Researcher agent that uses SerperDevTool for topic research
web_researcher = Agent(
    role='Web Researcher',
    goal='Find relevant online resources and articles related to the training topic {topic}.',
    backstory="A digital detective that specializes in gathering up-to-date information from the internet to support training needs.",
    llm=ChatOpenAI(model_name="gpt-4o-mini"),  # Updated to use gpt-4o-mini
    verbose=True,
    tools=[serper_tool]  # Add the SerperDevTool for web research
)

# Define the Training Developer agent with the WebsiteSearchTool
training_developer = Agent(
    role='Lead Instructional Designer and Training Specialist',
    goal='Create and enhance training materials based on specific employee queries and company standards.',
    backstory="A skilled instructional designer specializing in creating detailed training programs aligned with company standards.",
    llm=ChatOpenAI(model_name="gpt-4o-mini"),  # Updated to use gpt-4o-mini
    verbose=True,
    memory=True,
    tools=[website_search_tool]  # Add the website search tool
)

# Define the Head of HR agent with both SerperDevTool and FileReadTool
head_of_hr = Agent(
    role='Head of HR',
    goal=(
        'Define tasks and responsibilities for employees, ensuring they are aligned with the company\'s '
        'values, code of conduct, and the importance of employee training. Additionally, provide instructions to contact '
        'Raphael Main for further training or assistance.'
    ),
    backstory="A highly experienced HR leader, responsible for ensuring all employees understand their responsibilities and uphold the company values.",
    llm=ChatOpenAI(model_name="gpt-4o-mini"),  # Using the same model for consistency
    verbose=True,
    memory=True,
    tools=[serper_tool, file_read_tool]  # Added SerperDevTool and FileReadTool
)

# Define the tasks
knowledge_task = Task(
    description="Provide in-depth guidance to employees in the {department} regarding their role as a {position}, focusing on {topic} in accordance with Innovelle's practices.",
    expected_output="A detailed response providing actionable insights on {topic}, tailored to the employee’s department and role.",
    agent=knowledge_specialist
)

# Task for web researcher to find additional training resources related to {topic}
web_research_task = Task(
    description="Conduct a web search and gather online resources related to {topic} to supplement the training materials.",
    expected_output="A list of online resources and articles about {topic}.",
    agent=web_researcher,
    output_file="web_research_resources.md"  # Output will be saved to web_research_resources.md
)

# Training material task output will be saved to training_materials.md
training_material_task = Task(
    description="Create comprehensive training materials for employees in the {department} regarding their role as a {position}, emphasizing {topic}.",
    expected_output="Engaging and practical training documents tailored to Innovelle's best practices and standards.",
    agent=training_developer,
    output_file="training_materials.md"  # Output will be saved to training_materials.md
)

# Task for Head of HR agent to outline responsibilities and generate a report in markdown
hr_task = Task(
    description=(
        "Assign tasks and responsibilities to employees in the {department} regarding their role as a {position}. "
        "Additionally, provide instructions to contact Raphael Main for training and further assistance. "
        "Ensure to represent the values of Innovelle UK Ltd, its code of conduct, and highlight the importance of employee training."
    ),
    expected_output=(
        "A markdown report outlining employee responsibilities, "
        "the company values, code of conduct, "
        "and directions to contact Raphael Main for further assistance."
    ),
    agent=head_of_hr,
    output_file="hr_report.md"  # Output will be saved to hr_report.md
)

# Define the crew with the new Head of HR agent added
training_crew = Crew(
    agents=[knowledge_specialist, web_researcher, training_developer, head_of_hr],  # Added the Head of HR agent
    tasks=[knowledge_task, web_research_task, training_material_task, hr_task],  # Added the HR task
    verbose=True
)

# Kickoff the crew process with inputs for department, position, and topic
try:
    inputs = {'department': "Software", 'position': "AI Agent Developer", 'topic': "CrewAI agent training"}
    result = training_crew.kickoff(inputs=inputs)

except KeyError as e:
    print(f"An error occurred: Task output not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
