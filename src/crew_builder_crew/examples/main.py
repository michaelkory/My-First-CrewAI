# main.py

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from langchain_anthropic import ChatAnthropic

claude_llm = ChatAnthropic(temperature=1, model='claude-3-haiku-20240307')

from tasks import CrewBuilderTasks
from agents import CrewBuilderAgents

tasks = CrewBuilderTasks()
agents = CrewBuilderAgents()

print("## Welcome to the Crew Builder Crew")
print('-------------------------------')
new_crew_purpose = '*new_crew_purpose goes here*',
new_crew_details = '*new_crew_details goes here*',
    
# Instantiate Agents defined in `agent_list.yaml` under the `# Create Agents` section.
# Create Agents
name_of_the_first_agent = agents.name_of_the_first_agent(claude_llm)
name_of_the_second_agent = agents.name_of_the_second_agent(claude_llm)

# Instantiate Tasks defined in `task_list.yaml` under the `# Create Tasks` section.
# Create Tasks
name_of_the_first_task = tasks.name_of_the_first_task(name_of_the_first_agent, new_crew_purpose, new_crew_details)
name_of_the_second_task = tasks.name_of_the_second_task(name_of_the_second_agent, new_crew_purpose, new_crew_details)

# Invoke each Agent and Task in the `# Create Crew` section.
# Provide the name of the new crew in lowercase, use "_" for spaces, always ending in "_crew".
# Create Crew
new_crew_crew = Crew(
	agents=[
		name_of_the_first_agent,
		name_of_the_second_agent
	],
	tasks=[
        name_of_the_first_task,
        name_of_the_second_task
	],
    process=Process.sequential,
    memory=True,
    cache=True,
	max_rpm=10,
	verbose=2
)

# Provide the name of the new crew in lowercase.
new_crew = new_crew_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print(new_crew)