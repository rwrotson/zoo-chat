from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext

from bot.validation import validate_datetime
from bot.geo import get_location
from bot.utils import send_info_messages, get_authorized_users
from bot.consts import AUTH_USERS_PATH
from bot.texts import TEXTS
from bot.parser import get_totem


def start(update: Update, context: CallbackContext):
    """Send greeting message to user"""
    send_info_messages(context, update, TEXTS['start'])
        

def help(update: Update, context: CallbackContext):
    """Send command instructions to user"""
    send_info_messages(context, update, TEXTS['help'])


def password(update: Update, context: CallbackContext):
    """Receive password from user and test it"""
    user_id = str(update.message.chat.id)

    try:
        user_input = context.args[0]
    except IndexError:
        send_info_messages(context, update, TEXTS['password']['no_argument'])
        return None

    if user_input.strip().lower() == PASSWORD.strip().lower():
        if user_id in get_authorized_users(AUTH_USERS_PATH):
            send_info_messages(context, update, TEXTS['password']['already_logged_in'])
            return True
        with open(AUTH_USERS_PATH, 'a') as file:
            file.write(f'{user_id}, ')
        send_info_messages(context, update, TEXTS['password']['success'])
        return True

    send_info_messages(context, update, TEXTS['password']['failed'])
    return False


def send_credentials(update: Update, context: CallbackContext):
    """Receive date and place of birth from user and validate it"""
    user_id = str(update.message.chat.id)
    if user_id not in get_authorized_users(AUTH_USERS_PATH):
        send_info_messages(context, update, TEXTS['send_credentials']['not_auth'])
        return False
    try:
        validate_datetime(context.args)
    except AssertionError:
        send_info_messages(context, update, TEXTS['send_credentials']['no_arguments'])
        return None
    if len(context.args) == 3:
        date, time, place = context.args
        lat, long = get_location(place)
        lat = str(lat)
        long = str(long)
        print('lat:', lat, 'long:', long)
        if lat is None:
            send_info_messages(context, update, TEXTS['send_credentials']['not_found'])
            return None
        text = f'{date} {time} {lat}, {long}\nWait about 30 seconds to get totem animal!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        animal = get_totem(date, time, lat, long)
        print('animal3: ', animal)
        context.bot.send_message(chat_id=update.effective_chat.id, text=animal)
        return True
    date, time, lat, long = context.args
    return True
        





