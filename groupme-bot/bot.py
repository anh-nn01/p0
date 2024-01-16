import requests
import time
import json
import os
import random
from dotenv import load_dotenv

load_dotenv()

BOT_ID = os.getenv("BOT_ID")
GROUP_ID = os.getenv("GROUP_ID")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")
API_KEY_GIPHY = os.getenv("API_KEY_GIPHY")
LAST_MESSAGE_ID = None


def send_message(text, attachments=None):
    """Send a message to the group using the bot."""
    post_url = "https://api.groupme.com/v3/bots/post"
    data = {"bot_id": BOT_ID, "text": text, "attachments": attachments or []}
    response = requests.post(post_url, json=data)
    return response.status_code == 202


def get_group_messages(since_id=None):
    """Retrieve recent messages from the group."""
    params = {"token": ACCESS_TOKEN}
    if since_id:
        params["since_id"] = since_id

    get_url = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages"
    response = requests.get(get_url, params=params)
    if response.status_code == 200:
        # this shows how to use the .get() method to get specifically the messages but there is more you can do (hint: sample.json)
        return response.json().get("response", {}).get("messages", [])
    return []


def process_message(message):
    """Process and respond to a message."""
    global LAST_MESSAGE_ID
    sender_type = message["sender_type"]
    text = message["text"].lower()
    name = message["name"]
    user_id = message['user_id']
    # print(message)

    if sender_type == "user" and ("hello bot" in text or "hi bot" in text): # response to 'hello bot' or 'hi bot' message from ANY user
        send_message("This is Anh's bot! How can I help you today?")
    elif sender_type == "user" and "good morning" in text: # response to 'good morning' from ANY user
        send_message(f"Good morning, {name}!")
    elif sender_type == "user" and "good night" in text:   # response to 'good night' from ANY user
        send_message(f"Good night, {name}!")
    # i.e. responding to a specific message (note that this checks if "hello bot" is anywhere in the message, not just the beginning)
    elif user_id == USER_ID and "shutdown" in text: # response to ONLY my message
        # response to 'shutdown' message ONLY if it is from me
        send_message("Please use Ctrl+C to shut me down!")
    elif sender_type == "user": # response to any other message by querying the GIPHY and return a gif ONLY if the message is from me
        GIPHY_params = {
            "api_key" : API_KEY_GIPHY,
            "q" : text,
            "offset" : random.randint(0, 10)
        }
        r = requests.get("http://api.giphy.com/v1/gifs/search", params=GIPHY_params)
        url = r.json()["data"][0]["bitly_gif_url"]
        send_message(url)

    # Update the last message ID to this message's ID
    LAST_MESSAGE_ID = message["id"]


def main():
    global LAST_MESSAGE_ID

    # this is an infinite loop that will try to read (potentially) new messages every 10 seconds, but you can change this to run only once or whatever you want
    # while True:
    #     messages = get_group_messages(LAST_MESSAGE_ID)
    #     for message in reversed(messages):
    #         process_message(message)
    #     # time.sleep(10)\

    messages = get_group_messages(LAST_MESSAGE_ID)
    # print(messages)
    if len(messages) > 0:
        LAST_MESSAGE_ID = messages[0]["id"]
    while True:
        messages = get_group_messages(LAST_MESSAGE_ID)
        for message in reversed(messages):
            process_message(message)
        # time.sleep(10)


if __name__ == "__main__":
    main()
