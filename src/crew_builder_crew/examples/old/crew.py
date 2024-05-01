# crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq

@CrewBase
## Begin the class defintion here. 
## Replace "InsertNameOfCrew" with the class name in CamelCase.
## Replace "Insert Name Of Crew" with the class name.

class InsertNameOfCrew():
    """Insert Name Of Crew"""

## Create the agents_config and tasks_config structures.

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
## Create the LLM to use for all agents.
## let's stick with groq_llm because it's free.

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=1, model_name="llama3-70b-8192")

# Define the agent names here.
## Use a name that indicates the agent's role.
## Use "_" in lieu of spaces, and always with "_agent".

    @agent
    def name_of_the_first_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['name_of_the_first_agent'],
            llm = self.groq_llm,
        )

    @agent
    def name_of_the_next_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['name_of_the_next_agent'],
            llm = self.groq_llm,
        )
    
## continue defining the agent names as needed.

## Define the task names here.
## Use a name the indicates the task's purpose.
## Use "_" in lieu of spaces, and always with "_task".
## Assign the agent that is intended to complete each task.

    @task
    def name_of_the_first_task(self) -> Task:
        return Task(
            config = self.tasks_config['name_of_the_first_task'],
            agent = self.name_of_the_first_agent()
        )

    @task
    def name_of_the_next_task(self) -> Task:
        return Task(
            config = self.tasks_config['name_of_the_next_task'],
            agent = self.name_of_the_next_agent()
        )
    
## continue defining the task names as needed.
    
    @crew
    def crew(self) -> Crew:

## Replace "Insert Name Of Crew" with the name of the crew.

        """Creates the Insert Name Of Crew"""

## return the Crew with agents, tasks, and other attributes.
## the @agent and @task decorators all use to use self.agents and self.tasks.
## there is no need to use an array of agents and an array of tasks here!!
## this section is perfect the way it is!!

        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            manager_llm = self.groq_llm,
            verbose = 2,
            max_rpm = 10
        )