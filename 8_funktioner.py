#8.1

# def km_to_miles(dist): #skapar en funktion som heter km_to_miles
#     return str(dist*0.6213712) + 'miles' #som gör om km till miles

# def miles_to_km(dist): #skapar en funktion som heter miles_to_km
#     return str(dist*1.609344) + 'km' #som gör om miles till km

# distance = input('Ange din distans (OBS! Skriv med enheten:') 

# if 'km' in distance.lower(): #om stringen km finns med i distance-variabeln så gör den variabeln length så använder den km_to_miles funktionen
#     length = km_to_miles(float(distance.strip('km')))

# elif 'miles' in distance.lower(): #om stringen km finns med i distance-variabeln så gör den variabeln length så använder den miles_to_km funktionen
#     length = miles_to_km(float(distance.strip('miles')))

# print('Din distans koverterad:' + length) #skriver ut length

# #8.2
# import web #hämtar modulen web
# import requests #hämtar requests
# städer = [ "stockholm", "uppsala"] #var bara de städer som fungerade, troligtvis på grund av åäö

# stad = input('Skriv in en av följande städer:Stockholm eller Uppsala: ')

# if stad.lower() in städer: #om staden finns i staden städer
#     platser = web.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/'+ stad.lower())  #går un i urlen genom modulen och lägger till staden man har valt
#     forecasts = platser["forecasts"] #går sedan in i forecasts
#     for i in forecasts:
#         print(i["date"] + " is it " + i["forecast"]) # skriver ut alla datum och vilket väder det förväntas bli
# else:
#     print("Fel stad") #skriver man något annat än det som finns i variabeln städer säger den till om det

#8.3

# import ui #hämtar modulen ui

# ui.line() #använder funktioner från ui
# ui.header('Exempel')
# ui.line(True)
# ui.echo('Detta äe exempel på')
# ui.echo('ett gränssnitt kan se ut')
# ui.line()
# ui.header('..vad vill du göra')
# ui.line()
# ui.echo('A. Visa inköpslista')
# ui.echo('B. Lägg till vara')
# ui.echo('C, Ta bort vara')
# ui.echo('X. stäng programmet')
# ui.line()
# ui.promt('Val')

#8.4
import ui #importerar nödvändiga moudler och funktioner
import requests
import web

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/' # urlen

web.get(url) # använder modulen 
shutdown = False # sätter shutdown variabeln till false för att vi inte vill att whileloopen ska stängas ner


artists = web.get('https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/')['artists']  #går in i urlen och in i artister


ui.line() #skapar interface med ui.py
ui.header('Artist database')
ui.line()
ui.echo('Welcome to a world of')
ui.echo('Music')
ui.line()
ui.echo('L, List artists')
ui.echo('V, View artist profile')
ui.echo('E, Exit application')
ui.line()
choice = ui.promt('| Selection> ')
ui.line()
while shutdown == False: # om shutdown variabeln är falsk vilket vi satte den till kör den whileloopen
    if choice.lower() == 'l': #om man väljer l
        for i in artists: #skriver ut alla artisters namn
            ui.echo(i['name'])
        ui.line()
        ui.echo('L, List artists') #gör så man kan välja igen
        ui.echo('V, View artist profile')
        ui.echo('E, Exit application')  
        ui.line()
        choice = ui.promt('| Selection> ')
    if choice.lower() == 'v': # om man väljer v får man sedan välja artist för att få fram mer info
        choice1 = ui.promt('| Artist name> ')
        ui.line(True)
        ui.echo(choice1) #skriver ut vilken artist man valde
        for i in artists:
            if choice1.title() == i['name'].title():
                url2 = url + i['id'] #url2 använder variabeln url fast den går även in i id i urlen
                APIresponse = web.get(url2) #APIresponse är url2 fast i json
                fakta = APIresponse['artist']['members'] #gör en variabel både för medlemmarna och genrerna för att vi ska kunna använda det i forlooparna
                fakta1 = APIresponse['artist']['genres']
                for members in fakta: #skriver ut medlemmarna
                    ui.echo(members)
                for genres in fakta1:#skriver ut genrerna
                    ui.echo(genres)
                ui.echo(APIresponse['artist']['years_active'][0]) #behöver inte en forloop för aktiva år för att det alltid är ett värde
                ui.line()
                ui.echo('L, List artists')
                ui.echo('V, View artist profile')
                ui.echo('E, Exit application')
                ui.line()
                choice = ui.promt('| Selection> ')
                ui.line()



    if choice.lower() == 'e': #går ut ur loppen alltså avslutar programmet
        break



