# agents.py

from textwrap import dedent
from crewai import Agent

# *update the name of the new class using CamelCase*
class NewCrewAgents:

	def name_of_the_first_agent(self, llm):
		return Agent(
            role=dedent("""\
                *provide the role of the agent here*
				"""),
			goal=dedent("""\
				1. *provide the primary goal of the agent here*
				2. *provide the secondary goal of the agent here*
				"""),
			backstory=dedent("""\
                *provide the backstory of the agent here*
				"""),
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm,
        )

	def name_of_the_second_agent(self, llm):
		return Agent(
            role=dedent("""\
                *provide the role of the agent here*
				"""),
			goal=dedent("""\
				1. *provide the primary goal of the agent here*
				2. *provide the secondary goal of the agent here*
				"""),
			backstory=dedent("""\
                *provide the backstory of the agent here*
				"""),
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm,
        )