# # #6,1

# import requests
# nummer = str(input('Ange ett positivt heltal')) #Frågar efter ett heltal
# url = 'http://77.238.56.27/examples/numinfo/?integer='+ str(nummer) #gör en variabel till urlen + nummret mna skriver in
# r = requests.get(url) #hämtar urlen
# primtal = r.json() #gör variabeln r till json och gör det till en variabel
# if nummer %2==0: #kollar om talet är ett primtal
#     print(nummer + 'är inte ett primtal.')




#  #6,2
# import requests
# städer = [ "stockholm", "uppsala"] #de ända städerna som funkar, troligtvis pga att åäö finns i de andra

# stad = input('Skriv in en av följande städer:Stockholm, Göteborg, Malmö, Uppsala, Västerås: ')

# if stad.lower() in städer: #Om man skriver in staden hämtar den information om vädret  
#     url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/'+ stad
#     r = requests.get(url)
#     platser = r.json()
#     forecasts = platser["forecasts"]
#     for i in forecasts: #skriver ut alla all information som finns om vädret i staden
#         print(i["date"] + " is it " + i["forecast"])
# else:
#     print("Fel stad") #felmeddelande




# # # 6,3

# import requests

# url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

# r = requests.get(url)
# APIresponse = r.json()
# artists = APIresponse['artists'] #den går in i apin och sedan in i artister

# print('----Artister----')

# for i in artists: #skriver ut alla artister
#     print(i['name'])

# namn = str(input('pick an artist: ')) 



# for i in artists:
#     if namn.title() in i ['name']: #om namnet finns i namn från apin sågår den in i id och gör det till en ny variabel
#         url2 = url + i['id']
#         r = requests.get(url2)
#         APIresponse = r.json() #gör om APIresponse-variabeln sen tidigare till url2 i json
#         fakta = APIresponse['artist']
#         print('Genrer:')
#         for genres in fakta['genres']:#skriver ut genrerna för den artisten vi har valt och gör samma sak med medlemmar och år som aktiv längre ner
#             print(genres)
#         print('-----------')
#         print('Medlemmar:')
#         for members in fakta['members']:
#             print(members)
#         print('-----------')
#         print('År som aktiv:')
#         for years_active in fakta['years_active']:
#             print(years_active)

