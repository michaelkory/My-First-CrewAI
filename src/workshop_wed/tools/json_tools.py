#json_tools.py

from langchain.tools import tool
import logging
import json

from tools.csv_tools import find_assessment_by_date

def get_section_from_json(section_key):
    """
    Reads a JSON file and extracts a specific section based on the provided key.
    
    Args:
        section_key (str): The key for the section to extract (e.g., 'workshop', 'training', 'assessment').
    
    Returns:
        dict: The dictionary corresponding to the section if found, otherwise None.
    """
    file_path = 'src/workshop_wed/output/newsletter.json'  # Hardcoded path to the JSON file
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
        # Extract the specified section from the JSON data
        if section_key in json_data:
            return json_data[section_key]
        else:
            logging.error(f"The section '{section_key}' does not exist in the provided JSON data.")
            return None
    except FileNotFoundError:
        logging.error(f"No file found at {file_path}")
        return None
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON from the file at {file_path}")
        return None

@tool
def find_assessment_by_title(target_date: str) -> dict:
    """
    Retrieves the details for the assessment that matches a given title from a hardcoded JSON file.
    
    Args:
        target_date (str): The specific date to find the matching assessment details.
        
    Returns:
        dict: A dictionary containing the title, description, and registration URL of the assessment if found; otherwise, an empty dictionary.
        
    Notes:
        This function reads from a JSON file located at 'src/workshop_wed/resources/assessments.json'.
        The JSON should have keys as assessment titles with values as another dictionary containing 'description' and 'registration'.
    """
    file_path = 'src/workshop_wed/resources/assessments.json'  # Hardcoded path to the JSON file

    target_title = find_assessment_by_date(target_date)

    if not target_title:
        logging.error(f"No assessment found for the date: {target_date}")
        return None

    try:
        with open(file_path, 'r') as file:
            assessments = json.load(file)
        
        # Check if the target title exists in the JSON data
        if target_title in assessments:
            return {
                "title": target_title,
                "description": assessments[target_title]['description'],
                "registration": assessments[target_title]['registration']
            }
        else:
            logging.info(f"No matching title found for: {target_title}")
            return {}
    except FileNotFoundError:
        logging.error(f"The file {file_path} does not exist.")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from the file {file_path}.")
        return {}
    except KeyError:
        logging.error(f"Missing expected keys in the JSON data for the title: {target_title}.")
        return {}
    
def initialize_json_file():
    # Define the path to the JSON file
    file_path = 'src/workshop_wed/output/newsletter.json'
    
    # JSON data to be written
    data = {
        "workshop": {},
        "training": {},
        "assessment": {},
        "ansible_blog": {},
        "ansible_video": {},
        "openshift_blog": {},
        "openshift_video": {},
        "rhel_blog": {},
        "rhel_video": {}
    }
    
    # Write the JSON data to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"JSON file initialized at {file_path}")

@tool
def update_json_file(data=None, **kwargs):
    """
    Updates a JSON file based on the provided data.

    Args:
        data (dict, optional): The input data containing the details to update in the JSON file.
        **kwargs: Additional keyword arguments (ignored).
    """
    file_path = 'src/workshop_wed/output/newsletter.json'  # Hardcoded path to the JSON file

    if not data or not isinstance(data, dict):
        logging.error("Invalid or no data provided to update_json_file.")
        return

    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        logging.info("File not found. Creating a new file.")
        existing_data = {}
    except json.JSONDecodeError:
        logging.error("Error decoding JSON. The file will be overwritten with new data.")
        existing_data = {}

    for key, value in data.items():
        if key in existing_data and isinstance(existing_data[key], dict) and isinstance(value, dict):
            # Merge dictionaries at the first level
            existing_data[key].update(value)
        else:
            # Add or replace the entire entry if not a dictionary merge
            existing_data[key] = value

    try:
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
            logging.info("Details updated successfully in JSON file.")
            return data
    except Exception as e:
        logging.error(f"Failed to update the JSON file: {str(e)}")