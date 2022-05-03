import files
import logging
import bot
import commands
from telegram.ext import CommandHandler, MessageHandler, Filters
from urllib import error,request


CONF_FOLDER_NAME = "conf"
CONF_FILE_NAME = "abooboo_bot.conf"
TELEGRAM_DOMAIN = "https://api.telegram.org"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Initial:
    def __init__(self) -> None:
        self.fileService = files.FileService()

    def check(self):
        if not self.fileService.checkFolder(CONF_FOLDER_NAME):
            logging.debug("config folder doesn't exist, trying to create one")
            if not self.fileService.createFolder(CONF_FOLDER_NAME):
                logging.debug("unable to create a config folder, check the permissions")
                return False
            self.createDefaultConfig()
            logging.info("created new folder and config file, go modifying it and rerun")
            return False
            
        elif not self.fileService.checkFileInFolder(CONF_FILE_NAME,CONF_FOLDER_NAME):
            logging.debug("config file doesn't exist, creating a new one")
            self.createDefaultConfig()
            logging.info("created new config file, go modifying it and rerun ")
            return False
        elif not self.checkToken():
            logging.error("token not present or not valid, check the configuration file")
            return False
        elif not self.checkTelegramConnection():
            logging.error("unable to connect to telegram api")
            return False


        return True
    
    def createDefaultConfig(self):
        conf = files.ConfigService(CONF_FOLDER_NAME,CONF_FILE_NAME)
        conf.addValue("TOKEN","telegramtoken","replace-me")
        conf.addValue("SETTINGS","randomReply","False")
        conf.addValue("SETTINGS","probabilityToReply","1000")
        conf.saveConfig()


    def checkToken(self):
        conf = files.ConfigService(CONF_FOLDER_NAME,CONF_FILE_NAME)
        conf.readConfig()
        return True if conf.getValue("TOKEN","telegramtoken")!= "" and conf.getValue("TOKEN","telegramtoken")!= "replace-me" else False

    def checkTelegramConnection(self):
        try:
            request.urlopen(TELEGRAM_DOMAIN, timeout=1)
            return True
        except error.URLError as err: 
            return False
    
    def getBotToken(self):
        conf = files.ConfigService(CONF_FOLDER_NAME,CONF_FILE_NAME)
        conf.readConfig()
        return conf.getValue("TOKEN","telegramtoken")

    def initBot(self):
        self.bot = bot.Abooboo(self.getBotToken())
    
    def addAllCommands(self):
        self.bot.addHandler(CommandHandler("start",commands.start))
        self.bot.addHandler(CommandHandler("help",commands.help))
        self.bot.addHandler(CommandHandler("insulta",commands.insulta))
        self.bot.addHandler(MessageHandler( (Filters.text & ~Filters.command) | Filters.photo | Filters.sticker , commands.messages,edited_updates= True))
    
    def startBot(self):
        self.bot.startBot()

