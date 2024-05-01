# task.py

from textwrap import dedent
from crewai import Task

# *update the name of the new class using CamelCase*
class NewCrewTasks:

    def name_of_the_first_task(self, agent, crew_purpose, crew_details):
        return Task(
			description=dedent(f"""\
                # New CrewAI Crew: Step 1
                      
                *provide the summary of the task here*
                      
                ## Objective
                *provide the objective of the task here*
                      
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Provide detailed step-by-step instructions here.
                2. Break down complex tasks into indivdual steps

                ## Deliverable
                *provide the deliverable of the task here*
                """),
			agent=agent
        )

    def name_of_the_second_task(self, agent, crew_purpose, crew_details):
        return Task(
			description=dedent(f"""\
                # New CrewAI Crew: Step 2
                      
                *provide the summary of the task here*
                      
                ## Objective
                *provide the objective of the task here*
                      
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Provide detailed step-by-step instructions here.
                2. Break down complex tasks into indivdual steps

                ## Deliverable
                *provide the deliverable of the task here*
                """),
			agent=agent
        )