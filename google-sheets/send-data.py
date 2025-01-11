from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz

# Get the timezone object for New York
tz_NY = pytz.timezone('America/New_York') 

# Get the current time in New York
datetime_format = f"{datetime.now(tz_NY).date()}  {datetime.now(tz_NY).strftime('%I:%M %p')}"

load_dotenv('data.env')

# The ID of the spreadsheet you want to update
SPREADSHEET_ID = os.getenv("SHEET_ID") 

# print(datetime_NY.strftime('%I:%M:%S %p'))


# os._exit(0)

# Define the range where you want to add data (e.g., A1)
RANGE_NAME = 'Sheet1!A1'

# Data you want to send to Google Sheets
values = [
    # ['Name', 'Age', 'Email'],  # Header row
    ['John Doe', '28', 'john.doe@example.com', f"{datetime_format}"],
    ['Jane Smith', '34', 'jane.smith@example.com', f"{datetime_format}"]
]

# Authenticate using the service account
creds = Credentials.from_service_account_file(
    'C:/Users/zachc/repos/python/sheets-append/analytics-dash.json',  # Replace with the path to your service account JSON file
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)

# Build the service
service = build('sheets', 'v4', credentials=creds)

# Prepare the body with data
body = {
    'values': values
}

try:
    # Update the sheet with data
    result = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',  # You can also use 'USER_ENTERED' for automatic formatting
        body=body,
        insertDataOption='INSERT_ROWS'  # Ensures that new rows are inserted    
    ).execute()

    print(f"{result.get('updates').get('updatedRows')} cells appended.")
except HttpError as err:
    print(f"Error: {err}")
