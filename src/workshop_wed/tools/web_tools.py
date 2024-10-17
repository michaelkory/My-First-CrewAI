from bs4 import BeautifulSoup
from datetime import datetime
from pytube import YouTube
import logging, pytz
import requests, re
import feedparser

from tools.csv_tools import find_summit_video_by_date, find_summit_blog_by_date, find_training_by_date

def get_blog_details_from_feed(url: str):
    """
    Fetches the most recent article from an RSS feed.

    Args:
        feed_url (str): URL of the RSS feed.

    Returns:
        dict: A dictionary containing the title, link, description, and publication date of the most recent article.
    """
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Check if the feed entries exist
    if feed.entries:
        latest_article = feed.entries[0]  # The first entry is the most recent one
        return {
            'title': latest_article.title,
            'description': latest_article.description,
            'published': latest_article.published,
            'link': latest_article.link
        }
    else:
        return None

def get_blog_details_from_url(date: str):
    blog_url = find_summit_blog_by_date(date)

    # Send a GET request to the URL
    response = requests.get(blog_url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the publication date
    published_tag = soup.find('meta', attrs={'name': 'last-publish-date'})

    # Extract the title, description, publication date, and URL
    details = {
        'title': soup.find('meta', property='og:title')['content'],
        'description': soup.find('meta', property='og:description')['content'],
        'published': published_tag['content'] if published_tag else None,
        'link': soup.find('meta', property='og:url')['content']
    }
    
    # Return the details in a dictionary
    return details

def get_training_details(target_date: str):
    training_url = find_training_by_date(target_date)

    if not training_url:
        logging.error(f"No training found for the date: {target_date}")
        return None

    try:
        response = requests.get(training_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title from the meta tag
        title_elem = soup.find("meta", property="og:title")
        title = title_elem["content"] if title_elem else "Title not available"

        # Navigate to the course description section
        desc_heading = soup.find("h2", text="Course description")
        description = ""
        if desc_heading:
            # Get following sibling paragraphs for the description
            for sibling in desc_heading.find_next_siblings():
                if sibling.name == "p" and sibling.has_attr("itemprop") and sibling["itemprop"] == "description":
                    description = sibling.text.strip().replace('\n', ' ')
                    break

        # Navigate to the course content summary section
        course_content_heading = soup.find("h3", text="Course content summary")
        course_content = ""
        if course_content_heading:
            course_content_parts = []
            current = course_content_heading.find_next_sibling()
            while current and current.name != "h3":  # Collect till next heading
                if current.name in ["p", "ul"]:
                    course_content_parts.append(current.text.strip().replace('\n', ' '))
                current = current.find_next_sibling()
            course_content = ' '.join(course_content_parts)  # Corrected variable name here

        # Use the provided URL as the registration link
        registration = training_url

        return {
            "title": title,
            "description": description,
            "course_content": course_content,
            "registration": registration
        }
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve the training page: {e}")
        return None
    except Exception as e:
        logging.error(f"An error occurred while parsing the training page: {e}")
        return None

def get_video_details_from_feed(url: str):
    """
    Extracts details of a YouTube video.
    Returns a dictionary with these details.
    """
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Check if the feed entries exist
    if feed.entries:
        latest_video = feed.entries[0]
        return {
            'title': latest_video.title,
            'description': latest_video.description,
            'published': latest_video.published,
            'link': latest_video.link
        }
    else:
        return None

def get_video_details_from_url(date: str):
    video_url = find_summit_video_by_date(date)
    
    # Create a YouTube object
    yt = YouTube(video_url)
    
    # Send a GET request to the video URL
    response = requests.get(video_url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the published date
    published_date = soup.find('meta', itemprop='datePublished')['content']
    
    # Extract the description using BeautifulSoup
    description_tag = soup.find('meta', property='og:description')
    description = description_tag['content'] if description_tag else None
    
    # Return the details in a dictionary
    return {
        'title': yt.title,
        'description': description,
        'published': published_date,
        'link': video_url
    }

def get_workshop_by_date(url: str, target_date: str) -> str:
    """
    Searches a given webpage for an event link that is associated with a specified date.

    Args:
        url (str): The URL of the webpage where the events are listed.
        target_date (str): The target date string to search for within the webpage. The function
                           expects this date to be in a format recognizable in the text of the webpage.

    Returns:
        str: The URL of the first matching event found that contains the target date in its text.
             Returns None if no such link is found.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Enhanced search to account for strong tags and direct text comparison
        for container in soup.find_all('div', class_="rc-cta-secondary"):
            date_text = container.find('strong').text if container.find('strong') else ''
            if target_date in date_text:
                link = container.find('a')
                if link and 'href' in link.attrs:
                    return link['href']
                else:
                    logging.debug(f"Link found but no href attribute present for date {date_text} in {container}")
        logging.warning(f"No matching event link found for the date '{target_date}'.")
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve the page: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    return None

def get_workshop_details(target_date: str, target_url: str):
    if not target_url:
        target_url = get_workshop_by_date("https://www.redhat.com/en/events/na-workshops-labs", target_date)

    if not target_url:
        logging.error(f"No workshop found for the date: {target_date}")
        return None
    
    try:
        response = requests.get(target_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract title
        title_elem = soup.find("h1", class_="rh-event-teaser-headline")
        title = title_elem.text.strip().replace('\n', ' ') if title_elem else "Title not available"

        # Extract overview text
        overview_section = soup.find('h2', text='OVERVIEW')
        overview_text = ""
        if overview_section and overview_section.next_sibling:
            overview_text = ' '.join([p.text for p in overview_section.find_next_sibling('div').find_all('p')])

        # Extract the event date and time
        date_time_elem = soup.find("div", class_="rh-event-teaser-date")
        if date_time_elem:
            date_time_text = date_time_elem.get_text(" ", strip=True)
            date_time_pattern = r'(\w+\s\d{1,2},\s\d{4})\s\|\s*(\d{1,2}:\d{2}\s(?:AM|PM))'
            match = re.search(date_time_pattern, date_time_text)
            if match:
                workshop_date = match.group(1)
                workshop_time = match.group(2)
                # Convert time string from Eastern to Pacific
                eastern = pytz.timezone("US/Eastern")
                pacific = pytz.timezone("US/Pacific")
                naive_datetime = datetime.strptime(f"{workshop_date} {workshop_time}", '%B %d, %Y %I:%M %p')
                eastern_datetime = eastern.localize(naive_datetime)
                pacific_datetime = eastern_datetime.astimezone(pacific)
                workshop_time = pacific_datetime.strftime('%I:%M %p')
                workshop_date = pacific_datetime.strftime('%m/%d/%Y')
    
                # Determine whether to use PDT or PST based on the date
                year = pacific_datetime.year
                dst_start = pacific.localize(datetime(year, 3, 8, 2, 0, 0), is_dst=True)
                dst_end = pacific.localize(datetime(year, 11, 1, 2, 0, 0), is_dst=True)
                if dst_start <= pacific_datetime < dst_end:
                    time_zone = "PDT"
                else:
                    time_zone = "PST"
                
                workshop_time += f" {time_zone}"
            else:
                workshop_date = "Date format not found"
                workshop_time = "Time format not found"
        else:
            workshop_date = "Date and time not available"
            workshop_time = "Time not available"

        return {
            "title": title,
            "overview": overview_text,
            "date": workshop_date,
            "time": workshop_time,
            "registration": target_url
        }
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve the page: {e}")
        return None
    except Exception as e:
        logging.error(f"An error occurred while parsing the workshop page: {e}")
        return None