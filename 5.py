import os
import requests

# Jira API details
JIRA_DOMAIN = "https://YOUR_JIRA_DOMAIN.atlassian.net"  # Replace with your Jira domain
PROJECT_KEY = "EVERREQ"  # Your project key
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Your OAuth 2.0 access token

# Directory to save the text files
output_dir = "jira_ticket_details"
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

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
        # Loop through filtered issues
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

            # Create a text file for each issue
            file_path = os.path.join(output_dir, f"{ticket_id}.txt")
            with open(file_path, "w") as file:
                file.write(f"Ticket: {ticket_id}\n")
                file.write(f"Summary: {summary}\n")
                file.write(f"Description: {description}\n")
                file.write(f"Status: {status}\n")
                file.write(f"Assignee: {assignee}\n")
                file.write(f"Reporter: {reporter}\n")
                file.write(f"Created: {created}\n")
                file.write(f"Updated: {updated}\n")
                file.write("-" * 50 + "\n")

            print(f"Details for {ticket_id} saved to {file_path}")

else:
    print(f"Failed to fetch Jira issues. Status Code: {response.status_code}, Response: {response.text}")