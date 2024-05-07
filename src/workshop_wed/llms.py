
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_community.chat_models import ChatPerplexity

class RedHatNewsletterCrewLLMs:

    chatgpt4 = ChatOpenAI(
        model='gpt-4-turbo',
        temperature=0
        )

    haiku = ChatAnthropic(
        model='claude-3-haiku-20240307',
        temperature=.5
        )

    llama3 = ChatGroq(
        model_name="llama3-70b-8192",
        temperature=.5
        )