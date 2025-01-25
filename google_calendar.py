import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the OAuth 2.0 scopes
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Load or create credentials
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES  # update this with yours " client_secret.json " 
        )
        creds = flow.run_local_server(port=8080)
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Build the Google Calendar service
service = build('calendar', 'v3', credentials=creds)

# Load events from the JSON file
with open('events.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

# Iterate over each event and add it to Google Calendar
for event in events:
    event_body = {
        'summary': event['summary'],
        'description': event['description'],
        'start': {
            'dateTime': event['start']['dateTime'],
            'timeZone': event['start']['timeZone'],
        },
        'end': {
            'dateTime': event['end']['dateTime'],
            'timeZone': event['end']['timeZone'],
        },
        'location': event.get('location', '')
    }

    # Insert the event into the calendar
    event_result = service.events().insert(calendarId='primary', body=event_body).execute()
    print(f"Event created: {event_result['htmlLink']}")
