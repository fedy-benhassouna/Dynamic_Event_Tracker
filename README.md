# Dynamic Event Tracker

Dynamic Event Tracker is a Python-based web scraping tool that extracts event information from a specified webpage and saves it to a JSON file. The extracted events can then be added to Google Calendar using the Google Calendar API.

## Features

- Scrapes event information from a specified webpage.
- Extracts event details such as summary, description, start time, end time, and location.
- Saves the extracted events to a JSON file.
- Adds the events to Google Calendar using the Google Calendar API.

## Prerequisites

- Python 3.x
- Google API credentials for accessing the Google Calendar API

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/fedy-benhassouna/dynamic-event-tracker.git
    cd dynamic-event-tracker
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv myenv
    myenv\Scripts\activate  # On Windows
    source myenv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Obtain Google API credentials:
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing project.
    - Enable the Google Calendar API for the project.
    - Create OAuth 2.0 Client ID credentials for a web application.
    - Download the `client_secret.json` file and place it in the project directory.

## Usage

1. Update the URL in [app.py](http://_vscodecontentref_/0) to the webpage you want to scrape:
    ```python
    url = 'URL_DE_LA_PAGE'
    ```
2. Update the client_secret.json in [google_calendar.py](http://_vscodecontentref_/0) to the client secret you get from google cloud console :
    ```python
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES )
    ```

3. Run the [app.py](http://_vscodecontentref_/1) script to scrape the events and save them to [events.json](http://_vscodecontentref_/2):
    ```bash
    python app.py
    ```

4. Run the [google_calendar.py](http://_vscodecontentref_/3) script to add the events to Google Calendar:
    ```bash
    python google_calendar.py
    ```

## Files

- [app.py](http://_vscodecontentref_/4): Script to scrape event information from a webpage and save it to [events.json](http://_vscodecontentref_/5).
- [google_calendar.py](http://_vscodecontentref_/6): Script to add events from [events.json](http://_vscodecontentref_/7) to Google Calendar.
- [events.json](http://_vscodecontentref_/8): JSON file containing the scraped event information.
- `client_secret.json`: Google API credentials file (not included in the repository).

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): Library for web scraping.
- [Google API Client](https://github.com/googleapis/google-api-python-client): Library for accessing Google APIs.
