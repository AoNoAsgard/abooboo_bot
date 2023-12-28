import random
from tokenize import String
from telegram import Update
import telegram as telegram


listOfInsultsToSelf =[
    "Sei così stupido che in una gara di stupidità riusciresti comunque ad arrivare secondo",
    "Se cadessi in un fiume sarebbe una sfortuna. Ma se qualcuno ti ci tirasse fuori sarebbe una calamità", 
    "Ma sei scemo?",
    "Tua madre se ingoiava faceva una cosa buona quella notte",
    "Hai mai pensato di portarti dietro una pianta, così cerchi di compensare all'ossigeno che sprechi",
    "Tua mamma è cosí grassa che si sveglia da entrambi i lati del letto",
    "Ohi stronzo ti sei visto in faccia?",
    "Tu non sei un clown, sei l'intero circo",
    "Non ti meriti neanche un insulto",
    "Sei talmente brutto che non si capisce quale sia la faccia ed il culo",
    "Se fossimo rimasti solo noi due nel mondo preferirei vivere nella fiaba del principe ranocchio. Almeno saresti baciabile",
    "Tua madre è così grassa che non ci sta in una slide",
    "Tua madre è così grassa che provo a fargli una foto mi si riempie la memoria",
    "Quando non riesco a cagare, il primo pensiero che mi viene in mente sei tu",
    "Mi chiedo se il tuo culo sia geloso della quantità di merda che esce fuori dalla tua bocca"
]

listOfInsultsToSomeone = [
    "Dedicato a te, {Insultato} \nNAGG CHI TE STRAMIL MUORT!",
    "{Insultato} sei cattivo",
    "{Insultato} non sei un clown, sei l'intero circo",
    "Ohi, {Insultato} vattene che hai già fatto schifo abbastanza per oggi",
    "Ehi {Insultato}, se non la smetti di rompere i coglioni, TI FICCO UNA SPRANGA SU PER IL CULO!",
    #Aggiungo gli insulti della lista precedente a questa
    "{Insultato} sei così stupido che in una gara di stupidità riusciresti comunque ad arrivare secondo",
    "{Insultato}, se cadessi in un fiume sarebbe una sfortuna. Ma se qualcuno ti ci tirasse fuori sarebbe una calamità",
    "{Insultato} ma sei scemo?",
    "{Insultato} tua madre se ingoiava faceva una cosa buona quella notte",
    "{insultato}, hai mai pensato di portarti dietro una pianta? Compenseresti l'ossigeno che sprechi",
    "{Insultato}, tua mamma è cosí grassa che si sveglia da entrambi i lati del letto",
    "{Insultato} ti sei mai visto in faccia, stronzo come sei?",
    "{Insultato} non meriti neanche un insulto",
    "{Insultato} sei talmente brutto che non si capisce quale sia la faccia e quale il culo",
    "{Insultato}, se rimanessimo solo noi due nel mondo preferirei vivere nella fiaba del principe ranocchio. Almeno saresti baciabile",
    "{Insultato}, tua madre è così grassa che non ci sta in una slide",
    "{Insultato}, tua madre è così grassa che provo a fargli una foto mi si riempie la memoria",
    "{Insultato} mi chiedo se il tuo culo sia geloso della quantità di merda che esce fuori dalla tua bocca",
    #Aggiungo qualche altro insulto a caso
    "{Insultato} la tua unica qualità è che è impossibile sottostimarti",
    "{Insultato}, sei più stupido di un blocco di legno, che a differenza tua almeno può essere utile",
    "{Insultato} spero tu muoia come sei nato: cagando",
    "{Insultato}, visto il fetore che emani direi che tua madre era un murloc!",
    "{Insultato} saresti capace di rattristire anche Lucio Dalla. E ce ne vuole!",
    "{Insultato} che ci fai ancora qui? Le scimmie come te dovrebbero stare allo zoo",
    "{Insultato}, ti darei fuoco ma il mio senso civico m'impone di non bruciare la spazzatura",
    "{Insultato} ma perché parli ancora? Non ti hanno insegnato che è meglio lasciare che qualcuno pensi che sei un idiota piuttosto che aprire la bocca e dimostrarlo?",
    "{Insultato}, ricordi quando qualcuno ha mai chiesto la tua opinione? Nemmeno io",
    "{Insultato} sei acuto quanto un angolo di 200 gradi",
    "{Insultato}, non dimenticherò mai la prima volta che ci siamo incontrati, ma puoi stare certo che sto provando del meglio per farlo",
    "{Insultato}, per te l'italiano non basta: fick dich dummkop stück scheiße" 
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
