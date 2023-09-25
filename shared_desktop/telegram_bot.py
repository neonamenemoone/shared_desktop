import os

# Путь к файлу настроек Django проекта
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shared_desktop.settings")

# Загрузка настроек Django
import django

django.setup()

from board.models import Rule
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (CallbackQueryHandler, CommandHandler, Filters,
                          MessageHandler, Updater)

load_dotenv()

TGTOKEN = os.getenv("TGTOKEN")

if TGTOKEN is None:
    raise ValueError(
        "Убедитесь, что переменная окружения TGTOKEN установлена."
    )

updater = Updater(token=TGTOKEN, use_context=True)


def message(update, context):
    chat = update.effective_chat
    rules = Rule.objects.order_by("-pub_date")
    for rule in rules:
        message_text = f"{rule.name}\n\n{rule.text}"
        context.bot.send_message(chat_id=chat.id, text=message_text)

    keyboard = [
        [InlineKeyboardButton("Обновить информацию", callback_data="get_info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(
        chat_id=chat.id, text="...", reply_markup=reply_markup
    )


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name

    keyboard = [
        [InlineKeyboardButton("Получить информацию", callback_data="get_info")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=chat.id,
        text="Приветствуем, {}!".format(name),
        reply_markup=reply_markup,
    )


def button_click(update, context):
    query = update.callback_query
    query.answer()

    if query.data == "get_info":
        message(update, context)


updater.dispatcher.add_handler(CommandHandler("start", wake_up))
updater.dispatcher.add_handler(CallbackQueryHandler(button_click))


updater.dispatcher.add_handler(MessageHandler(Filters.text, message))

updater.start_polling()
updater.idle()
