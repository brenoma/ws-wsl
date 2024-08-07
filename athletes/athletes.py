import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
DOMAIN = os.getenv('DOMAIN_URL')
PATH = os.getenv('PATH_URL')
URL = f'{DOMAIN}/{PATH}'
HEADERS = {'User-Agent': 'Mozilla/5.0'}
PARAMETERS = {
}


def get_page_content(url: str, headers: dict, parameters: dict) -> BeautifulSoup:
    response = requests.get(URL, headers=HEADERS, params=PARAMETERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


page = get_page_content(URL, HEADERS, PARAMETERS)
table = page.find('div', class_='content-main')
rows = table.find_all('div', class_='tooltip-item avatar avatar--system avatar--directory')
athletes = []

for row in rows:
    name = row.find('a', class_='athlete-name').text
    country = row.find('span', class_='athlete-country-name').text
    photoUrl = row.find('a', class_='headshot proxy-img')['data-img-src']
    athletes.append({
        "name": name,
        "country": country,
        "photoUrl": photoUrl
    })

print(athletes)
