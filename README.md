# Amazon-Code
Web Data Scraping - Top 2500 Tech Products on Amazon
This is my firs project that is a little more advanced. I feel confident on the code I have created but I am running in an issue.
The error message I'm receiving is:
"RefreshError: ('invalid_scope: Invalid OAuth scope or ID token audience provided.', {'error': 'invalid_scope', 'error_description': 'Invalid OAuth scope or ID token audience provided.'})"

I have followed the documentation and obtained the necessary credentials, but it seems that the authentication scopes are not sufficient for the Google Sheets API.

Here are the details of my setup:

I'm using the gspread library in Python to interact with the Google Sheets API.
I have generated a service account key file in JSON format.
I have authorized the service account with the necessary scopes for accessing Google Sheets.
I'm running the code on my local machine using the Chrome WebDriver for web scraping.
Despite these steps, I'm still facing the authentication issue mentioned above.
I finished this on 7/7/2023 will update read me file as I progress.
