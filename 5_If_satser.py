# print('Vilket kön har du?') 
# kön=input()
# print('Vilken hårfärg har du?')
# hårfärg=input()
# print('Vilken ögonfärg har du?')
# ögonfärg=input()

# daniel_radcliff=['man','brun','brun','Daniel Radcliff']
# rupert_grint=['man','röd','blå','Rupert Grint']
# emma_watson=['kvinna','brun','brun','Emma Watson']
# selena_gomez=['kvinna','brun','brun','Selena Gomez']

# kändis=[daniel_radcliff,rupert_grint,emma_watson,selena_gomez]

# for personer in kändis: #kollar om din information är lika som någon av personerna
#     if kön == personer[0]:
#         if hårfärg == personer[1]:
#             if ögonfärg == personer[2]:
#                 print('Du är lik:', personer[3])
            
#  #5.2

# namn = input('Ange ditt namn:')
# ålder = int(input('Ange ditt ålder:'))

# behov=[14,13,12,11.5,11,11,10.5,10,10,10,9.5,9,9,9,8.5,8]

# if ålder < 17: # om åldern är under 17 går den efter listan,annars 8h
#     h=behov[ålder-1] #tar åldern man skriver in -1 för att få rätt plats i listan
# else:
#     h=8

# print('Hej',namn,', du borde sova', h ,'timmar')

# 5.3

# land=input('Skriv ett land:')
# land=land.capitalize() # för att få första bokstäven stor

# norden=['Danmark','Finland','Island','Norge','Sverige']
# stor=['England','Nordirland','Skottland','Wales']

# if land in norden: #om landet man skriver in ligger i listan norden säger den det
#     print('Ditt land ligger i Norden!')
# elif land in stor: #om landet man skriver in ligger i listan stor säger den det
#     print('Ditt land ligger i Storbrittanien!')
# else:
#     print('Ditt land ligger varken i Norden eller Storbrittanien') #om det man skriver in inte finns i någon av listorna säger den att landet ligger i varken eller


