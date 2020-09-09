import configparser as cp
import datetime as dt
from slack import WebClient
from slack.errors import SlackApiError

cfg = cp.ConfigParser()
cfg.read('config.ini')

TOKEN = cfg["default"]["token"]


def _get_web_client():
    client = WebClient(token=TOKEN)
    return client


def post_message(target, message):
    try:
        client = _get_web_client()
        response = client.chat_postMessage(channel=target, text=message)
        return response
    except SlackApiError as e:
        print(f"Failure: {e.response['error']}")


def post_file(target, filepath):
    try:
        client = _get_web_client()
        response = client.files_upload(channels=target, file=filepath)
        return response
    except SlackApiError as e:
        print(f"Failure: {e.response['error']}")


def post_notification(target, message):
    today = dt.date.today()
    first = dt.date(today.year, 1, 1)
    last = dt.date(today.year, 12, 31)

    days_passed = (today-first).days
    days_remaining = (last-today).days

    header = "*[Attention]*"
    elapsed = f"`Days since start of year: {days_passed}`"
    remainder = f"`Days until end of year: {days_remaining}`"

    notification = f"{header} \n{message} \n{elapsed} \n{remainder}"
    response = post_message(target, notification)
    return response


def post_notifications(target, messages):
    responses = [post_notification(target, message) for message in messages] 
    return responses