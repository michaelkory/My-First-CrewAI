from crewai import Task
from textwrap import dedent

class CrewBuilderTasks:
	def roles_and_goals_task(self, agent, new_crew_purpose, new_crew_details):
		return Task(
			description=dedent(f"""\
                **Task: Define Roles, Goals, and Backstories for a New Crew**

                Analyze the given crew purpose and details to create a well-structured team with clear roles, goals, and backstories.

                **Step-by-Step Instructions:**

                1. **Analyze Crew Purpose**: {new_crew_purpose}
                    * Identify key objectives and requirements
                    * Determine necessary agent functionalities and expertise

                2. **Analyze Output Details**: {new_crew_details}
                    * Identify specific functionalities, tools, and processes needed
                    * Consider how these requirements influence agent roles and goals

                3. **Define Agent Roles and Goals**:
                    * Create distinct roles based on identified requirements and functionalities
                    * Specify skills, expertise, and responsibilities for each role
                    * Ensure clear delineation of duties and minimal overlap between roles
                    * Establish specific goals and KPIs for each role aligned with the crew purpose

                4. **Develop Agent Backstories**:
                    * Create relevant past experiences and backgrounds fitting assigned roles
                    * Highlight skills, achievements, and characteristics enhancing agent suitability
                    * Ensure backstories provide context and depth to agents' capabilities

                5. **Evaluate and Refine Team Structure**:
                    * Assess potential gaps or overlaps in roles and responsibilities
                    * Make necessary adjustments to optimize team structure and collaboration
                    * Incorporate feedback mechanisms for continuous improvement and adaptation

                6. **Document Team Structure**:
                    * Clearly outline each agent's role, goals, backstory, and KPIs
                    * Emphasize team dynamics, interaction, and expected contributions from each agent
                    * Ensure the document is well-organized, clear, and easily understandable

                **Expected Output:**
                A comprehensive document presenting well-defined roles, goals, and backstories for each agent, focusing on effective team collaboration and alignment with the crew purpose and required functionalities.
                """),
            expected_output="A comprehensive document outlining each new agent's role, goal, and backstory, with an emphasis on team dynamics and technology integration.",
            agent=agent
        )

	def optimal_tools_task(self, agent, new_crew_purpose, new_crew_details):
		return Task(
            description=dedent(f"""\
                **Task: Identify Optimal Tools for New Agents**

                **Objective:** Select the best tools from CrewAI and LangChain to support the new agents in achieving the crew's purpose and output requirements.

                **Step-by-Step Instructions:**

                1. **Analyze Crew Purpose**: {new_crew_purpose}
                    * Understand how the purpose influences technological needs and tool functionalities required

                2. **Analyze Output Details**: {new_crew_details}
                    * Identify specific outputs expected and technical capabilities needed to achieve them

                3. **Evaluate and Select Tools**:
                    * Assess tools based on performance metrics, ease of integration, scalability, and customization support
                    * Determine compatibility with existing technology stack and potential for future upgrades or expansion
                    * Evaluate learning curve and impact on project timeline and agent productivity

                4. **Justify Tool Selection**:
                    * Provide a detailed justification for each selected tool, including its features, cost-effectiveness, and alignment with crew purpose and output requirements
                    * Analyze potential limitations or risks associated with each tool and propose mitigation strategies

                5. **Compile Tool List**:
                    * Create a comprehensive list of tools for each agent, including detailed explanations for their selection
                    * Ensure all tools collectively enhance the crew's functionality and efficiency

                **Expected Output:**
                A detailed report listing all selected tools for each agent, including justifications for each choice, potential limitations, and mitigation strategies.
                """),
            expected_output="A detailed report listing all selected tools for each agent, including justifications for each choice, potential limitations, and mitigation strategies.",
            agent=agent
		)

	def optimal_models_task(self, agent, new_crew_purpose, new_crew_details):
		return Task(
            description=dedent(f"""\
                Analyze the given crew purpose: {new_crew_purpose}.
                Consider how the purpose influences the technological needs and functionalities required. Reflect on how different LLMs might enhance or limit achieving these purposes.

                Analyze the details about the intended output of the crew: {new_crew_details}.
                Understand the specific outputs expected and the technical capabilities needed to achieve these outputs. Map these requirements to the features of various LLMs.

                Evaluate and select the optimal LLM for each new agent, considering:
                - Cost-effectiveness in the context of the project's budget and duration.
                - Performance metrics relevant to the specific tasks, such as processing speed, accuracy, and reliability.
                - Feature set compatibility with the crew’s purpose, especially focusing on any specialized features that might be particularly beneficial.
                - Ease of integration with existing systems and scalability potential to accommodate future expansions.
                - Vendor support and community activity to ensure ongoing updates and problem-solving resources are available.

                For each chosen LLM, provide:
                - A detailed justification for its selection, linking back to how it meets the crew's purpose and intended outputs.
                - An assessment of any potential challenges or limitations in using the selected LLM and strategies to mitigate these challenges.

                Compile a comprehensive report detailing the chosen LLMs for each agent, including justifications for each choice and any anticipated challenges with suggested mitigation strategies.
                """),
            expected_output="A detailed report listing all selected LLMs for each agent, including justifications for each choice, an analysis of potential challenges, and mitigation strategies.",
            agent=agent
		)

	def craft_crewai_code_task(self, agent, new_crew_purpose, new_crew_details):
		return Task(
			description=dedent(f"""\
                Analyze the given crew purpose: {new_crew_purpose}.
                Consider how this purpose translates into specific technological functionalities and system requirements.

                Analyze the details about the intended output of the crew: {new_crew_details}.
                Detail the capabilities and processes necessary to achieve these outputs and how they can be facilitated by software.

                Craft Python code to optimize the attributes and tools for the new agents, ensuring peak performance by:
                - Creating a clear and modular code structure where each module aligns with specific crew functionalities.
                - Implementing classes and functions that encapsulate the behavior and properties of different agents and tools.
                - Using efficient data structures and algorithms to ensure that the system operates optimally under different operational conditions.
                - Incorporating error handling and data validation to ensure the robustness and reliability of the code.
                - Adding comments and documentation within the code to explain the purpose of modules, classes, functions, and key operations.
                - Considering integration points for future expansions or modifications to ensure the system remains adaptable and scalable.

                Your final submission should be the complete Python code, and only the python code, meticulously structured and documented.
                """),
            expected_output="Python scripts for agent optimization, fully documented and ready for implementation.",
            agent=agent
		)

	def code_review_task(self, agent, new_crew_purpose, new_crew_details):
		return Task(
			description=dedent(f"""\
                You are helping build a crew using crewai and python.
				
                Analyze the given crew purpose: {new_crew_purpose}.
                Consider how this purpose translates into specific technological functionalities and system requirements.

                Analyze the details about the intended output of the crew: {new_crew_details}.
                Detail the capabilities and processes necessary to achieve these outputs and how they can be facilitated by software.

                Instructions
                ------------

                Using the code you got, check for errors. Check for logic errors, syntax errors, 
				missing imports, variable declarations, mismatched brackets, and security vulnerabilities.

                Your Final answer must be the full python code, only the python code and nothing else.
                """),
			agent=agent
		)

	def code_evaluate_task(self, agent, new_crew_purpose, new_crew_details):
		return Task(
			description=dedent(f"""\
                You are helping build a crew using crewai and python.
				
                Analyze the given crew purpose: {new_crew_purpose}.
                Consider how this purpose translates into specific technological functionalities and system requirements.

                Analyze the details about the intended output of the crew: {new_crew_details}.
                Detail the capabilities and processes necessary to achieve these outputs and how they can be facilitated by software.

                Instructions
                ------------

                You will look over the code to insure that it is complete and does the job that it is supposed to do.

                Your Final answer must be the full python code, only the python code and nothing else.
                """),
			agent=agent
		)