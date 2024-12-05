import streamlit as st
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Configuration for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'path/to/your/service_account.json'

# Authenticate and create the Calendar API client
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('calendar', 'v3', credentials=credentials)

def get_events(start_time, end_time):
    """Fetch events from Google Calendar within the specified time range."""
    try:
        events_result = service.events().list(
            calendarId='primary',
            timeMin=start_time.isoformat() + 'Z',
            timeMax=end_time.isoformat() + 'Z',
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        return events_result.get('items', [])
    except HttpError as error:
        st.error(f"An error occurred: {error}")
        return []

def display_events(events):
    """Display events in Streamlit."""
    if not events:
        st.write("No events found.")
        return

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        end = event['end'].get('dateTime', event['end'].get('date'))
        st.write(f"**{event['summary']}**")
        st.write(f"- Start: {start}")
        st.write(f"- End: {end}")
        if 'location' in event:
            st.write(f"- Location: {event['location']}")
        st.write('---')

def main():
    st.title("Google Calendar Event Viewer")

    # Get the current date
    today = datetime.now().date()

    # Define time range
    start_date = st.date_input("Start Date", today)
    end_date = st.date_input("End Date", today + timedelta(days=7))

    if st.button("Fetch Events"):
        start_time = datetime.combine(start_date, datetime.min.time())
        end_time = datetime.combine(end_date, datetime.max.time())
        events = get_events(start_time, end_time)
        display_events(events)

if __name__ == "__main__":
    main()
