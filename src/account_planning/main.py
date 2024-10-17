```
# main.py

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process
from langchain_anthropic import ChatAnthropic

claude_llm = ChatAnthropic(temperature=1, model='claude-3-haiku-20240307')

from tasks import CrewBuilderTasks
from agents import CrewBuilderAgents

tasks = CrewBuilderTasks()
agents = CrewBuilderAgents()

print("## Welcome to the Account Plan Crew")
print('-------------------------------')
new_crew_purpose = """
## Crew Purpose
An effective account plan identifies and aligns our understanding of customer's business drivers, strategies, and initiatives to our business value, and serves as a tool to build and activate relationships with the customer and their ecosystem in order to grow business and customer success.
"""
new_crew_details = """
Your task is to create a comprehensive account plan for a key customer. 

The plan should include:
- A Customer View section summarizing their current state, needs, and priorities
- An overview of the strategic value Red Hat can provide to the customer
- Details on the customer's objectives, challenges, and initiatives 
- An assessment of the customer's growth trajectory and competitive landscape
- A SWOT analysis of Red Hat's positioning with the customer
- A technical landscape review of the customer's IT infrastructure and platforms, including:
    - Server and Cloud Operating System TDP: 
    - Major operating systems in use (on-premise and cloud)
    - Linux distributions and strategy
    - Systems management and automation solutions 
    - Workload environments targeted for RHEL
    - Cloud Native Infrastructure TDP:
    - Cloud strategy (on-prem, public, hybrid)
    - Kubernetes and container platform usage
    - Virtualization strategy and workloads
    - Container platform management and security
    - Application Platform TDP: 
    - Application migration/modernization strategy
    - Key customer applications and initiatives
    - Software supply chain and CI/CD practices
    - Cloud-native development landscape
    - Mission Critical IT Automation TDP:
    - Current automation tools and practices 
    - Workloads and processes being automated
    - Automation strategy and maturity
    - Executive buy-in and cross-functional alignment
"""

# Create Agents
customer_current_state_agent = agents.customer_current_state_agent(claude_llm)
red_hat_strategic_value_agent = agents.red_hat_strategic_value_agent(claude_llm)
customer_objectives_agent = agents.customer_objectives_agent(claude_llm)
customer_growth_trajectory_agent = agents.customer_growth_trajectory_agent(claude_llm)
swot_analysis_agent = agents.swot_analysis_agent(claude_llm)
it_infrastructure_review_agent = agents.it_infrastructure_review_agent(claude_llm)
server_and_cloud_os_agent = agents.server_and_cloud_os_agent(claude_llm)
major_operating_systems_agent = agents.major_operating_systems_agent(claude_llm)
linux_distributions_agent = agents.linux_distributions_agent(claude_llm)
cloud_native_infrastructure_agent = agents.cloud_native_infrastructure_agent(claude_llm)
application_migration_agent = agents.application_migration_agent(claude_llm)
automation_tools_agent = agents.automation_tools_agent(claude_llm)
virtualization_strategy_agent = agents.virtualization_strategy_agent(claude_llm)
container_platform_agent = agents.container_platform_agent(claude_llm)
key_applications_agent = agents.key_applications_agent(claude_llm)
cloud_native_development_agent = agents.cloud_native_development_agent(claude_llm)
mission_critical_it_automation_agent = agents.mission_critical_it_automation_agent(claude_llm)
automation_strategy_agent = agents.automation_strategy_agent(claude_llm)

# Create Tasks
analyze_customer_current_state_and_needs_task = tasks.analyze_customer_current_state_and_needs_task(customer_current_state_agent, new_crew_purpose, new_crew_details)
assess_red_hat_strategic_value_task = tasks.assess_red_hat_strategic_value_task(red_hat_strategic_value_agent, new_crew_purpose, new_crew_details)
document_customer_objectives_challenges_and_initiatives_task = tasks.document_customer_objectives_challenges_and_initiatives_task(customer_objectives_agent, new_crew_purpose, new_crew_details)
evaluate_customer_growth_trajectory_and_competitive_landscape_task = tasks.evaluate_customer_growth_trajectory_and_competitive_landscape_task(customer_growth_trajectory_agent, new_crew_purpose, new_crew_details)
conduct_swot_analysis_of_red_hat_positioning_task = tasks.conduct_swot_analysis_of_red_hat_positioning_task(swot_analysis_agent, new_crew_purpose, new_crew_details)
review_customer_it_infrastructure_and_platforms_task = tasks.review_customer_it_infrastructure_and_platforms_task(it_infrastructure_review_agent, new_crew_purpose, new_crew_details)
analyze_customer_server_and_cloud_operating_systems_task = tasks.analyze_customer_server_and_cloud_operating_systems_task(server_and_cloud_os_agent, new_crew_purpose, new_crew_details)
review_customer_major_operating_systems_task = tasks.review_customer_major_operating_systems_task(major_operating_systems_agent, new_crew_purpose, new_crew_details)
analyze_customer_linux_distributions_and_strategy_task = tasks.analyze_customer_linux_distributions_and_strategy_task(linux_distributions_agent, new_crew_purpose, new_crew_details)
review_customer_cloud_native_infrastructure_task = tasks.review_customer_cloud_native_infrastructure_task(cloud_native_infrastructure_agent, new_crew_purpose, new_crew_details)
analyze_customer_application_migration_and_modernization_strategy_task = tasks.analyze_customer_application_migration_and_modernization_strategy_task(application_migration_agent, new_crew_purpose, new_crew_details)
assess_customer_automation_tools_and_practices_task = tasks.assess_customer_automation_tools_and_practices_task(automation_tools_agent, new_crew_purpose, new_crew_details)
evaluate_customer_virtualization_strategy_task = tasks.evaluate_customer_virtualization_strategy_task(virtualization_strategy_agent, new_crew_purpose, new_crew_details)
review_customer_container_platform_management_and_security_task = tasks.review_customer_container_platform_management_and_security_task(container_platform_agent, new_crew_purpose, new_crew_details)
analyze_customer_key_applications_and_initiatives_task = tasks.analyze_customer_key_applications_and_initiatives_task(key_applications_agent, new_crew_purpose, new_crew_details)
assess_customer_cloud_native_development_landscape_task = tasks.assess_customer_cloud_native_development_landscape_task(cloud_native_development_agent, new_crew_purpose, new_crew_details)
evaluate_customer_mission_critical_it_automation_task = tasks.evaluate_customer_mission_critical_it_automation_task(mission_critical_it_automation_agent, new_crew_purpose, new_crew_details)
review_customer_automation_strategy_and_maturity_task = tasks.review_customer_automation_strategy_and_maturity_task(automation_strategy_agent, new_crew_purpose, new_crew_details)

# Create Crew
new_crew_crew = Crew(
    agents=[
        customer_current_state_agent,
        red_hat_strategic_value_agent,
        customer_objectives_agent,
        customer_growth_trajectory_agent,
        swot_analysis_agent,
        it_infrastructure_review_agent,
        server_and_cloud_os_agent,
        major_operating_systems_agent,
        linux_distributions_agent,
        cloud_native_infrastructure_agent,
        application_migration_agent,
        automation_tools_agent,
        virtualization_strategy_agent,
        container_platform_agent,
        key_applications_agent,
        cloud_native_development_agent,
        mission_critical_it_automation_agent,
        automation_strategy_agent
    ],
    tasks=[
        analyze_customer_current_state_and_needs_task,
        assess_red_hat_strategic_value_task,
        document_customer_objectives_challenges_and_initiatives_task,
        evaluate_customer_growth_trajectory_and_competitive_landscape_task,
        conduct_swot_analysis_of_red_hat_positioning_task,
        review_customer_it_infrastructure_and_platforms_task,
        analyze_customer_server_and_cloud_operating_systems_task,
        review_customer_major_operating_systems_task,
        analyze_customer_linux_distributions_and_strategy_task,
        review_customer_cloud_native_infrastructure_task,
        analyze_customer_application_migration_and_modernization_strategy_task,
        assess_customer_automation_tools_and_practices_task,
        evaluate_customer_virtualization_strategy_task,
        review_customer_container_platform_management_and_security_task,
        analyze_customer_key_applications_and_initiatives_task,
        assess_customer_cloud_native_development_landscape_task,
        evaluate_customer_mission_critical_it_automation_task,
        review_customer_automation_strategy_and_maturity_task
    ],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=10,
    verbose=2
)

# Kickoff Crew
new_crew = new_crew_crew.kickoff()

# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print(new_crew)
```