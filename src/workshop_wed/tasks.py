from textwrap import dedent
from crewai import Task
import logging
import json

from tools.html_tools import create_newsletter_html
from tools.json_tools import get_section_from_json,find_assessment_by_title
from tools.web_tools import get_blog_details, get_training_details, get_video_details, get_workshop_details

class RedHatNewsletterCrewTasks:

    def summarize_workshop_task(self, agent, target_date):
        workshop_details = get_workshop_details(target_date)

        if not workshop_details:
            logging.error("Failed to fetch or parse workshop details.")
            return None
        
        # Update the summary in the workshop details
        workshop_details['summary'] = "*newly created summary goes here*"
        expected_output = json.dumps({"data": {"workshop": workshop_details}}, indent=4)
    
        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Step 1 - Summarize Upcoming Workshop Overview

                ## Objective
                Create a concise summary of the next upcoming Red Hat Workshop Wednesday, scheduled for {target_date}, for inclusion in the weekly newsletter.

                ## Instructions
                1. Review the detailed workshop information.
                2. Extract and summarize the key points from the workshop overview.
                3. Store the new summary in the provided JSON format under `workshop_details['summary']`.
                4. Return the updated `workshop_details` dictionary in JSON format as described.

                ## Expected Output Format
                The JSON-formatted output should look like this:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `workshop_details` dictionary, updated with the new 'summary', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, overview, date, time, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )

    def copywrite_workshop_task(self, agent):
        workshop_details = get_section_from_json("workshop")
        if not workshop_details:
            logging.error(f"Failed to fetch or parse Red Hat Training.")
            workshop_details = {}
        
        # Update the final_copy in the training details
        workshop_details['final_copy'] = "*newly created final_copy goes here*"
        expected_output = json.dumps({"data": {"workshop": workshop_details}}, indent=4)
        
        return Task(
            description=dedent(f"""
                # Red Hat Newsletter: Enhance Workshop Summary
                
                ## Objective 
                Refine the summary of the upcoming Red Hat Enterprise Linux Technical Workshop without altering the original content, creating an additional version for the weekly newsletter that is engaging and informative.

                ## Instructions
                - Start by reviewing the existing summary and the detailed overview provided.
                - Develop a 'final_copy' that:
                    - Constructs a new narrative structure to dynamically emphasize key points.
                    - Utilizes engaging and persuasive language to captivate the newsletter's audience.
                    - Highlights practical applications like cloud provisioning and system roles, making them relatable and appealing.
                - Ensure the 'final_copy' complements the existing 'summary', providing a clear, comprehensive, yet succinct depiction of the workshop's value.
                - Retain the original 'summary' in its entirety to serve as a reference or for other purposes.

                ## Expected Output Format
                Return the completed and updated `workshop_details` dictionary in the specified JSON format:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `workshop_details` dictionary, updated with the new 'final_copy', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, overview, date, time, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )
    
    def summarize_training_task(self, agent, target_date):
        training_details = get_training_details(target_date)
        if not training_details:
            logging.error("Failed to fetch or parse training details.")
            return None
        
        # Update the summary in the training details
        training_details['summary'] = "*newly created summary goes here*"
        expected_output = json.dumps({"data": {"training": training_details}}, indent=4)

        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Step 3 - Summarize Training Course Details

                ## Objective
                Create a concise summary of the Red Hat training to include in the weekly newsletter.

                ## Instructions
                1. Review the detailed training information.
                2. Extract and summarize the key points from the training description.
                3. Store the new summary in the provided JSON format under `training_details['summary']`.
                4. Return the updated `training_details` dictionary in JSON format as described.

                ## Expected Output Format
                The JSON-formatted output should look like this:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `training_details` dictionary, updated with the new 'summary', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, course_content, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )
    
    def copywrite_training_task(self, agent):
        training_details = get_section_from_json("training")
        if not training_details:
            logging.error(f"Failed to fetch or parse Red Hat Training.")
            training_details = {}
        
        # Update the final_copy in the training details
        training_details['final_copy'] = "*newly created final_copy goes here*"
        expected_output = json.dumps({"data": {"training": training_details}}, indent=4)
        
        return Task(
            description=dedent("""
                # Red Hat Newsletter Crew: Step 4 - Enhance Training Summary
                            
                ## Objective 
                Refine the summary of the upcoming Red Hat Training without altering the original content, creating an additional version for the weekly newsletter that is engaging and informative.

                ## Instructions
                - Start by reviewing the existing summary and the detailed course_content provided.
                - Develop a 'final_copy' that:
                    - Constructs a new narrative structure to dynamically emphasize key points.
                    - Utilizes engaging and persuasive language to captivate the newsletter's audience.
                    - Highlights practical applications like cloud provisioning and system roles, making them relatable and appealing.
                - Ensure the 'final_copy' complements the existing 'summary', providing a clear, comprehensive, yet succinct depiction of the training's value.
                - Retain the original 'summary' in its entirety to serve as a reference or for other purposes.

                ## Expected Output Format
                Return the completed and updated `training_details` dictionary in the specified JSON format:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `training_details` dictionary, updated with the new 'final_copy', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, course_content, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )
 
    def summarize_assessment_task(self, agent, target_date):
        assessment_details = find_assessment_by_title(target_date)
        if not assessment_details:
            logging.error("Failed to fetch or parse assessment details.")
            return None
        
        # Update the summary in the assessment details
        assessment_details['summary'] = "*newly created summary goes here*"
        expected_output = json.dumps({"data": {"assessment": assessment_details}}, indent=4)

        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Step 5 - Summarize Skills Assessment Details

                ## Objective
                Create a concise summary of the Red Hat Skills Assessment to include in the weekly newsletter.

                ## Instructions
                1. Review the detailed assessment information.
                2. Extract and summarize the key points from the assessment description.
                3. Store the new summary in the provided JSON format under `assessment_details['summary']`.
                4. Return the updated `assessment_details` dictionary in JSON format as described.

                ## Expected Output Format
                The JSON-formatted output should look like this:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `assessment_details` dictionary, updated with the new 'summary', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )
    
    def copywrite_assessment_task(self, agent):
        assessment_details = get_section_from_json("assessment")
        if not assessment_details:
            logging.error(f"Failed to fetch or parse Red Hat Skills Assessment.")
            assessment_details = {}
        
        # Update the final_copy in the assessment details
        assessment_details['final_copy'] = "*newly created final_copy goes here*"
        expected_output = json.dumps({"data": {"assessment": assessment_details}}, indent=4)
        
        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Step 6 - Enhance Skills Assessment
                            
                ## Objective 
                Refine the summary of the upcoming Red Hat Skills Assessment without altering the original content, creating an additional version for the weekly newsletter that is engaging and informative.

                ## Instructions
                - Start by reviewing the existing summary and the detailed course_content provided.
                - Develop a 'final_copy' that:
                    - Constructs a new narrative structure to dynamically emphasize key points.
                    - Utilizes engaging and persuasive language to captivate the newsletter's audience.
                    - Highlights practical applications like cloud provisioning and system roles, making them relatable and appealing.
                - Ensure the 'final_copy' complements the existing 'summary', providing a clear, comprehensive, yet succinct depiction of the assessment's value.
                - Retain the original 'summary' in its entirety to serve as a reference or for other purposes.

                ## Expected Output Format
                Return the completed and updated `assessment_details` dictionary in the specified JSON format:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `assessment_details` dictionary, updated with the new 'final_copy', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )

    def summarize_blog_task(self, agent, blog_channel, blog_key, blog_url):
        blog_details = get_blog_details(blog_url)
        if not blog_details:
            logging.error(f"Failed to fetch or parse {blog_channel} blog.")
            return None
        
        # Update the summary in the blog details
        blog_details['summary'] = "*newly created summary goes here*"
        expected_output = json.dumps({"data": {blog_key: blog_details}}, indent=4)
    
        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Summarize {blog_channel} Blog

                ## Objective
                Create a concise summary of the {blog_channel} Blog to include in the weekly newsletter.

                ## Instructions
                1. Review the detailed {blog_channel} Blog information.
                2. Extract and summarize the key points from the {blog_channel} Blog title and description.
                3. Incorporate the new summary into the `blog_details['summary']`.
                4. Ensure the entire `{blog_key}` dictionary, with all updated details including the new summary, is correctly formatted and returned in JSON format as described below.

                ## Expected Output Format
                You are required to return the complete `{blog_key}` dictionary with all details, not just the summary. The JSON-formatted output should look like this:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `{blog_key}` dictionary, updated with the new summary, formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, summary, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )
    
    def copywrite_blog_task(self, agent, blog_channel, blog_key):
        blog_details = get_section_from_json(blog_key)
        if not blog_details:
            logging.error(f"Failed to fetch or parse {blog_channel} blog.")
            blog_details = {}
        
        # Update the summary in the blog details
        blog_details['final_copy'] = "*newly created final_copy goes here*"
        expected_output = json.dumps({"data": {blog_key: blog_details}}, indent=4)

        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Enhance the Summary of the {blog_channel} Blog

                ## Objective
                Create a compelling 'final_copy' of the Red Hat {blog_channel} Blog to include in the weekly newsletter.

                ## Instructions
                1. Review the detailed Red Hat {blog_channel} Blog information.
                2. Extract and enhance the key points from the Red Hat {blog_channel} Blog title, description, and summary.
                3. Incorporate the new 'final_copy' into {blog_details['final_copy']}.
                4. Ensure the entire `{blog_key}` dictionary, with all updated details including the new 'final_copy', is correctly formatted and returned in JSON format as described below.

                ## Expected Output Format
                You are required to return the complete `{blog_key}` dictionary with all details, not just the summary. The JSON-formatted output should look like this:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `{blog_key}` dictionary, updated with the new 'final_copy', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, summary, and all other relevant fields updated as necessary.**
                """),
            expected_output=expected_output,
            agent=agent
        )

    def summarize_video_task(self, agent, video_channel, video_key, video_url):
        video_details = get_video_details(video_url)
        if not video_details:
            logging.error(f"Failed to fetch or parse {video_channel} video.")
            return None
        
        # Update the summary in the video details
        video_details['summary'] = "*newly created summary goes here*"
        expected_output = json.dumps({"data": {video_key: video_details}}, indent=4)
    
        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Summarize {video_channel} YouTube Video

                ## Objective
                Create a concise summary of the latest {video_channel} YouTube Video to include in the weekly newsletter.

                ## Instructions
                1. Review the detailed information about the YouTube video.
                2. Extract and summarize the key points from the YouTube video title and description.
                3. Incorporate the new summary into the `video_details['summary']`.
                4. Ensure the entire `{video_key}` dictionary, with all updated details including the new summary, is correctly formatted and returned in JSON format as described below.

                ## Expected Output Format
                You are required to return the complete `{video_key}` dictionary with all details, not just the summary. The JSON-formatted output should look like this:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `{video_key}` dictionary, updated with the new summary, formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, content, and all other relevant fields updated as necessary.**
            """),
            expected_output=expected_output,
            agent=agent
        )
    
    def copywrite_video_task(self, agent, video_channel, video_key):
        video_details = get_section_from_json(video_key)
        if not video_details:
            logging.error(f"Failed to fetch or parse {video_channel} video.")
            video_details = {}
        
        # Update the summary in the video details
        video_details['final_copy'] = "*newly created final_copy goes here*"
        expected_output = json.dumps({"data": {video_key: video_details}}, indent=4)

        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Enhance the Summary of the {video_channel} Blog

                ## Objective
                Create a compelling 'final_copy' of the Red Hat {video_channel} Blog to include in the weekly newsletter.

                ## Instructions
                1. Review the detailed Red Hat {video_channel} Blog information.
                2. Extract and enhance the key points from the Red Hat {video_channel} Blog summary, content, and description.
                3. Incorporate the new 'final_copy' into {video_details['final_copy']}.
                4. Ensure the entire `{video_key}` dictionary, with all updated details including the new summary, is correctly formatted and returned in JSON format as described below.

                ## Expected Output Format
                You are required to return the complete `{video_key}` dictionary with all details, not just the summary. The JSON-formatted output should look like this:
                ```json
                {expected_output}
                ```

                ## Deliverable
                A fully detailed `{video_key}` dictionary, updated with the new 'final_copy', formatted in JSON, and ready to be included in the weekly newsletter. 
                **This should include the title, description, content, and all other relevant fields updated as necessary.**
                """),
            expected_output=expected_output,
            agent=agent
        )
    
    def newsletter_html_task(self, agent):
        newsletter_html = create_newsletter_html()

        return Task(
            description=dedent(f"""
                # Red Hat Newsletter Crew: Final Review and Validation of Newsletter HTML

                ## Objective
                Perform a thorough review and validation of the HTML for the Workshop Wednesday Newsletter to ensure its accuracy and readiness for distribution.

                ## Instructions
                1. Carefully review the HTML content of the Red Hat Workshop Wednesday Newsletter.
                2. Check that the HTML is formatted properly, paying special attention to the use of tags and their nesting to ensure the structure is logically and visually correct.
                3. Validate the syntax to ensure there are no HTML errors such as unclosed tags, missing attributes, or deprecated elements that could affect the newsletter's rendering across different email clients.
                4. Confirm that all links, images, and multimedia elements are correctly embedded and functioning as expected.

                ## Expected Output Format
                You are required to return the complete, validated HTML file of the Workshop Wednesday Newsletter. The HTML must be well-formatted, syntactically correct, and ready to be used. Here is what the HTML should look like:
                ```html
                {newsletter_html}
                ```

                ## Deliverable
                A fully detailed, validated, and formatted HTML version of the Workshop Wednesday Newsletter, ready for deployment.
                """),
            expected_output=newsletter_html,
            agent=agent
        )
