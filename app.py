import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime,timedelta
import json

# Étape 1 : Récupérer la page web
url = 'URL_DE_LA_PAGE' #update this with the webpage URL
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Étape 3 : Extraire les informations requises
events = []
rows = soup.select('table.top-events-table tbody tr')
for row in rows:
    date = row.find('td').text.strip()
    event = row.find('b', class_='ghref').text.strip()
    venue = row.find_all('td')[2].text.strip()
    data_href = row.find('b', class_='ghref')['data-href']
    
    # Étape 4 : Suivre le lien dans 'data-href' et récupérer la description
    event_response = requests.get(data_href)
    if event_response.status_code == 200:
        event_soup = BeautifulSoup(event_response.content, 'html.parser')
        event_description = event_soup.find('div', class_='event-description-html').get_text(separator=' ', strip=True)
    else:
        event_description = "Description non disponible"
    
    events.append({
        'summary': event,
        'description': event_description,
        'start': {
            'dateTime': datetime.strptime(date, '%d %b %Y').isoformat(),
            'timeZone': 'Africa/Tunis'
        },
        'end': {
            'dateTime': (datetime.strptime(date, '%d %b %Y') + timedelta(hours=1)).isoformat(),  # Assuming 1 hour duration
            'timeZone': 'Africa/Tunis'
        },
        'location': venue
    })

# Sauvegarder les événements dans un fichier JSON
with open('events.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=4)

print("Les événements ont été sauvegardés dans events.json.")
