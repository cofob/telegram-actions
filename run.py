import os
import requests
from urllib.parse import urlencode
import json

# Get the telegram client specific values from env
TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["BOT_CHAT_ID"]
IGNORE_FROM = os.getenv("BOT_IGNORE")

# Get the github event specific values from env
GITHUB_SERVER_URL = os.getenv("GITHUB_SERVER_URL")
REPOSITORY = os.getenv("GITHUB_REPOSITORY")
GITHUB_ACTOR = os.getenv("GITHUB_ACTOR")
GITHUB_EVENT_NAME = os.getenv("GITHUB_EVENT_NAME")
EVENT_NAME = os.getenv("GITHUB_EVENT_NAME")
PR_NUMBER = os.getenv("INPUT_PR_NUMBER")
PR_TITLE = os.getenv("INPUT_PR_TITLE")
PR_BODY = os.getenv("INPUT_PR_BODY")
ISSUE_TITLE = os.getenv("INPUT_ISSUE_TITLE")
ISSUE_NUMBER = os.getenv('INPUT_ISSUE_NUMBER')
ISSUE_BODY = os.getenv('INPUT_ISSUE_BODY')
REPO_FORK_COUNT = os.getenv('INPUT_REPO_FORK_COUNT')
REPO_WATCH_COUNT = os.getenv('INPUT_REPO_WATCH_COUNT')

try:
    IGNORE = json.loads(IGNORE_FROM)
except:
    IGNORE = []

if GITHUB_ACTOR in IGNORE:
    raise Exception('Ignoring actor')

repo_url = f"{GITHUB_SERVER_URL}/{REPOSITORY}"
response = f"Hello there, \n"

# Process the event and prepare Telegram message payload
media_url_for_avatar = f"{GITHUB_SERVER_URL}/{GITHUB_ACTOR}.png"
if GITHUB_EVENT_NAME == "push":
    response += f"There is a new <b>push</b> in your repository <b>{REPOSITORY}</b> by <b>{GITHUB_ACTOR}</b>.\n\n"
    response += f"<b>Repository URL</b>: {repo_url}"
elif GITHUB_EVENT_NAME == "pull_request":
    pr_url = f"{repo_url}/pull/{PR_NUMBER}"
    response += f"A new event was triggered for a <b>Pull Request</b> in your repository <b>{REPOSITORY}</b>.\n\n"
    response += f"<b>PR Number</b>: <code>#{PR_NUMBER}</code>\n"
    response += f"<b>PR Title</b> : <code>{PR_TITLE}</ode>\n"
    response += f"<b>PR User</b>  : <code>{GITHUB_ACTOR}</code>\n"
    response += f"<b>PR Body</b>  : <code>{PR_BODY}</code>\n\n"
    response += f"<b>Check it out</b>: {pr_url}\n"
    response += f"<b>Repository URL</b>: {repo_url}"
elif GITHUB_EVENT_NAME == "issues":
    issue_url = f"{repo_url}/issues/{ISSUE_NUMBER}"
    response += f"A new event was triggered for an <b>Issue</b> in your repository <b>{REPOSITORY}</b>.\n\n"
    response += f"<b>Issue Number</b>: <code>#{ISSUE_NUMBER}</code>\n"
    response += f"<b>Issue Title</b> : <code>{ISSUE_TITLE}</code>\n"
    response += f"<b>Issue User</b>  : <code>{GITHUB_ACTOR}</code>\n"
    response += f"<b>Issue Body</b>  : <code>{ISSUE_BODY}</code>\n\n"
    response += f"<b>Check it out</b>: {issue_url}\n"
    response += f"<b>Repository URL</b>: {repo_url}"
elif GITHUB_EVENT_NAME == "fork":
    response += f"Your repository <b>{REPOSITORY}</b> was forked by <b>{GITHUB_ACTOR}</b>.\n"
    response += f"Current fork count: <b>{REPO_FORK_COUNT}</b>\n\n"
    response += f"<b>Repository URL</b>: {repo_url}"
elif GITHUB_EVENT_NAME == "watch":
    response += f"Your repository <b>{REPOSITORY}</b> is now watched by <b>{GITHUB_ACTOR}</b>.\n"
    response += f"Current watch count: <b>{REPO_WATCH_COUNT}</b>\n\n"
    response += f"<b>Repository URL</b>: {repo_url}"
else:
    response += f"A new <b>{GITHUB_EVENT_NAME}</b> event was triggered by " \
                f"<b>{GITHUB_ACTOR}</b> in your repository <b>{REPOSITORY}</b>\n\n"
    response += f"<b>Repository URL</b>: {repo_url}"

# Prepare and send the message payload
media_url = media_url_for_avatar if media_url_for_avatar else None
body = response

base_url = f'https://api.telegram.org/bot{TOKEN}/{"sendPhoto?" if media_url else "sendMessage?"}'

args = {'chat_id': CHAT_ID,
        'parse_mode': 'html'}

if media_url:
    args['caption'] = body
    args['photo'] = media_url
else:
    args['text'] = body

r = requests.get(base_url+urlencode(args))
print('status -> '+str(r.status_code))
print('args -> '+str(args))
