import requests
from bs4 import BeautifulSoup

def search(task):
    URL = "https://www.google.com/search?q=" + task
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(URL, headers=header)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find(class_="Z0LcW t2b5Cf").getText()
    return result
