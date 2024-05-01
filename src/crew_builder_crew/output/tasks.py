```
from textwrap import dedent
from crewai import Task

class NewCrewTasks:

    def crew_purpose_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 1 - Analyze Crew Purpose
                
                ## Objective
                Analyze the **crew purpose** to ensure it aligns with the **crew details**.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details 
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Carefully review the provided **crew purpose** and **crew details**.
                2. Identify any potential misalignments or gaps between the purpose and details.
                3. Suggest refinements to the purpose or details to ensure they are well-aligned.
                4. Document your analysis and recommendations in a concise report.
                
                ## Deliverable
                A report detailing the analysis of the crew purpose and crew details, along with recommendations for refinement.
            """),
            agent=agent
        )

    def crew_details_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 2 - Review Crew Details
                
                ## Objective
                Review the **crew details** to ensure they align with the **crew purpose**.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Carefully examine the provided **crew details**.
                2. Assess whether the details adequately describe the actions and deliverables needed to fulfill the **crew purpose**.
                3. Identify any gaps, inconsistencies, or areas that require further clarification.
                4. Document your review and provide recommendations for improving the crew details.
                
                ## Deliverable
                A report detailing the review of the crew details and recommendations for enhancement.
            """),
            agent=agent
        )

    def task_sequence_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 3 - Sequence the Tasks
                
                ## Objective
                Sequence the tasks logically to fulfill the **crew purpose** and **crew details**.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Review the task descriptions in the `task_list.yaml` file.
                2. Determine the optimal sequence of tasks to efficiently achieve the crew purpose and details.
                3. Identify any dependencies or prerequisites between tasks and adjust the sequence accordingly.
                4. Document the task sequence in a clear and organized manner.
                
                ## Deliverable
                A detailed task sequence plan that outlines the order and dependencies of the tasks.
            """),
            agent=agent
        )

    def error_detection_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 4 - Detect Errors
                
                ## Objective
                Conduct a comprehensive review to detect errors in the `task_list.yaml` file.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Thoroughly review the `task_list.yaml` file for any errors, inconsistencies, or missing information.
                2. Validate that the task descriptions, dependencies, and other metadata are accurate and complete.
                3. Identify any potential issues that could impact the successful execution of the crew.
                4. Document the findings of your review and provide recommendations for correcting any detected errors.
                
                ## Deliverable
                A report detailing the findings of the review and recommendations for correcting any detected errors.
            """),
            agent=agent
        )

    def crew_builder_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 5 - Build the Crew
                
                ## Objective
                Build the most excellent crewai crew for building crewai crews.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Use the task sequence plan to guide the building of the crew.
                2. Ensure that the crew is well-structured and easy to maintain.
                3. Implement feedback loops and review stages to incorporate iterative improvements.
                4. Document the building process and provide recommendations for future enhancements.
                
                ## Deliverable
                A fully built crewai crew that meets the crew purpose and details.
            """),
            agent=agent
        )

    def crew_review_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 6 - Review the Crew
                
                ## Objective
                Review the built crew to ensure it meets the crew purpose and details.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Carefully review the built crew to ensure it meets the crew purpose and details.
                2. Identify any gaps or inconsistencies between the crew and the purpose and details.
                3. Provide recommendations for improving the crew to better align with the purpose and details.
                4. Document the review and recommendations in a concise report.
                
                ## Deliverable
                A report detailing the review of the built crew and recommendations for improvement.
            """),
            agent=agent
        )

    def crew_deployment_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 7 - Deploy the Crew
                
                ## Objective
                Deploy the built crew to start building crewai crews.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Deploy the built crew to the production environment.
                2. Ensure that the crew is properly configured and ready for use.
                3. Provide documentation and training to ensure a smooth transition.
                4. Monitor the crew's performance and provide ongoing support.
                
                ## Deliverable
                A fully deployed crewai crew that is ready for use.
            """),
            agent=agent
        )

    def crew_monitoring_task(self, agent, crew_purpose, crew_details):
        return Task(
            description=dedent(f"""\
                # New CrewAI Crew: Step 8 - Monitor the Crew
                
                ## Objective
                Monitor the built crew to ensure it continues to meet the crew purpose and details.
                
                ## Crew Purpose
                <crew_purpose>{crew_purpose}</crew_purpose>
                
                ## Crew Details
                <crew_details>{crew_details}</crew_details>
                
                ## Instructions
                1. Continuously monitor the crew's performance and identify areas for improvement.
                2. Gather feedback from users and stakeholders to inform iterative improvements.
                3. Implement changes and updates to ensure the crew remains aligned with the purpose and details.
                4. Document the monitoring process and provide recommendations for future enhancements.
                
                ## Deliverable
                A report detailing the monitoring process and recommendations for future enhancements.
            """),
            agent=agent
        )
```