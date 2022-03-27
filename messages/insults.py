import random
from tokenize import String
from telegram import Update
import telegram as telegram


listOfInsultsToSelf =[
    "Sei così stupido che in una gara di stupido riusciresti comunque ad arrivare secondo",
    "Se cadessi in un fiume sarebbe una sfortuna. Ma se qualcuno ti ci tirasse fuori sarebbe una calamità", 
    "Ma sei scemo?",
    "Tua madre se ingoiava faceva una cosa buona quella notte",
    "Hai mai pensato di portarti dietro una pianta, così cerchi di compensare all'ossigeno che sprechi",
    "Tua mamma é cosí grassa che si sveglia da entrambi i lati del letto.",
    "Ohi stronzo ti sei visto in faccia?",
    "Tu non sei un clown, sei l'intero circo",
    "Non ti meriti neanche un insulto",
    "Sei talmente brutto che non si capisce quale sia la faccia ed il culo",
    "Se fossimo rimasti solo noi due nel mondo preferirei vivere nella fiaba del principe ranocchio. Almeno saresti baciabile",
    "Tua madre è così grassa che non ci sta in una slide",
    "Tua madre è così grassa che provo a fargli una foto mi si riempie la memoria",
    "Quando non riesco a cagare, il primo pensiero che mi viene in mente sei tu"]

listOfInsultsToSomeone = [
    "Dedicato a te, {Insultato} \nNAGG CHI TE STRAMIL MUORT!",
    "{Insultato} sei cattivo",
    "{Insultato} non sei un clown, sei l'intero circo",
    "Ohi, {Insultato} vattene che hai già fatto schifo abbastanza per oggi"
]

def insulta(update: Update):
    message = update.message.text;
    print(message);
    if len(message.split())>1:
        insultato = message.split()[1]
        update.message.reply_text( insultToSomeone(insultato) )
    else:
        update.message.reply_text( insultToSelf() )

def insultToSomeone(insultato: str):
    return random.choice(listOfInsultsToSomeone).format(Insultato = insultato)

def insultToSelf():
    return random.choice(listOfInsultsToSelf)
