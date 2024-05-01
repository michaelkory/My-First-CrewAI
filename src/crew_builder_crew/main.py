from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process

from llms import CrewBuilderLLMs
from tasks import CrewBuilderTasks
from agents import CrewBuilderAgents

llms = CrewBuilderLLMs()
tasks = CrewBuilderTasks()
agents = CrewBuilderAgents()
    
# Create Agents
crewai_crew_expert_agent = agents.crewai_crew_expert_agent(llms.claude)
crewai_qa_engineer_agent = agents.crewai_qa_engineer_agent(llms.g_llama3)

with open('src/crew_builder_crew/examples/task_list.yaml', 'r') as file:
    task_list_example = file.read()

with open('src/crew_builder_crew/examples/agent_list.yaml', 'r') as file:
    agent_list_example = file.read()

with open('src/crew_builder_crew/examples/tasks.py', 'r') as file:
    tasks_class_example = file.read()

with open('src/crew_builder_crew/examples/agents.py', 'r') as file:
    agents_class_example = file.read()

with open('src/crew_builder_crew/examples/main.py', 'r') as file:
    main_py_example = file.read()

print("## Welcome to the Crew Builder Crew")
print('-------------------------------')
# new_crew_purpose = input("What is the purpose of the crew you want to build?\n")
# new_crew_details = input("Describe in detail the intended output of the crew.\n")
new_crew_purpose = 'build a new crew builder crew',
new_crew_details = 'build the most excellent crewai crew for building crewai crews'

# Create Tasks
create_task_list_task = tasks.create_task_list_task(
    crewai_crew_expert_agent, 
    new_crew_purpose, new_crew_details, 
    task_list_example)

review_task_list_task = tasks.review_task_list_task(
    crewai_qa_engineer_agent,
    [create_task_list_task],
    new_crew_purpose, new_crew_details, 
    task_list_example)

create_agent_list_task = tasks.create_agent_list_task(
    crewai_crew_expert_agent, 
    new_crew_purpose, new_crew_details, 
    agent_list_example)

review_agent_list_task = tasks.review_agent_list_task(
    crewai_qa_engineer_agent,
	[review_task_list_task,create_agent_list_task],
    new_crew_purpose, new_crew_details, 
    agent_list_example)

create_tasks_task = tasks.create_tasks_task(
    crewai_crew_expert_agent, 
    [review_task_list_task],
    new_crew_purpose, new_crew_details, 
    tasks_class_example)

review_tasks_task = tasks.review_tasks_task(
    crewai_qa_engineer_agent, 
    [review_task_list_task,create_tasks_task],
    new_crew_purpose, new_crew_details, 
    tasks_class_example)

create_agents_task = tasks.create_agents_task(
    crewai_crew_expert_agent, 
    [review_agent_list_task],
    new_crew_purpose, new_crew_details, 
    agents_class_example)

review_agents_task = tasks.review_agents_task(
    crewai_qa_engineer_agent, 
    [review_agent_list_task,create_agents_task],
    new_crew_purpose, new_crew_details, 
    agents_class_example)

create_main_py_task = tasks.create_main_py_task(
    crewai_crew_expert_agent, 
    [review_task_list_task,review_agent_list_task],
    new_crew_purpose, new_crew_details, 
    main_py_example)

review_main_py_task = tasks.review_main_py_task(
    crewai_qa_engineer_agent, 
    [review_task_list_task,review_agent_list_task,create_main_py_task],
    new_crew_purpose, new_crew_details, 
    main_py_example)

# Create Crew
crew_builder_crew = Crew(
	agents=[
		crewai_crew_expert_agent,
		crewai_qa_engineer_agent
	],
	tasks=[
        create_task_list_task,review_task_list_task,
        create_agent_list_task,review_agent_list_task,
		create_tasks_task,review_tasks_task,
		create_agents_task,review_agents_task,
		create_main_py_task,review_main_py_task
	],
    process=Process.sequential,
	manager_llm = llms.g_llama3,
	verbose=2,
	max_rpm=2,
    memory=True,
    cache=True
)

crew_builder = crew_builder_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print(crew_builder)