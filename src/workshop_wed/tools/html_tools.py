import json
from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
from jinja2 import Environment, FileSystemLoader

def create_newsletter_html():
    # Define the paths
    output_file_path = 'src/workshop_wed/output/newsletter.html'
    json_file_path = 'src/workshop_wed/output/newsletter.json'
    template_dir = 'src/workshop_wed/resources'
    template_file_name = 'newsletter.j2'  # Just the template file name

    # Load the JSON data
    try:
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            newsletter_json = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} contains invalid JSON.")
        return None

    # Create a Jinja2 environment and render the template
    try:
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(template_file_name)
        rendered_html = template.render(newsletter_json=newsletter_json)
    except FileNotFoundError:
        print(f"Error: The template {template_file_name} does not exist in {template_dir}.")
        return None
    except Exception as e:
        print(f"An error occurred while rendering the template: {str(e)}")
        return None

    # Save the rendered HTML to a file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(rendered_html)
        print(f"Successfully saved the newsletter HTML to {output_file_path}")
        return rendered_html
    except IOError as e:
        print(f"An error occurred while saving the file: {str(e)}")
        return None