# Employee Training Crew - Onboarding

## Overview
This project implements an automated system using CrewAI for the onboarding and training of Web Developers in the Software department. The system utilizes a combination of agents, including a **Senior Knowledge and Learning Specialist** and a **Lead Instructional Designer and Training Specialist**, to deliver comprehensive training materials tailored to professional standards and practices.

---

## Project Structure

```text
EmployeeTrainingCrew/
├── env/                         # Virtual environment directory
├── memory_file.text             # Memory data file containing training information
├── main.py                      # Main script to execute the training crew process
├── final_knowledge_response.txt  # Output: Knowledge specialist's guidance
├── final_training_materials.txt  # Output: Detailed training materials
└── README.md                    # This README file

Requirements
Python: 3.7 or higher

Packages: CrewAI, OpenAI, and dependencies listed in requirements.txt

Setup Instructions
1. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:

Bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
2. Install Required Packages

Bash
pip install -r requirements.txt
3. Set Environment Variables
Set your OpenAI API key to enable the language model interactions:

Bash
export OPENAI_API_KEY="your_openai_api_key"   # On Windows, use `set OPENAI_API_KEY=your_openai_api_key`
4. Prepare Memory Data File
Ensure that memory_file.text contains all the necessary information for the onboarding process. This file serves as the primary data source for the agents.

Usage Instructions
Run the Main Script

Execute the script to initiate the agents and process the tasks:

Bash
python main.py
Outputs

The script will generate two primary output files:

final_knowledge_response.txt: Contains comprehensive guidance from the Senior Knowledge and Learning Specialist.

final_training_materials.txt: Contains the structured training modules created by the Instructional Designer.

Error Handling
Memory File Not Found: The script will exit if memory_file.text is missing.

Empty Memory Data: If the source file contains no data, the process will terminate with an error message.

Task Output Errors: Any issues accessing specific task results will be logged while the script attempts to complete remaining processes.

Contributions
Contributions to this project are welcome. Please ensure that any additions align with modern web development training standards.

License
This project is licensed under the MIT License.

Contact Information
For further information or assistance, please contact the project maintainer at:
aiagent.mackenzie@gmail.com
