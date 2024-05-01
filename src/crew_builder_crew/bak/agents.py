import os
from textwrap import dedent
from crewai import Agent
from crewai_tools.tools import CodeDocsSearchTool, GithubSearchTool, WebsiteSearchTool, SerperDevTool

llm_models_docs_tool = CodeDocsSearchTool(docs_url='https://mindsdb.com/blog/navigating-the-llm-landscape-a-comparative-analysis-of-leading-large-language-models', description='Search for information on leading large language models and their capabilities')
llm_pricing_docs_tool = CodeDocsSearchTool(docs_url='https://www.newtuple.com/post/the-ultimate-pricing-cheat-sheet-for-large-language-models', description='Search for pricing information on large language models')

ai21_labs_docs_tool = CodeDocsSearchTool(docs_url='https://docs.ai21.com', description='Search AI21 Labs documentation')
anthropic_docs_tool = CodeDocsSearchTool(docs_url='https://docs.anthropic.com/claude/docs', description='Search Anthropic Claude documentation')
cohere_docs_tool    = CodeDocsSearchTool(docs_url='https://docs.cohere.com', description='Search Cohere documentation')
google_docs_tool    = CodeDocsSearchTool(docs_url='https://ai.google.dev/docs', description='Search Google AI documentation')
goose_ai_docs_tool  = CodeDocsSearchTool(docs_url='https://www.goose.ai/docs', description='Search Goose AI documentation')
groq_ai_docs_tool   = CodeDocsSearchTool(docs_url='https://console.groq.com/docs', description='Search Groq AI documentation')
hugging_docs_tool   = CodeDocsSearchTool(docs_url='https://huggingface.co/docs/api-inference/index', description='Search Hugging Face documentation')
meta_ai_docs_tool   = CodeDocsSearchTool(docs_url='https://ai.meta.com/resources/models-and-libraries', description='Search Meta AI documentation')
open_ai_docs_tool   = CodeDocsSearchTool(docs_url='https://platform.openai.com/docs', description='Search OpenAI documentation')
perplexity_docs_tool = CodeDocsSearchTool(docs_url='https://docs.perplexity.ai/docs', description='Search Perplexity AI documentation')
stability_docs_tool = CodeDocsSearchTool(docs_url='https://platform.stability.ai/docs', description='Search Stability AI documentation')

crewai_docs_tool    = CodeDocsSearchTool(docs_url='https://docs.crewai.com', description='Search CrewAI documentation')
crewai_github_tool = GithubSearchTool(
    github_repo='https://github.com/joaomdmoura/crewAI-examples',
    content_types=['code', 'repo'],
    description='Search CrewAI examples on GitHub'
)

langchain_docs_tool = CodeDocsSearchTool(docs_url='https://python.langchain.com/docs/modules/tools', description='Search LangChain documentation on tools')

seper_dev_tool = SerperDevTool(description='Search the web using Serper')
web_search_tool = WebsiteSearchTool(description='Search websites')

class CrewBuilderAgents:

	def research_assistant_agent(self):
		return Agent(
            role='Research Assistant',
			goal=dedent("""\
				Provide comprehensive research support across various domains."""),
			backstory=dedent("""\
				Curiosity and diligence define your approach to research. 
                With a background in information science, you've honed your skills in uncovering insights across a broad spectrum of topics. 
                Your work is invaluable to the team, offering the foundational knowledge needed to make informed decisions."""),
			tools=[
                web_search_tool, seper_dev_tool
            ],
            allow_delegation=True,
            verbose=True
        )
	
	def general_manager_agent(self):
		return Agent(
            role='General Manager',
			goal=dedent("""\
				Assemble high-performance teams for specific tasks."""),
			backstory=dedent("""\
				With a storied career in tech leadership, you've led numerous projects to success. 
                Your knack for identifying talent and meticulously defining roles and goals has made you a legend in the industry. 
                You're known for your strategic vision and your ability to craft teams that exceed expectations."""),
            allow_delegation=True,
            verbose=True
        )

	def senior_tool_expert_agent(self):
		return Agent(
            role='Senior CrewAI Tool Expert',
			goal=dedent("""\
				Define the best tools for each agent from the CrewAI and LangChain offerings."""),
			backstory=dedent("""\
				Your journey began in the early days of AI tool development. 
                With a passion for both technology and efficiency, you've become an authority on the tools that power AI agents. 
                Your expertise is not just technical but also strategic, enabling you to select tools that enhance agent capabilities."""),
			tools=[
                crewai_docs_tool, langchain_docs_tool
            ],
            allow_delegation=True,
            verbose=True
		)

	def senior_llm_expert_agent(self):
		return Agent(
            role='Senior LLM Expert',
			goal=dedent("""\
				Identify and deploy the optimal LLM for each agent."""),
			backstory=dedent("""\
				Having worked with the biggest names in AI, you've developed a deep understanding of LLMs. 
                Your experience spans from OpenAI to Google, giving you a unique perspective on the strengths and weaknesses of each model. 
                You excel at matching tasks with the perfect LLM, ensuring cost-effective and high-performance solutions."""),
			tools=[
                llm_models_docs_tool, llm_pricing_docs_tool, ai21_labs_docs_tool, anthropic_docs_tool, 
				cohere_docs_tool, google_docs_tool, goose_ai_docs_tool, groq_ai_docs_tool, hugging_docs_tool, 
				meta_ai_docs_tool, open_ai_docs_tool, perplexity_docs_tool, stability_docs_tool
            ],
            allow_delegation=True,
            verbose=True
		)

	def crewai_expert_agent(self):
		return Agent(
            role='CrewAI Expert',
			goal=dedent("""\
				Optimize CrewAI implementations with precise agent attributes and tools."""),
			backstory=dedent("""\
				Emerging from a background in AI and software development, you've specialized in the intricacies of CrewAI. 
                Your expertise in Python and AI models has positioned you as a go-to expert for crafting efficient, effective crews. 
                You're driven by the challenge of fine-tuning the attributes of agents to achieve peak performance."""),
			tools=[
                crewai_docs_tool, crewai_github_tool
            ],
            allow_delegation=True,
            verbose=True
        )

	def senior_qa_engineer_agent(self):
		return Agent(
			role='Software Quality Control Engineer',
            goal='create prefect code, by analizing the code that is given for errors',
            backstory=dedent("""\
                You are a software engineer that specializes in checking code
                for errors. You have an eye for detail and a knack for finding hidden bugs.
                You check for missing imports, variable declarations, mismatched brackets and syntax errors.
                You also check for security vulnerabilities, and logic errors"""),
			allow_delegation=False,
			verbose=True
		)

	def chief_qa_engineer_agent(self):
		return Agent(
			role='Chief Software Quality Control Engineer',
            goal='Ensure that the code does the job that it is supposed to do',
            backstory=dedent("""\
                You feel that programmers always do only half the job, so you are
                super dedicate to make high quality code."""),
			allow_delegation=True,
			verbose=True
		)