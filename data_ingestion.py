import requests
from requests.exceptions import ConnectionError, Timeout
import time


def collect_url_data(url, retries=3, backoff_factor=0.3):
    """
    Collect data about the URL with retry mechanism.
    This could be user input or an automated check.
    """
    for i in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.content, response.status_code
        except (ConnectionError, Timeout) as e:
            if i < retries - 1:  # Retry up to retries times
                time.sleep(backoff_factor * (2 ** i))  # Exponential backoff
            else:
                print(f"Failed to retrieve {url}: {e}")
                return None, None


def label_url(url):
    """
    Placeholder function to label the URL.
    This could be based on user feedback or predefined rules.
    For now, a dummy implementation is used.
    """
    safe = "yes" if "kids" in url else "no"
    return safe


def get_data():
    urls = ["http://example.com", "http://carter.tech"]
    data = []

    for url in urls:
        content, status = collect_url_data(url)
        if content is not None and status is not None:
            label = label_url(url)
            data.append((url, content, label))

    return data
