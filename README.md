Employee Training Crew - Innovelle Onboarding

Overview

This project implements an automated system using CrewAI for the onboarding and training of Web Developers in the Software department at Innovelle. The system utilizes a combination of agents, including a Senior Knowledge and Learning Specialist and a Lead Instructional Designer and Training Specialist, to deliver comprehensive training and onboarding materials tailored to Innovelle's standards and practices.

Project Structure

EmployeeTrainingCrew/
├── env/                    # Virtual environment directory
├── memory_file.text        # Memory data file containing relevant training and onboarding information
├── main.py                 # Main script to execute the training crew process
├── final_knowledge_response.txt  # Output file for knowledge specialist's guidance
├── final_training_materials.txt  # Output file for training developer's materials
├── README.md               # This README file

Requirements

Python 3.7 or higher
Required Python packages (listed in requirements.txt or managed within a virtual environment)
Setup Instructions

Create a Virtual Environment:

It is recommended to create a virtual environment to manage dependencies for this project. You can create one using the following commands:


python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`

Install Required Packages:

After activating the virtual environment, install the required packages:


pip install -r requirements.txt

Set Environment Variables:

Make sure to set your OpenAI API key as an environment variable before running the script. This key is necessary for the language model interactions.


export OPENAI_API_KEY="your_openai_api_key"   # On Windows, use `set OPENAI_API_KEY=your_openai_api_key`
Prepare Memory Data File:

Ensure that memory_file.text contains all the necessary information for the training and onboarding process. This file serves as the primary data source for the agents.

Usage Instructions

Run the Main Script:

Execute the main script to start the training crew process. The script will load memory data, initiate the agents, and process the tasks.

python main.py
Outputs:

The script will generate two output files containing the results of the training process:

final_knowledge_response.txt: Contains the comprehensive guidance provided by the Senior Knowledge and Learning Specialist.
final_training_materials.txt: Contains the detailed training materials created by the Lead Instructional Designer and Training Specialist.
Error Handling

Memory File Not Found:

If the memory file (memory_file.text) is not found, the script will exit with an error message.
Empty Memory Data:

If the memory file is empty, the script will exit with an error message.

Task Output Errors:

If there are errors in accessing task outputs, they will be logged, and the script will continue to provide as much information as possible.

Contributions

Contributions to this project are welcome. Please ensure that any contributions align with Innovelle's training and onboarding standards.

License
This project is licensed under the MIT License.

Contact Information
For further information or assistance, please contact the project maintainer at email@example.com.