import os
import sys
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# Set API key for OpenAI
os.environ["OPENAI_API_KEY"] = "sk-proj-Your-API-Key"

# Load memory data from the single file
memory_file_path = r'C:\Users\augus\EmployeeTrainingCrew\memory_file.text'
try:
    with open(memory_file_path, 'r') as file:
        memory_data = file.read()
    print("Memory data loaded successfully.")
except FileNotFoundError:
    print(f"Memory file not found at {memory_file_path}. Exiting.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while loading the memory file: {e}")
    sys.exit(1)

# Check if memory data is empty
if not memory_data.strip():
    print("Memory data is empty. Exiting.")
    sys.exit(1)

# Define the Knowledge Specialist agent
knowledge_specialist = Agent(
    role='Senior Knowledge and Learning Specialist',
    goal='Deliver comprehensive and precise information directly to employees, leveraging Innovelle\'s extensive knowledge base.',
    backstory="An expert in Innovelle's policies, training resources, and history.",
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True,
    memory=memory_data
)

# Define the Training Developer agent
training_developer = Agent(
    role='Lead Instructional Designer and Training Specialist',
    goal='Create and enhance training materials based on specific employee queries and Innovelle standards.',
    backstory="A skilled instructional designer specializing in creating detailed training programs.",
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    verbose=True,
    memory=memory_data
)

# Define the tasks
knowledge_task = Task(
    description="Provide in-depth guidance to employees in the {department} regarding their role as a {position}, focusing on {topic} in accordance with Innovelle's practices.",
    expected_output="A detailed response providing actionable insights on {topic}, tailored to the employee’s department and role.",
    agent=knowledge_specialist
)

training_material_task = Task(
    description="Create comprehensive training materials for employees in the {department} regarding their role as a {position}, emphasizing {topic}.",
    expected_output="Engaging and practical training documents tailored to Innovelle's best practices and standards.",
    agent=training_developer
)

# Define the crew
training_crew = Crew(
    agents=[knowledge_specialist, training_developer],
    tasks=[knowledge_task, training_material_task],
    verbose=True
)

# Kickoff the crew process with inputs for department, position, and topic
try:
    inputs = {'department': "Software", 'position': "Web Developer", 'topic': "In-depth onboarding"}
    result = training_crew.kickoff(inputs=inputs)

    # Process outputs directly from the result object
    try:
        # Extract the outputs from the task results
        knowledge_output = result['tasks'][0]['output']  # First task's output
        training_output = result['tasks'][1]['output']   # Second task's output

        print("Knowledge Task Output:", knowledge_output)
        print("Training Material Task Output:", training_output)

    except Exception as e:
        print(f"Error accessing outputs: {e}")

except KeyError as e:
    print(f"An error occurred: Task output not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
