from slack import WebClient
from odinbot import OdinBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

# Get a new NestorBot
odin_bot = OdinBot("#general")

# Get the onboarding message payload
message = odin_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)
