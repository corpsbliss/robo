import requests

# Jira API details
JIRA_DOMAIN = "https://YOUR_JIRA_DOMAIN.atlassian.net"  # Replace with your Jira domain
ISSUE_ID = "EVERREQ-23242"  # Replace with your Jira issue ID
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your OAuth 2.0 access token

# Jira API endpoint to get issue details
url = f"{JIRA_DOMAIN}/rest/api/3/issue/{ISSUE_ID}"

# Headers with Bearer token authentication
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Accept": "application/json"
}

# Send GET request
response = requests.get(url, headers=headers)

# Check response
if response.status_code == 200:
    issue_data = response.json()

    # Extract specific details
    ticket_id = issue_data.get("key", "N/A")
    summary = issue_data["fields"].get("summary", "N/A")
    description = issue_data["fields"].get("description", "N/A")
    status = issue_data["fields"]["status"].get("name", "N/A")
    assignee = issue_data["fields"].get("assignee", {}).get("displayName", "Unassigned")
    reporter = issue_data["fields"].get("reporter", {}).get("displayName", "Unknown")
    created = issue_data["fields"].get("created", "N/A")
    updated = issue_data["fields"].get("updated", "N/A")

    # Print issue details
    print(f"Ticket ID: {ticket_id}")
    print(f"Summary: {summary}")
    print(f"Description: {description}")
    print(f"Status: {status}")
    print(f"Assignee: {assignee}")
    print(f"Reporter: {reporter}")
    print(f"Created: {created}")
    print(f"Updated: {updated}")

else:
    print(f"Failed to fetch Jira issue. Status Code: {response.status_code}, Response: {response.text}")