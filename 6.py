import requests
import json

# Jira credentials
JIRA_URL = "https://your-jira-instance.atlassian.net"
EMAIL = "your-email@example.com"
API_TOKEN = "your-api-token"
ISSUE_KEY = "EVERREQ-12345"  # Replace with your Jira issue key

# Jira API URL to get available transitions
TRANSITIONS_URL = f"{JIRA_URL}/rest/api/3/issue/{ISSUE_KEY}/transitions"

# Make the API request
response = requests.get(
    TRANSITIONS_URL,
    auth=(EMAIL, API_TOKEN),
    headers={"Accept": "application/json"}
)

# Check if request was successful
if response.status_code == 200:
    transitions = response.json().get("transitions", [])
    
    # Print all transition names and IDs
    print("Available Transitions:")
    for transition in transitions:
        print(f"Name: {transition['name']}, ID: {transition['id']}")
    
    # Find the ID for "In Progress"
    in_progress_id = next((t['id'] for t in transitions if t['name'] == "In Progress"), None)
    
    if in_progress_id:
        print(f"\nTransition ID for 'In Progress': {in_progress_id}")
    else:
        print("\n'In Progress' transition not found.")
else:
    print(f"Failed to fetch transitions. Status Code: {response.status_code}, Response: {response.text}")