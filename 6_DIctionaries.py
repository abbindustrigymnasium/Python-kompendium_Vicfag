# #6,1

# import requests
# url = 'http://77.238.56.27/examples/numinfo/?integer='+ str(nummer)
# r = requests.get(url)
# primtal = r.json()
# nummer = str(input('Ange ett positivt heltal'))
# if nummer %2==0:
#     print(nummer + 'är inte ett primtal.')




# # #6,2
# import requests
# städer = [ "stockholm", "uppsala"]

# stad = input('Skriv in en av följande städer:Stockholm, Göteborg, Malmö, Uppsala, Västerås: ')

# if stad.lower() in städer:
#     url = 'https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/'+ stad
#     r = requests.get(url)
#     platser = r.json()
#     forecasts = platser["forecasts"]
#     for i in forecasts:
#         print(i["date"] + " is it " + i["forecast"])
# else:
#     print("Fel stad")




# # 6,3

import requests

url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

r = requests.get(url)
APIresponse = r.json()
artists = APIresponse['artists']

print('----Artister----')

for i in artists:
    print(i['name'])

namn = str(input('pick an artist: ')) 



for i in artists:
    if namn.title() in i ['name']:
        url2 = url + i['id']
        r = requests.get(url2)
        APIresponse = r.json()
        #print(url2)
        #print(i['id'])
        fakta = APIresponse['artist']
        print('Genrer:')
        for genres in fakta['genres']:
            print(genres)
        print('-----------')
        print('Medlemmar:')
        for members in fakta['members']:
            print(members)
        print('-----------')
        print('År som aktiv:')
        for years_active in fakta['years_active']:
            print(years_active)

