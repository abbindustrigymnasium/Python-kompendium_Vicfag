#8.1

# def km_to_miles(dist):
#     return str(dist*0.6213712) + 'miles'

# def miles_to_km(dist):
#     return str(dist*1.609344) + 'km'

# distance = input('Ange din distans:')

# if 'km' in distance.lower():
#     length = km_to_miles(float(distance.strip('km')))

# elif 'miles' in distance.lower():
#     length = miles_to_km(float(distance.strip('miles')))

# print('Din distans koverterad:' + length)

# #8.2
# import web
# import requests
# städer = [ "stockholm", "uppsala"]

# stad = input('Skriv in en av följande städer:Stockholm, Göteborg, Malmö, Uppsala, Västerås: ')

# if stad.lower() in städer:
#     platser = web.get('https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/'+ stad.lower())
#     forecasts = platser["forecasts"]
#     for i in forecasts:
#         print(i["date"] + " is it " + i["forecast"])
# else:
#     print("Fel stad")

#8.3

# import ui

# ui.line()
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
import ui
import requests
import web

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

web.get(url)
shutdown = False
# r = requests.get(url)
# APIresponse = r.json()

artists = web.get('https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/')['artists']
# artists = APIresponse['artists']

ui.line()
ui.header('Artist database')
ui.line()
    # print('----Artister----')
ui.echo('Welcome to a world of')
ui.echo('Music')
ui.line()
ui.echo('L, List artists')
ui.echo('V, View artist profile')
ui.echo('E, Exit application')
ui.line()
choice = ui.promt('| Selection> ')
ui.line()
while shutdown == False:
    if choice.lower() == 'l':
        for i in artists:
            ui.echo(i['name'])
        ui.line()
        ui.echo('L, List artists')
        ui.echo('V, View artist profile')
        ui.echo('E, Exit application')  
        ui.line()
        choice = ui.promt('| Selection> ')
    if choice.lower() == 'v':
        choice1 = ui.promt('| Artist name> ')
        ui.line(True)
        ui.echo(choice1)
        for i in artists:
            if choice1.title() == i['name'].title():
                url2 = url + i['id']
                APIresponse = web.get(url2)
                fakta = APIresponse['artist']['members']
                fakta1 = APIresponse['artist']['genres']
                for members in fakta:
                    ui.echo(members)
                for genres in fakta1:
                    ui.echo(genres)
                ui.echo(APIresponse['artist']['years_active'][0])
                ui.line()
                ui.echo('L, List artists')
                ui.echo('V, View artist profile')
                ui.echo('E, Exit application')
                ui.line()
                choice = ui.promt('| Selection> ')
                ui.line()



    if choice.lower() == 'e':
        break





#namn = str(input('pick an artist: ')) 



# for i in artists:
#     if namn.title() in i ['name']:
#         url2 = url + i['id']
#         r = requests.get(url2)
#         APIresponse = r.json()
#         #print(url2)
#         #print(i['id'])
#         fakta = APIresponse['artist']
#         print('Genrer:')
#         for genres in fakta['genres']:
#             print(genres)
#         print('-----------')
#         print('Medlemmar:')
#         for members in fakta['members']:
#             print(members)
#         print('-----------')
#         print('År som aktiv:')
#         for years_active in fakta['years_active']:
#             print(years_active)
