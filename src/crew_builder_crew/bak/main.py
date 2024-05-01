from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process

from tasks import CrewBuilderTasks
from agents import CrewBuilderAgents

tasks = CrewBuilderTasks()
agents = CrewBuilderAgents()

print("## Welcome to the Crew Builder Crew")
print('-------------------------------')
new_crew_purpose = input("What is the purpose of the crew you want to build?\n")
new_crew_details = input("Describe in detail the intended output of the crew.\n")

# Create Agents
research_assistant_agent = agents.research_assistant_agent()
general_manager_agent = agents.general_manager_agent()
senior_tool_expert_agent = agents.senior_tool_expert_agent()
senior_llm_expert_agent = agents.senior_llm_expert_agent()
crewai_expert_agent = agents.crewai_expert_agent()
senior_qa_engineer_agent = agents.senior_qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# Create Tasks
roles_and_goals_task = tasks.roles_and_goals_task(general_manager_agent, new_crew_purpose, new_crew_details)
optimal_tools_task = tasks.optimal_tools_task(senior_tool_expert_agent, new_crew_purpose, new_crew_details)
optimal_models_task = tasks.optimal_models_task(senior_llm_expert_agent, new_crew_purpose, new_crew_details)
craft_crewai_code_task = tasks.craft_crewai_code_task(crewai_expert_agent, new_crew_purpose, new_crew_details)
code_review_task = tasks.craft_crewai_code_task(senior_qa_engineer_agent, new_crew_purpose, new_crew_details)
code_evaluate_task = tasks.craft_crewai_code_task(chief_qa_engineer_agent, new_crew_purpose, new_crew_details)

# Create Crew responsible for building the new crew
crew_builder_crew = Crew(
	agents=[
		general_manager_agent,
		crewai_expert_agent,
		senior_llm_expert_agent,
		senior_tool_expert_agent,
		research_assistant_agent,
		senior_qa_engineer_agent,
		chief_qa_engineer_agent
	],
	tasks=[
		roles_and_goals_task,
		optimal_tools_task,
		optimal_models_task,
		craft_crewai_code_task,
		code_review_task,
		code_evaluate_task
	],
    process=Process.hierarchical,  # Optional: Sequential task execution is default
    memory=True,
    cache=True,
	verbose=True
)

crew_builder = crew_builder_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print(crew_builder)
