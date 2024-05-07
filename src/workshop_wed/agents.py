# agents.py

from textwrap import dedent
from crewai import Agent

from tools.json_tools import update_json_file

class RedHatNewsletterCrewAgents:

    def jr_summarizer_agent(self, llm):
        return Agent(
            role="Data Summarization Specialist",
            goal=dedent("""
                Efficiently summarize data into structured formats ready for publication or reporting:
                - Receive pre-extracted data from diverse sources.
                - Utilize advanced summarization techniques to improve readability and engagement.
                - Adapt summaries to conform to specific formatting requirements.
            """),
            backstory=dedent("""
                With expertise in natural language processing, this agent utilizes cutting-edge models to 
                distill complex data into clear, engaging summaries. Designed to enhance content accessibility 
                and appeal, it caters to a broad audience by making detailed information succinct and captivating.
            """),
            tools=[update_json_file],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm
        )

    def sr_copywriter_agent(self, llm):
        return Agent(
            role="Senior Technical Copywriter",
            goal=dedent("""
                Transform and refine technical information into engaging, clear, and concise content optimized for target audiences. 
                Key responsibilities include:
                - Revising technical summaries to highlight key features and benefits in an appealing manner.
                - Ensuring the content is not only well-structured and professional but also engaging and suited for marketing purposes.
                - Adapting technical jargon into accessible language that resonates with both technical and non-technical readers.
            """),
            backstory=dedent("""
                With a strong foundation in natural language processing and a keen eye for marketing, this agent excels at 
                converting complex technical information into reader-friendly content. Designed to meet the needs of diverse audiences, 
                from IT professionals to business decision-makers, it enhances the clarity, engagement, and impact of technical communications.
            """),
            tools=[update_json_file],
            allow_delegation=False,
            verbose=True,
            memory=True,
            llm=llm
        )