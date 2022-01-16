import random
import utilities

listTypesHi = ["ciao", "salve"]
listOfReplyForHi =["Ciao anche a te","Salve salvino", "Ciao tizio","Ciao :D"]

listOfReplyForEmoji =["TI BANNO","NON SI FA", "AAAAAAAAAAAAAAAAAAAAAAAAAAA","CATTIVO BIMBO","VAI IN PUNIZIONE CATTIVO"]

def replyHi(update):
    message = update.message.text.lower();
    if(any(string in listTypesHi for string in message.split())):
        update.message.reply_text(random.choice(listOfReplyForHi))

def replyEmoji(update):
    if(utilities.is_emoji(update.message.text)):
        update.message.reply_text(random.choice(listOfReplyForEmoji))

