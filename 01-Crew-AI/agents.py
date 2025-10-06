from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"


# Create a senior blog content researcher
blog_researcher = Agent(
    role="Blog Researcher from YouTube Videos",
    goal="Get the relevant video content for the topic {topic} from Youtube Channel",
    name="Blog Researcher",
    verbose=True,
    memory=True,
    backstory = {
        "Expert in understanding videos in AI Data Science, Machine Learning and GenAI and providing suggestions",
    },
    tools=[],
    allow_delegation=True,
)

# Create a senior blog writen agent with YT Tool
blog_writer = Agent(
    role="Blog Writer from YouTube Videos",
    goal="Narrate compelling tech stories for the topic {topic} from Youtube Channel",
    name="Blog Writer",
    verbose=True,
    memory=True,
    backstory = {
        "With a flair of simplifying complex topics, you craft engaging narratives that captivate and educate"
        ", bringing new discoveries to light in an accessible manner.",
    },
    tools=[yt_tool],
    allow_delegation=False,
)

