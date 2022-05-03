from inspect import getmembers, isfunction
import random
import logging
from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext
from inspect import getmembers, isfunction
import messages.messageToRespond as messageToRespond
from messages.messageToRespond import listOfReplyForEmoji
import messages.insults as insults
from utilities import is_emoji
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

listOfFunctionForMessages = []

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Ciao {user.mention_markdown_v2()}\!',
    )


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('non ho ancora una lista di comandi')



def messages(update: Update, context: CallbackContext) -> None:
    logging.debug("got new message")
    message = {}
    if update.message != None:
        message = update.message
    if update.edited_message != None:
        message = update.edited_message
    if message.caption != None:
        message_photo(update,context)
    elif message.sticker != None:
        if "emoji" in message.sticker.set_name.lower():
            update.message.reply_text(random.choice(listOfReplyForEmoji))
    else:
        for name,functionForMessage in listOfFunctionForMessages:
            functionForMessage(update)

def message_photo(update: Update, context: CallbackContext) -> None:
    if update.message != None:
        if is_emoji(update.message.caption):
            update.message.reply_text(random.choice(listOfReplyForEmoji))
    if update.edited_message != None:
        if is_emoji(update.edited_message.caption):
            update.edited_message.reply_text(random.choice(listOfReplyForEmoji))

def insulta(update: Update,context: CallbackContext)-> None:
    insults.insulta(update)

listOfFunctionForMessages = getmembers(messageToRespond,isfunction)
