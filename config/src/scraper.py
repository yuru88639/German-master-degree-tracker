import requests

def fetch_page(url):
    """
    Download HTML content from a webpage.

    Parameters
    ----------
    url : str
        The program webpage URL.

    Returns
    -------
    html : str
        HTML content if the request succeeds.
    """

    # Pretend to be a normal browser
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    # Check if request is successful
    if response.status_code == 200:
        return response.text

    print("Failed to fetch:", url)
    return None
