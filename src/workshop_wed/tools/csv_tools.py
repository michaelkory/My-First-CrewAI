#csv_tools.py

from langchain.tools import tool
import pandas as pd
import logging

@tool
def find_assessment_by_date(target_date: str) -> str:
    """
    Retrieves the title for the assessment that matches a given date from a hardcoded CSV file.
    Args:
        target_date (str): The specific date to find the matching assessment title.
                           The date should be in the format 'MM/DD/YY'.
    Returns:
        str: The title of the assessment if a match is found; otherwise, an empty string.
    Notes:
        This function reads from a CSV file located at 'src/workshop_wed/resources/assessment.csv'.
        The CSV must have at least two columns: 'Date' and 'Assessment Title', where 'Date' is expected
        to be in 'MM/DD/YYYY' format.
    """
    file_path = 'src/workshop_wed/resources/assessment.csv'  # Hardcoded path to the CSV file
    try:
        # Read the CSV with date parsing directly in the read_csv call
        courses_df = pd.read_csv(file_path, parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x.strip(), format='%m/%d/%y', errors='coerce'))
        # Convert the target date similarly
        target_date_parsed = pd.to_datetime(target_date.strip(), format='%m/%d/%y', errors='coerce')
        matching_course = courses_df[courses_df['Date'] == target_date_parsed]

        if not matching_course.empty:
            return matching_course['Assessment Title'].iloc[0]
    except Exception as e:
        logging.error(f"An error occurred while trying to fetch the assessment URL: {str(e)}")
    return ""

@tool
def find_training_by_date(target_date: str) -> str:
    """
    Retrieves the URL for a training that matches a given date from a hardcoded CSV file.

    Args:
        target_date (str): The specific date to find the matching course URL. 
                           The date should be in the format 'MM/DD/YY'.

    Returns:
        str: The URL of the course if a match is found; otherwise, an empty string.

    Notes:
        This function reads from a CSV file located at 'src/workshop_wed/resources/training.csv'.
        The CSV must have at least two columns: 'Date' and 'Training URL', where 'Date' is expected
        to be in 'MM/DD/YY' format.
    """
    file_path = 'src/workshop_wed/resources/training.csv'
    try:
        # Read the CSV with date parsing directly in the read_csv call
        courses_df = pd.read_csv(file_path, parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x.strip(), format='%m/%d/%y', errors='coerce'))
        # Convert the target date similarly
        target_date_parsed = pd.to_datetime(target_date.strip(), format='%m/%d/%y', errors='coerce')
        matching_course = courses_df[courses_df['Date'] == target_date_parsed]

        if not matching_course.empty:
            return matching_course['Training URL'].iloc[0]
    except Exception as e:
        logging.error(f"An error occurred while trying to fetch the training URL: {str(e)}")
    return ""