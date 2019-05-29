import random
import requests
import web
import ui

def escape(str):
    str = str.replace('&rsquo;', "\'") #byter ut &rsquo till en ' 
    return str
    

url = 'https://opentdb.com/api.php?amount=5&category=27&difficulty=easy&type=boolean'

fragor = web.get(url)['results'] #gör om urlen till json och går in i results i dictionaryt

nummer = list(range(0,5))
random.shuffle(nummer) #blandar nummer från 0 till 5 i slumpmässig ordning

i = 0 # väljer första siffran i listan
rightanswer = 0 #startar rätträknaren på noll



ui.line()
ui.header('Välkommen till Djurquizet')
ui.header('Du kommer att få fem frågor som handlar om djur')
ui.line(True)



while i < 5: #körs 5 gånger och slutar sen
    rättsvar = fragor[nummer[i]]["correct_answer"] #skapar en variabel som har rätt svar till rätt fråga
    ui.echo(escape(fragor[nummer[i]]["question"]))  #skriver ut första frågan
    svar1 = ui.promt('Answer (true or false) : ') # skapar en variabel med deltagarens svar
    if svar1.title() == rättsvar: #om svaret med första bokstaven stor stämmer:
        print(rättsvar)
        print('Du har svarat rätt! ')
        ui.line()
        rightanswer += 1 #om man har rätt på frågan lägger den till 1 till rätträknaren
        i += 1#gör så att den tar nästa fråga
        continue
    else:
        print(rättsvar)
        print('Du har svarat fel:( ')
        ui.line()
        i += 1
        continue

print('Antal rätt:', rightanswer)




