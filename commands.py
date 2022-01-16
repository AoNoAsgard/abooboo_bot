from inspect import getmembers, isfunction
from telegram import Update, ForceReply
from telegram.ext import Updater, CallbackContext
from inspect import getmembers, isfunction
import messageToRespond

listOfFunctionForMessages = []

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Ciao {user.mention_markdown_v2()}\!',
    )


def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('non ho ancora una lista di comandi')



def messages(update: Update, context: CallbackContext) -> None:
    for name,functionForMessage in listOfFunctionForMessages:
        functionForMessage(update)



listOfFunctionForMessages = getmembers(messageToRespond,isfunction)
