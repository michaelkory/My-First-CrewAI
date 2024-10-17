```
from textwrap import dedent
from crewai import Task

class NewCrewTasks:

    def analyze_customer_current_state_and_needs_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 1 - Analyze Customer Current State and Needs
                
                ## Objective
                Analyze the customer's current state, including their business drivers, strategies, and initiatives to understand their needs.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's current state, including their industry, market position, and overall business goals.
                2. Identify the customer's key business drivers, strategies, and initiatives that are shaping their priorities and decision-making.
                3. Analyze how the customer's current state and needs align with Red Hat's capabilities and value proposition.
                4. Document your findings in a comprehensive summary.
                
                ## Deliverable
                A detailed analysis of the customer's current state and needs, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def assess_red_hat_strategic_value_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 2 - Assess Red Hat's Strategic Value
                
                ## Objective
                Assess the strategic value that Red Hat can provide to the customer based on their current state and needs.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Review Red Hat's products, services, and solutions that are relevant to the customer's needs and initiatives.
                2. Identify the key value propositions and competitive advantages that Red Hat can offer the customer.
                3. Determine how Red Hat's offerings can help the customer achieve their business objectives and address their challenges.
                4. Document the strategic value that Red Hat can provide to the customer in the account plan.
                
                ## Deliverable
                A clear assessment of the strategic value that Red Hat can provide to the customer, including specific ways in which Red Hat's solutions can support the customer's goals.
            """),
            agent=agent
        )

    def document_customer_objectives_challenges_and_initiatives_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 3 - Document Customer Objectives, Challenges, and Initiatives
                
                ## Objective
                Document the customer's key objectives, challenges, and initiatives that should be addressed in the account plan.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Identify the customer's primary business objectives, such as revenue growth, cost reduction, or operational efficiency.
                2. Recognize the key challenges the customer is facing, such as legacy infrastructure, skills gaps, or regulatory compliance.
                3. Understand the customer's strategic initiatives, such as digital transformation, cloud migration, or application modernization.
                4. Document these customer objectives, challenges, and initiatives in the account plan, highlighting how Red Hat's solutions can address them.
                
                ## Deliverable
                A comprehensive list of the customer's key objectives, challenges, and initiatives, along with an explanation of how Red Hat can help the customer achieve their goals.
            """),
            agent=agent
        )

    def evaluate_customer_growth_trajectory_and_competitive_landscape_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 4 - Evaluate Customer Growth Trajectory and Competitive Landscape
                
                ## Objective
                Evaluate the customer's growth trajectory and competitive landscape to inform the account plan.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Analyze the customer's current market position and growth trajectory.
                2. Identify the customer's key competitors and their market positioning.
                3. Evaluate the customer's competitive landscape, including market trends, customer needs, and competitor strategies.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive analysis of the customer's growth trajectory and competitive landscape, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def conduct_swot_analysis_of_red_hat_positioning_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 5 - Conduct SWOT Analysis of Red Hat Positioning
                
                ## Objective
                Conduct a SWOT analysis to assess Red Hat's positioning with the customer.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Identify Red Hat's strengths, weaknesses, opportunities, and threats in the context of the customer's needs and initiatives.
                2. Analyze how Red Hat's strengths can be leveraged to address the customer's challenges and opportunities.
                3. Evaluate how Red Hat's weaknesses can be mitigated to minimize risks and maximize opportunities.
                4. Document the SWOT analysis in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive SWOT analysis of Red Hat's positioning with the customer, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def review_customer_it_infrastructure_and_platforms_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 6 - Review Customer IT Infrastructure and Platforms
                
                ## Objective
                Review the customer's IT infrastructure and platforms, including server and cloud operating systems, Linux distributions, and cloud-native technologies.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's IT infrastructure, including server and cloud operating systems, Linux distributions, and cloud-native technologies.
                2. Analyze the customer's IT infrastructure and platforms, identifying areas of strength and weakness.
                3. Evaluate how the customer's IT infrastructure and platforms align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive review of the customer's IT infrastructure and platforms, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def analyze_customer_server_and_cloud_operating_systems_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 7 - Analyze Customer Server and Cloud Operating Systems
                
                ## Objective
                Analyze the customer's server and cloud operating systems, including major operating systems in use and Linux distributions.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's server and cloud operating systems, including major operating systems in use and Linux distributions.
                2. Analyze the customer's server and cloud operating systems, identifying areas of strength and weakness.
                3. Evaluate how the customer's server and cloud operating systems align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive analysis of the customer's server and cloud operating systems, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def review_customer_major_operating_systems_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 8 - Review Customer Major Operating Systems
                
                ## Objective
                Review the customer's major operating systems in use, including on-premise and cloud.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's major operating systems in use, including on-premise and cloud.
                2. Analyze the customer's major operating systems, identifying areas of strength and weakness.
                3. Evaluate how the customer's major operating systems align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive review of the customer's major operating systems, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def analyze_customer_linux_distributions_and_strategy_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 9 - Analyze Customer Linux Distributions and Strategy
                
                ## Objective
                Analyze the customer's Linux distributions and strategy, including systems management and automation solutions.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's Linux distributions and strategy, including systems management and automation solutions.
                2. Analyze the customer's Linux distributions and strategy, identifying areas of strength and weakness.
                3. Evaluate how the customer's Linux distributions and strategy align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive analysis of the customer's Linux distributions and strategy, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def review_customer_cloud_native_infrastructure_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 10 - Review Customer Cloud-Native Infrastructure
                
                ## Objective
                Review the customer's cloud-native infrastructure, including cloud strategy and Kubernetes and container platform usage.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's cloud-native infrastructure, including cloud strategy and Kubernetes and container platform usage.
                2. Analyze the customer's cloud-native infrastructure, identifying areas of strength and weakness.
                3. Evaluate how the customer's cloud-native infrastructure aligns with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive review of the customer's cloud-native infrastructure, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def analyze_customer_application_migration_and_modernization_strategy_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 11 - Analyze Customer Application Migration and Modernization Strategy
                
                ## Objective
                Analyze the customer's application migration and modernization strategy, including software supply chain and CI/CD practices.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's application migration and modernization strategy, including software supply chain and CI/CD practices.
                2. Analyze the customer's application migration and modernization strategy, identifying areas of strength and weakness.
                3. Evaluate how the customer's application migration and modernization strategy aligns with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive analysis of the customer's application migration and modernization strategy, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def assess_customer_automation_tools_and_practices_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 12 - Assess Customer Automation Tools and Practices
                
                ## Objective
                Assess the customer's current automation tools and practices, as well as their automation strategy and maturity.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's current automation tools and practices, as well as their automation strategy and maturity.
                2. Analyze the customer's automation tools and practices, identifying areas of strength and weakness.
                3. Evaluate how the customer's automation tools and practices align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive assessment of the customer's automation tools and practices, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def evaluate_customer_virtualization_strategy_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 13 - Evaluate Customer Virtualization Strategy
                
                ## Objective
                Evaluate the customer's virtualization strategy and workloads.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's virtualization strategy and workloads.
                2. Analyze the customer's virtualization strategy and workloads, identifying areas of strength and weakness.
                3. Evaluate how the customer's virtualization strategy and workloads align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive evaluation of the customer's virtualization strategy and workloads, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def review_customer_container_platform_management_and_security_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 14 - Review Customer Container Platform Management and Security
                
                ## Objective
                Review the customer's container platform management and security practices.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's container platform management and security practices.
                2. Analyze the customer's container platform management and security practices, identifying areas of strength and weakness.
                3. Evaluate how the customer's container platform management and security practices align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive review of the customer's container platform management and security practices, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def analyze_customer_key_applications_and_initiatives_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 15 - Analyze Customer Key Applications and Initiatives
                
                ## Objective
                Analyze the customer's key applications and initiatives, including software supply chain and CI/CD practices.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's key applications and initiatives, including software supply chain and CI/CD practices.
                2. Analyze the customer's key applications and initiatives, identifying areas of strength and weakness.
                3. Evaluate how the customer's key applications and initiatives align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive analysis of the customer's key applications and initiatives, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def assess_customer_cloud_native_development_landscape_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 16 - Assess Customer Cloud-Native Development Landscape
                
                ## Objective
                Assess the customer's cloud-native development landscape, including application migration and modernization strategy.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's cloud-native development landscape, including application migration and modernization strategy.
                2. Analyze the customer's cloud-native development landscape, identifying areas of strength and weakness.
                3. Evaluate how the customer's cloud-native development landscape aligns with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive assessment of the customer's cloud-native development landscape, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def evaluate_customer_mission_critical_it_automation_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 17 - Evaluate Customer Mission-Critical IT Automation
                
                ## Objective
                Evaluate the customer's mission-critical IT automation, including current automation tools and practices.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's mission-critical IT automation, including current automation tools and practices.
                2. Analyze the customer's mission-critical IT automation, identifying areas of strength and weakness.
                3. Evaluate how the customer's mission-critical IT automation aligns with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive evaluation of the customer's mission-critical IT automation, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )

    def review_customer_automation_strategy_and_maturity_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 18 - Review Customer Automation Strategy and Maturity
                
                ## Objective
                Review the customer's automation strategy and maturity, including executive buy-in and cross-functional alignment.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Gather information about the customer's automation strategy and maturity, including executive buy-in and cross-functional alignment.
                2. Analyze the customer's automation strategy and maturity, identifying areas of strength and weakness.
                3. Evaluate how the customer's automation strategy and maturity align with Red Hat's solutions and value proposition.
                4. Document your findings in the account plan, highlighting key insights that will inform the customer's growth strategy.
                
                ## Deliverable
                A comprehensive review of the customer's automation strategy and maturity, highlighting key insights that will inform the account plan.
            """),
            agent=agent
        )
```