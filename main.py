import os
import sys
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai_tools import FileReadTool, WebsiteSearchTool, SerperDevTool  # Import the tools

# Set API key for OpenAI and Serper
os.environ["OPENAI_API_KEY"] = "sk-gt1NTXK87AnCnuGW_kl7MmWgWDrvBOb_1c2Y13tZIXT3BlbkFJ_SUXB4rVV08ALM3cFJx7OqZvDlwH0Rv9aSrE5Q0tgA"
os.environ["SERPER_API_KEY"] = "d2fd408fadf55b44b304f7f61bff135d477b40e9"

# Define tools
file_read_tool = FileReadTool(file_path='memory.txt')  # Use FileReadTool to read from a memory file
website_search_tool = WebsiteSearchTool()  # Use WebsiteSearchTool to gather info from websites
serper_tool = SerperDevTool()  # Use SerperDevTool for web-based research

# Define the Knowledge Specialist agent with the FileReadTool
knowledge_specialist = Agent(
    role='Senior Knowledge and Learning Specialist',
    goal='Deliver comprehensive and precise information directly to employees, leveraging Innovelle\'s extensive knowledge base.',
    backstory="An expert in Innovelle's policies, training resources, and history.",
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True,
    memory=True,
    tools=[file_read_tool]  # Add the file read tool
)

# Define the Web Researcher agent that uses SerperDevTool for topic research
web_researcher = Agent(
    role='Web Researcher',
    goal='Find relevant online resources and articles related to the training topic {topic}.',
    backstory="A digital detective that specializes in gathering up-to-date information from the internet to support training needs.",
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True,
    tools=[serper_tool]  # Add the SerperDevTool for web research
)

# Define the Training Developer agent with the WebsiteSearchTool
training_developer = Agent(
    role='Lead Instructional Designer and Training Specialist',
    goal='Create and enhance training materials based on specific employee queries and Innovelle standards.',
    backstory="A skilled instructional designer specializing in creating detailed training programs.",
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True,
    memory=True,
    tools=[website_search_tool]  # Add the website search tool
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

# Define the crew with the new Web Researcher agent added
training_crew = Crew(
    agents=[knowledge_specialist, web_researcher, training_developer],  # Added the web_researcher agent
    tasks=[knowledge_task, web_research_task, training_material_task],  # Added the web_research_task
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
