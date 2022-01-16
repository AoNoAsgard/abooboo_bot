from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

class Abooboo:
    def __init__(self,token):
        self.updater = Updater(token)
        self.dispatcher = self.updater.dispatcher
    
    def addHandler(self,commandHandler):
        self.dispatcher.add_handler(commandHandler)
    
    def startBot(self):
        self.updater.start_polling()
        self.updater.idle()

    def getBotUsername(self):
        return self.updater.bot.get_me().username
