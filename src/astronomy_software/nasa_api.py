import requests

def get_apod():
    """
    Fetches the Astronomy Picture of the Day (APOD) from the NASA API.

    Returns:
        dict: A dictionary containing the APOD data, or None if the request fails.
    """
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
