from bs4 import BeautifulSoup

def parse_program(html):
    """
    Extract admission information from HTML.

    Parameters
    ----------
    html : str
        Raw HTML of the program page.

    Returns
    -------
    dict
        Extracted program information.
    """

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text().lower()

    data = {
        "deadline": None,
        "tuition": None,
        "gpa": None,
        "language": None,
        "exchange": None
    }

    # Detect keywords
    if "deadline" in text:
        data["deadline"] = "mentioned"

    if "tuition" in text:
        data["tuition"] = "mentioned"

    if "gpa" in text:
        data["gpa"] = "mentioned"

    if "ielts" in text or "toefl" in text:
        data["language"] = "mentioned"

    if "exchange" in text:
        data["exchange"] = "yes"

    return data
