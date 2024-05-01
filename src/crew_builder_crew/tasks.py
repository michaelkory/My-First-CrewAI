from crewai import Task
from textwrap import dedent

class CrewBuilderTasks:
    def __init__(self):
        self.task_outputs = {}  # Dictionary to store task outputs by name

    def create_task_list_task(self, agent, crew_purpose, crew_details, task_list_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 1

                You are a **CrewAI Crew Expert Engineer** and this is the first step in creating a *NEW* CrewAI Crew.

                ## Objective
                Your first task is to provide a list of tasks to fulfill the Crew Purpose and Crew Details.
                      
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Analyze the given Crew Purpose and Crew Details to determine the required tasks.
                2. Think carefully about the Crew Purpose and Crew Details to sequence the tasks logically.
                3. Create a `task_list.yaml` file that contains the name of each task and a concise summary.

                **Your final answer should be the complete `task_list.yaml` file, and only the `task_list.yaml` file.**
                """),
            expected_output=task_list_example,
			agent=agent
        )
        # self.task_outputs['create_task_list_task'] = task.execute()
        return task

    def review_task_list_task(self, agent, context, crew_purpose, crew_details, task_list_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 2
                      
                You are a **Software Quality Control Engineer** and this is the second step in creating a *NEW* CrewAI Crew.
                      
                ## Objective
                Your task is to carefully review the provided list of tasks designed to fulfill the Crew Purpose and Crew Details.
                      
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Analyze the given Crew Purpose and Crew Details to determine if the provided tasks are correct.
                2. Think carefully about the Crew Purpose and Crew Details to ensure the tasks are sequenced logically.
                3. Conduct a comprehensive review to detect any errors in the `task_list.yaml` file.

                **Your final answer should be the complete `task_list.yaml` file, and only the `task_list.yaml` file.**
                """),
            output_file = 'src/crew_builder_crew/output/task_list.yaml',
            expected_output=task_list_example,
            context=context,
			agent=agent
        )
        # self.task_outputs['review_task_list_task'] = task.execute()
        return task

    def create_agent_list_task(self, agent, crew_purpose, crew_details, agent_list_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 3

                You are a **CrewAI Crew Expert Engineer** and this is the third step in creating a *NEW* CrewAI Crew.

                ## Objective
                Your next task is to provide a list of agents to fulfill the Crew Purpose and Crew Details.
                      
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Analyze the `task_list.yaml`, Crew Purpose, and Crew Details to determine the required agents.
                2. Think carefully about the `task_list.yaml`, Crew Purpose, and Crew Details to provide the most suitable agents.
                3. Create am `agent_list.yaml` file that contains the name of each agent and a concise summary.

                **Your final answer should be the complete `agent_list.yaml` file, and only the `agent_list.yaml` file.**
                """),
            expected_output=agent_list_example,
			agent=agent
        )
        # self.task_outputs['create_agent_list_task'] = task.execute()
        return task

    def review_agent_list_task(self, agent, context, crew_purpose, crew_details, agent_list_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 4
                      
                You are a **Software Quality Control Engineer** and this is the fourth step in creating a *NEW* CrewAI Crew.
                      
                ## Objective
                Your task is to carefully review the provided list of agents designed to fulfill the Crew Purpose and Crew Details.
                      
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Analyze the given Crew Purpose and Crew Details to determine if the provided agents are correct.
                2. Think carefully about the `task_list.yaml`, Crew Purpose, and Crew Details to provide the most suitable agents.
                3. Conduct a comprehensive review to detect any errors in the `agent_list.yaml` file.

                **Your final answer should be the complete `agent_list.yaml` file, and only the `agent_list.yaml` file.**
                """),
            output_file = 'src/crew_builder_crew/output/agent_list.yaml',
            expected_output=agent_list_example,
            context=context,
			agent=agent
        )
        # self.task_outputs['review_agent_list_task'] = task.execute()
        return task

    def create_tasks_task(self, agent, context, crew_purpose, crew_details, tasks_class_example):
        task = Task(
            description=dedent(f"""\
                # CrewAI Crew Creation: Step 5

                You are a **CrewAI Crew Expert Engineer** and this is the fifth step in creating a *NEW* CrewAI Crew.

                ## Objective
                Your next task is to provide detailed task descriptions to fulfill the Crew Purpose and Crew Details.

                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Create a well-structured `tasks.py` file that clearly describes each task defined in `task_list.yaml`.
                2. Provide concise and impactful descriptions to optimize clarity and token usage.
                3. Use markdown formatting to enhance the task descriptions and emphasize crucial aspects of each task.

                ### Markdown Formatting Tips
                - Use level 2 headings (`##`) to separate each task.
                - Utilize bold (`**text**`) and italic (`*text*`) formatting to highlight important information.
                - Create bullet points (`-`) or numbered lists (`1.`) to break down complex tasks into smaller steps.
                - Use code blocks (triple backticks) to display code snippets or file names.

                ## Deliverable
                **Your final answer should be a complete `tasks.py` file, and only the `tasks.py` file.**
                """),
            expected_output=tasks_class_example,
            context=context,
            agent=agent
        )
        # self.task_outputs['create_tasks'] = task.execute()
        return task

    def review_tasks_task(self, agent, context, crew_purpose, crew_details, tasks_class_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 6

                You are a **Software Quality Control Engineer** and this is the sixth step in creating a *NEW* CrewAI Crew.

                ## Objective
                Your task is to carefully review the provided task descriptions to ensure they fulfill the Crew Purpose and Crew Details.

                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Conduct a thorough examination of the `tasks.py` file:
                - Verify that each task defined in `task_list.yaml` is clearly described.
                - Ensure that the descriptions are concise, impactful, and optimized for clarity and token usage.
                - Check that crucial aspects of each task description are emphasized using markdown formatting.

                2. Review the Python code:
                - Ensure that the Python code in `tasks.py` is complete and functional.
                - Verify that the code follows best practices and adheres to the specified requirements.

                ## Markdown Formatting Checklist
                - [ ] Level 2 headings (`##`) are used to separate each task.
                - [ ] Bold (`**text**`) and italic (`*text*`) formatting is utilized to highlight important information.
                - [ ] Bullet points (`-`) or numbered lists (`1.`) are used to break down complex tasks into smaller steps.
                - [ ] Code blocks (triple backticks) are used to display code snippets or file names.

                Ensure that all markdown formatting is properly applied and enhances the readability and clarity of the task descriptions.                      
                
                ## Deliverable
                **Your final answer should be a complete `tasks.py` file, and only the `tasks.py` file.**
                """),
            output_file = 'src/crew_builder_crew/output/tasks.py',
            expected_output=tasks_class_example,
            context=context,
            agent=agent
        )
        # self.task_outputs['review_tasks'] = task.execute()
        return task

    def create_agents_task(self, agent, context, crew_purpose, crew_details, agents_class_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 7

                You are a **CrewAI Crew Expert Engineer** and this is the seventh step in creating a *NEW* CrewAI Crew.

                ## Objective
                Your next task is to provide detailed agent roles, goals, and backstories to fulfill the Crew Purpose and Crew Details.

                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Create a well-structured `agents.py` file that clearly defines the attributes of each agent in `agent_list.yaml`.
                2. Provide concise and impactful roles, goals, and backstories, optimizing token usage while maintaining clarity.
                3. Use markdown formatting to enhance the agent attributes and emphasize crucial aspects of each attribute.

                ## Markdown Formatting Checklist
                - [ ] Level 2 headings (`##`) are used to separate each task.
                - [ ] Bold (`**text**`) and italic (`*text*`) formatting is utilized to highlight important information.
                - [ ] Bullet points (`-`) or numbered lists (`1.`) are used to break down complex tasks into smaller steps.
                - [ ] Code blocks (triple backticks) are used to display code snippets or file names.

                Ensure that all markdown formatting is properly applied and enhances the readability and clarity of the task descriptions.                      
                
                ## Deliverable
                **Your final answer should be a complete `agents.py` file, and only the `agents.py` file.**
                """),
            expected_output=agents_class_example,
            context=context,
			agent=agent
        )
        # self.task_outputs['create_agents'] = task.execute()
        return task

    def review_agents_task(self, agent, context, crew_purpose, crew_details, agents_class_example):
        # crew_python = self.task_outputs.get('review_crew')  # Get the output from create_crew task
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 8

                You are a **Software Quality Control Engineer** and this is the eighth step in creating a *NEW* CrewAI Crew.

                ## Objective
                Your task is to carefully review the provided agent roles, goals, and backstories to ensure they fulfill the Crew Purpose and Crew Details.

                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Conduct a thorough examination of the `agents.py` file:
                - Verify that each agent defined in `agent_list.yaml` is clearly described.
                - Ensure that the roles, goals, and backstories are concise, impactful, and optimized for clarity and token usage.
                - Check that crucial aspects of each of the roles, goals, and backstories are emphasized using markdown formatting.

                2. Review the Python code:
                - Ensure that the Python code in `agents.py` is complete and functional.
                - Verify that the code follows best practices and adheres to the specified requirements.

                ## Markdown Formatting Checklist
                - [ ] Level 2 headings (`##`) are used to separate each task.
                - [ ] Bold (`**text**`) and italic (`*text*`) formatting is utilized to highlight important information.
                - [ ] Bullet points (`-`) or numbered lists (`1.`) are used to break down complex tasks into smaller steps.
                - [ ] Code blocks (triple backticks) are used to display code snippets or file names.

                Ensure that all markdown formatting is properly applied and enhances the readability and clarity of the task descriptions.                      
                
                ## Deliverable
                **Your final answer should be a complete `agents.py` file, and only the `agents.py` file.**
                """),
            output_file = 'src/crew_builder_crew/output/agents.py',
            expected_output=agents_class_example,
            context=context,
			agent=agent
        )
        # self.task_outputs['review_agents'] = task.execute()
        return task

    def create_main_py_task(self, agent, context, crew_purpose, crew_details, main_py_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 9

                You are a **CrewAI Crew Expert Engineer** working on the ninth step of creating a *NEW* CrewAI Crew.

                ## Objective
                Provide the `main.py` file that instantiates the Agents, Tasks, and Crew to fulfill the Crew Purpose and Details.

                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Create a well-structured `main.py` file:
                - Instantiate Agents defined in `agent_list.yaml` under the `# Create Agents` section.
                - Instantiate Tasks defined in `task_list.yaml` under the `# Create Tasks` section.
                - Invoke each Agent and Task in the `# Create Crew` section.

                2. Ensure proper instantiation and invocation of all Agents and Tasks.
                
                ## Deliverable
                **Your final answer should be a complete `main.py` file, and only the `main.py` file.**
                """),
            expected_output=main_py_example,
            context=context,
			agent=agent
        )
        # self.task_outputs['create_agents'] = task.execute()
        return task

    def review_main_py_task(self, agent, context, crew_purpose, crew_details, main_py_example):
        task = Task(
			description=dedent(f"""\
                # CrewAI Crew Creation: Step 10

                You are a **Software Quality Control Engineer** and this is the tenth step in creating a *NEW* CrewAI Crew.

                ## Objective
                Carefully review the provided `main.py` file that instantiates the Agents, Tasks, and Crew to fulfill the Crew Purpose and Details.

                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>

                ## Crew Details
                <crew_details>{crew_details}</crew_details>

                ## Instructions
                1. Conduct a thorough examination of the `main.py` file:
                - Verify that each agent defined in `agent_list.yaml` is instantiated under the `# Create Agents` section.
                - Verify that each task defined in `task_list.yaml` is instantiated under the `# Create Tasks` section.
                - Ensure that each Agent and Task in the `# Create Crew` section.

                2. Review the Python code:
                - Ensure proper instantiation and invocation of all Agents and Tasks.
                - Ensure that the Python code in `main.py` is complete and functional.
                - Verify that the code follows best practices and adheres to the specified requirements.
                
                ## Deliverable
                **Your final answer should be a complete `main.py` file, and only the `main.py` file.**
                """),
            output_file = 'src/crew_builder_crew/output/main.py',
            expected_output=main_py_example,
            context=context,
			agent=agent
        )
        # self.task_outputs['create_agents'] = task.execute()
        return task