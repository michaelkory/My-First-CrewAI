# main.py

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process

from llms import RedHatNewsletterCrewLLMs as llms; llms = llms()
from tasks import RedHatNewsletterCrewTasks as tasks; tasks = tasks()
from agents import RedHatNewsletterCrewAgents as agents; agents = agents()

from tools.json_tools import initialize_json_file
from tools.html_tools import create_newsletter_html

# initialize_json_file()

print('-------------------------------')
print("## Welcome to the Red Hat Newsletter Crew")
workshop_date = '5/15/24'
print(f"## Workshop Wednesday for {workshop_date}")
print('-------------------------------')

# Create Agents
jr_summarizer_agent = agents.jr_summarizer_agent(llms.haiku)
sr_copywriter_agent = agents.sr_copywriter_agent(llms.llama3)

# Create Tasks
# summarize_workshop_task = tasks.summarize_workshop_task(jr_summarizer_agent, workshop_date)
# copywrite_workshop_task = tasks.copywrite_workshop_task(sr_copywriter_agent)
# summarize_training_task = tasks.summarize_training_task(jr_summarizer_agent, workshop_date)
# copywrite_training_task = tasks.copywrite_training_task(sr_copywriter_agent)
# summarize_assessment_task = tasks.summarize_assessment_task(jr_summarizer_agent, workshop_date)
# copywrite_assessment_task = tasks.copywrite_assessment_task(sr_copywriter_agent)

# summarize_ansible_blog_task = tasks.summarize_blog_task(
#     jr_summarizer_agent, "Red Hat Ansible Automation", "ansible_blog",
#     "https://www.redhat.com/en/rss/blog/channel/red-hat-ansible-automation")
# copywrite_ansible_blog_task = tasks.copywrite_blog_task(
#     sr_copywriter_agent, "Red Hat Ansible Automation", "ansible_blog")

# summarize_openshift_blog_task = tasks.summarize_blog_task(
#     jr_summarizer_agent, "Red Hat Openshift", "openshift_blog",
#     "https://www.redhat.com/en/rss/blog/channel/red-hat-openshift")
# copywrite_openshift_blog_task = tasks.copywrite_blog_task(
#     sr_copywriter_agent, "Red Hat Openshift", "openshift_blog")

# summarize_rhel_blog_task = tasks.summarize_blog_task(
#     jr_summarizer_agent, "Red Hat Enterprise Linux", "rhel_blog",
#     "https://www.redhat.com/en/rss/blog/channel/red-hat-enterprise-linux")
# copywrite_rhel_blog_task = tasks.copywrite_blog_task(
#     sr_copywriter_agent, "Red Hat Enterprise Linux", "rhel_blog")

# summarize_ansible_video_task = tasks.summarize_video_task(
#     jr_summarizer_agent, "Red Hat Ansible Automation", "ansible_video",
#     "https://www.youtube.com/feeds/videos.xml?channel_id=UCPJo5UY1KsP7J1BuHmiWNzQ")
# copywrite_ansible_video_task = tasks.copywrite_video_task(
#     sr_copywriter_agent, "Ansible", "ansible_video")

# summarize_openshift_video_task = tasks.summarize_video_task(
#     jr_summarizer_agent, "Red Hat Openshift", "openshift_video",
#     "https://www.youtube.com/feeds/videos.xml?channel_id=UCZKMj3YI0wP-kq4QYpaKdEA")
# copywrite_openshift_video_task = tasks.copywrite_video_task(
#     sr_copywriter_agent, "Red Hat Openshift", "openshift_video")

summarize_rhel_video_task = tasks.summarize_video_task(
    jr_summarizer_agent, "Red Hat Enterprise Linux", "rhel_video",
    "https://www.youtube.com/feeds/videos.xml?channel_id=UCG5LuxhUtax6wVhH1qPNxvA")
copywrite_rhel_video_task = tasks.copywrite_video_task(
    sr_copywriter_agent, "Red Hat Enterprise Linux", "rhel_video")

# Create Crew
crew = Crew(
    agents=[
        jr_summarizer_agent,
        sr_copywriter_agent
    ],
    tasks=[
        # summarize_workshop_task,
        # copywrite_workshop_task,
        # summarize_training_task,
        # copywrite_training_task,
        # summarize_assessment_task,
        # copywrite_assessment_task,
        # summarize_ansible_blog_task,
        # copywrite_ansible_blog_task,
        # summarize_openshift_blog_task,
        # copywrite_openshift_blog_task,
        # summarize_rhel_blog_task,
        # copywrite_rhel_blog_task,
        # summarize_ansible_video_task,
        # copywrite_ansible_video_task,
        # summarize_openshift_video_task,
        # copywrite_openshift_video_task,
        summarize_rhel_video_task,
        copywrite_rhel_video_task
    ],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=10,
    verbose=2
)

# Kickoff Crew
crew.kickoff()

create_newsletter_html()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print(crew)