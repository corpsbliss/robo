from jira import JIRA
import json

# Jira server URL, username, and API token
JIRA_SERVER = 'https://your-jira-instance.atlassian.net'
JIRA_USERNAME = 'your-email@example.com'
JIRA_API_TOKEN = 'your-api-token'

# Initialize JIRA client
jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))

# Specify the ticket key (e.g., 'PROJECT-123')
ticket_key = 'PROJECT-123'

# Fetch the ticket details
ticket = jira.issue(ticket_key)

# Extract relevant details
ticket_details = {
    'Key': ticket.key,
    'Summary': ticket.fields.summary,
    'Description': ticket.fields.description,
    'Status': ticket.fields.status.name,
    'Assignee': ticket.fields.assignee.displayName if ticket.fields.assignee else 'Unassigned',
    'Reporter': ticket.fields.reporter.displayName,
    'Created': ticket.fields.created,
    'Updated': ticket.fields.updated,
    'Priority': ticket.fields.priority.name,
    'Issue Type': ticket.fields.issuetype.name,
    'Labels': ticket.fields.labels,
    'Comments': [comment.body for comment in ticket.fields.comment.comments]
}

# Write the details to a text file
output_file = f'{ticket_key}_details.txt'
with open(output_file, 'w') as file:
    file.write(json.dumps(ticket_details, indent=4))

print(f"Ticket details have been written to {output_file}")