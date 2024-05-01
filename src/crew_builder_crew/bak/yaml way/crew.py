from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools.tools import CodeDocsSearchTool, GithubSearchTool, WebsiteSearchTool

crewai_docs_tool = CodeDocsSearchTool(docs_url='https://docs.crewai.com', description='Search CrewAI documentation')
crewai_github_tool = GithubSearchTool(
    github_repo='https://github.com/joaomdmoura/crewAI-examples',
    content_types=['code', 'repo'],
    description='Search CrewAI examples on GitHub'
)

with open('src/crew_builder_crew/examples/crew.py', 'r') as file:
    create_crewai_crew_example = file.read()

with open('src/crew_builder_crew/examples/tasks.yaml', 'r') as file:
    create_crewai_tasks_example = file.read()

with open('src/crew_builder_crew/examples/agents.yaml', 'r') as file:
    create_crewai_agents_example = file.read()

@CrewBase
class CrewBuilderCrew():
    """Crew Builder Crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def crewai_crew_expert_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['crewai_crew_expert_agent'],
            #tools = [crewai_docs_tool],
            #tools = [crewai_docs_tool, crewai_github_tool],
            llm = self.groq_llm,
            memory = True,
        )

    @agent
    def crewai_qa_engineer_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['crewai_qa_engineer_agent'],
            #tools = [crewai_docs_tool],
            #tools = [crewai_docs_tool, crewai_github_tool],
            llm = self.groq_llm,
            memory = True,
        )

    @task
    def create_crewai_crew_task(self) -> Task:
        return Task(
            config = self.tasks_config['create_crewai_crew_task'],
            agent = self.crewai_crew_expert_agent(),
            expected_output = create_crewai_crew_example,
        )

    @task
    def review_crewai_crew_task(self) -> Task:
        return Task(
            config = self.tasks_config['review_crewai_crew_task'],
            agent = self.crewai_qa_engineer_agent(),
            expected_output = create_crewai_crew_example,
            output_file = 'src/crew_builder_crew/output/crew.py',
        )

    @task
    def create_crewai_tasks_task(self) -> Task:
        return Task(
            config = self.tasks_config['create_crewai_tasks_task'],
            agent = self.crewai_crew_expert_agent(),
            expected_output = create_crewai_tasks_example,
        )
        
    @task
    def review_crewai_tasks_task(self) -> Task:
        return Task(
            config = self.tasks_config['review_crewai_tasks_task'],
            agent = self.crewai_qa_engineer_agent(),
            expected_output = create_crewai_tasks_example,
            output_file = 'src/crew_builder_crew/output/tasks.yaml',
        )

    @task
    def create_crewai_agents_task(self) -> Task:
        return Task(
            config = self.tasks_config['create_crewai_agents_task'],
            agent = self.crewai_crew_expert_agent(),
            expected_output = create_crewai_agents_example,
        )
        
    @task
    def review_crewai_agents_task(self) -> Task:
        return Task(
            config = self.tasks_config['review_crewai_agents_task'],
            agent = self.crewai_qa_engineer_agent(),
            expected_output = create_crewai_agents_example,
            output_file = 'src/crew_builder_crew/output/agents.yaml',
        )
        """ 
    @task
    def create_crewai_main_task(self) -> Task:
        return Task(
            config = self.tasks_config['create_crewai_main_task'],
            agent = self.crewai_crew_expert_agent()
        )
        
    @task
    def review_crewai_main_task(self) -> Task:
        return Task(
            config = self.tasks_config['review_crewai_main_task'],
            agent = self.crewai_qa_engineer_agent()
        )
        
    @task
    def create_pyproject_task(self) -> Task:
        return Task(
            config = self.tasks_config['create_pyproject_task'],
            agent = self.crewai_crew_expert_agent()
        )
        
    @task
    def review_pyproject_task(self) -> Task:
        return Task(
            config = self.tasks_config['review_pyproject_task'],
            agent = self.crewai_qa_engineer_agent()
        ) """
    
    @crew
    def crew(self) -> Crew:
        """Creates the Crew Builder Crew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            manager_llm = self.groq_llm,
            verbose = 2,
            max_rpm = 6
        )