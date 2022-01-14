import os
import logging
import configparser


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class FileService:
    def __init__(self) -> None:
        pass

    def checkFolderAbsolutePath(self,folderName):
        return os.path.isdir(folderName)
    
    def checkFolder(self,folderName):
        folderName = "./"+folderName
        return self.checkFolderAbsolutePath(folderName)
    
    def checkFileInFolder(self,fileName,folderName):
        return self.checkFile(folderName+"/"+fileName)

    def checkFile(self,fileName):
        fileName = "./"+fileName
        return self.checkFileAbsolutePath(fileName)

    def checkFileAbsolutePath(self,fileName):
        return os.path.isfile(fileName)

    def createFolder(self,folderName):
        folderName = "./"+folderName
        return self.createFolderAbsolutePath(folderName)

    def createFolderAbsolutePath(self,folderName):
        try:
            os.mkdir(folderName)
        except OSError:
            logging.error("Creation of the directory %s failed" % folderName)
            return False
        else:
            logging.debug("Creation of the directory %s successfull" % folderName)
            return True

class ConfigService:
    def __init__(self,folderName,fileName) -> None:
        self.folderName = folderName
        self.fileName = fileName
        self.configs = configparser.ConfigParser()
    
    def addValue(self,section,property,value):
        if not self.configs.has_section(section):
            self.configs.add_section(section)
        self.configs[section][property] = value

    def setFolderAndFile(self,folderName,fileName):
        self.folderName = folderName
        self.fileName = fileName

    def getValue(self,section,property):
        if not self.configs.has_section(section):
            return ""
        if self.configs[section].get(property) is None:
            return ""
        return self.configs[section][property]
        

    def readConfig(self):
        self.configs.read(self.folderName+"/"+self.fileName)

    def saveConfig(self):
        with open(self.folderName+"/"+self.fileName, 'w') as configfile:
            self.configs.write(configfile)