import requests
import json

# Jira API details
JIRA_BASE_URL = "https://your-domain.atlassian.net"
JIRA_PROJECT_KEY = "EVERREQ"  # Change this to your Jira project key
JIRA_API_TOKEN = "your-api-token"
JIRA_USER_EMAIL = "your-email@example.com"

# Jira API endpoint to fetch issues
JIRA_API_URL = f"{JIRA_BASE_URL}/rest/api/3/search"

# Headers for authentication
HEADERS = {
    "Authorization": f"Basic {requests.auth._basic_auth_str(JIRA_USER_EMAIL, JIRA_API_TOKEN)}",
    "Accept": "application/json"
}

# JQL query to fetch all issues from the project
PARAMS = {
    "jql": f"project={JIRA_PROJECT_KEY}",
    "maxResults": 100,  # Adjust this as needed
    "fields": "summary,description,status,assignee,reporter,created,updated"
}

def fetch_jira_issues():
    """Fetch all Jira issues and save details to a text file."""
    response = requests.get(JIRA_API_URL, headers=HEADERS, params=PARAMS)

    if response.status_code == 200:
        issues = response.json().get("issues", [])
        with open("jira_tickets.txt", "w", encoding="utf-8") as file:
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

                file.write(f"Ticket: {ticket_id}\n")
                file.write(f"Summary: {summary}\n")
                file.write(f"Description: {description}\n")
                file.write(f"Status: {status}\n")
                file.write(f"Assignee: {assignee}\n")
                file.write(f"Reporter: {reporter}\n")
                file.write(f"Created: {created}\n")
                file.write(f"Updated: {updated}\n")
                file.write("-" * 50 + "\n")
        
        print("Jira ticket details have been saved to 'jira_tickets.txt'.")
    else:
        print(f"Failed to fetch Jira issues. Status Code: {response.status_code}, Response: {response.text}")

# Run the script
fetch_jira_issues()