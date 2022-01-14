import files
import logging


CONF_FOLDER_NAME = "conf"
CONF_FILE_NAME = "abooboo_bot.conf"
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
            
        return True
        

    
    def createDefaultConfig(self):
        conf = files.ConfigService(CONF_FOLDER_NAME,CONF_FILE_NAME)
        conf.addValue("TOKEN","telegramtoken","replace-me")
        conf.saveConfig()
    def checkToken(self):
        conf = files.ConfigService(CONF_FOLDER_NAME,CONF_FILE_NAME)
        conf.readConfig()
        return True if conf.getValue("TOKEN","telegramtoken")!= "" and conf.getValue("TOKEN","telegramtoken")!= "replace-me" else False
    
