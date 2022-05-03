import random
from types import NoneType
import utilities
import logging
import files

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

CONF_FOLDER_NAME = "conf"
CONF_FILE_NAME = "abooboo_bot.conf"

listTypesHi = ["ciao", "salve"]
listOfReplyForHi =["Ciao anche a te","Salve salvino", "Ciao tizio","Ciao :D"]

listOfReplyForEmoji =["TI BANNO","NON SI FA", "AAAAAAAAAAAAAAAAAAAAAAAAAAA","CATTIVO BIMBO","VAI IN PUNIZIONE CATTIVO"]

listOfRandomReply =["Confermo","Ma sei sicuro?", "non ne sono sicuro","eh immagino","sisì","hahahahahahaha","che bello","sisì"]



def replyHi(update):
    if(update.message != None):
        message = update.message.text.lower();
        if(any(string in listTypesHi for string in message.split())):
            update.message.reply_text(random.choice(listOfReplyForHi))

def replyEmoji(update):
    
    if  update.edited_message != None:
        message = update.edited_message.text
    else:
        message = update.message.text;
    
    if(utilities.is_emoji(message)):
        if  update.edited_message != None:
            update.edited_message.reply_text(random.choice(listOfReplyForEmoji))
        else:
            update.message.reply_text(random.choice(listOfReplyForEmoji))

def oneOfX(update):
    config = files.ConfigService(CONF_FOLDER_NAME,CONF_FILE_NAME)
    config.readConfig()
    active =config.getValue("SETTINGS","randomReply")
    if active != "" and active == 'True':
        logging.debug("true")
        if random.randrange(int(config.getValue("SETTINGS","probabilityToReply"))) ==1:
            update.message.reply_text(random.choice(listOfRandomReply))
    
