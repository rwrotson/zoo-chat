from time import sleep
from telegram.constants import PARSEMODE_MARKDOWN_V2


def send_info_messages(context, update, texts):
    for _, text in texts.items():
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=text,
            parse_mode=PARSEMODE_MARKDOWN_V2
        )
        sleep(0.4)


def get_authorized_users(path):
    with open(path, 'r') as file:
        string = file.read()
        if string == '':
            return []
        return string[:-2].split(', ')

