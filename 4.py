import requests

# Jira API details
JIRA_DOMAIN = "https://YOUR_JIRA_DOMAIN.atlassian.net"  # Replace with your Jira domain
PROJECT_KEY = "EVERREQ"  # Your project key
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Your OAuth 2.0 access token

# Jira API endpoint to fetch issues
url = f"{JIRA_DOMAIN}/rest/api/2/search"

# Headers with Bearer token authentication
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/json"
}

# JQL query to fetch only "To Do" and "In Progress" tickets
params = {
    "jql": f'project={PROJECT_KEY} AND status in ("To Do", "In Progress")',
    "maxResults": 100,  # Adjust as needed
    "fields": "summary,description,status,assignee,reporter,created,updated"
}

# Send GET request
response = requests.get(url, headers=headers, params=params)

# Check response
if response.status_code == 200:
    issues = response.json().get("issues", [])

    if not issues:
        print("No 'To Do' or 'In Progress' tickets found.")
    else:
        # Loop through filtered issues and print details
        for issue in issues:
            ticket_id = issue["key"]
            fields = issue["fields"]
            summary = fields.get("summary", "N/A")
            description = fields.get("description", "N/A")
            status = fields.get("status", {}).get("name", "N/A")
            assignee = fields.get("assignee", {}).get("displayName", "Unassigned")
            reporter = fields.get("reporter", {}).get("displayName", "Unknown")
            created = fields.get("created", "N/A")
            updated = fields.get("updated", "N/A")

            print(f"Ticket: {ticket_id}")
            print(f"Summary: {summary}")
            print(f"Description: {description}")
            print(f"Status: {status}")
            print(f"Assignee: {assignee}")
            print(f"Reporter: {reporter}")
            print(f"Created: {created}")
            print(f"Updated: {updated}")
            print("-" * 50)

else:
    print(f"Failed to fetch Jira issues. Status Code: {response.status_code}, Response: {response.text}")