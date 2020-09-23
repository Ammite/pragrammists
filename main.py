import variables
import requests
from time import sleep

url = "https://api.telegram.org/bot" + variables.token + "/"


def get_updates():
    response = requests.get(url + "getUpdates")
    return response.json()


def get_last_update():
    results = get_updates()['result']
    total_updates = len(results) - 1
    if total_updates < 0:
        total_updates = 0
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_message(chat_id, message):
    parameters = {'chat_id': chat_id, 'text': message}
    response = requests.post(url + "sendMessage", data=parameters)
    return response


def main():

    last_update = get_last_update()
    chat_id = get_chat_id(last_update)
    text = last_update['message']['text']
    if text == "Првиет":
        send_message(chat_id, "Пока")


if __name__ == "__main__":
    main()
