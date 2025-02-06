import requests
import json

# Jira credentials
JIRA_DOMAIN = "https://YOUR_JIRA_DOMAIN.atlassian.net"
ISSUE_ID = "EVERREQ-23242"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# API Endpoint
url = f"{JIRA_DOMAIN}/rest/api/3/issue/{ISSUE_ID}/comment"

# Headers
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Comment payload
comment_data = {
    "body": "This is a test comment added via the Jira API."
}

# Send request
response = requests.post(url, headers=headers, data=json.dumps(comment_data))

# Check response
if response.status_code == 201:
    print("Comment added successfully!")
else:
    print(f"Failed to add comment. Status Code: {response.status_code}, Response: {response.text}")