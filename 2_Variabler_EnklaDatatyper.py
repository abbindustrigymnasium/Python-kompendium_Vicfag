#2,1
# citat='datatyper har inbyggda metoder'
# Nyttcitat= citat.title()
# print(Nyttcitat)          
# #Gör så att första bokstaven i varje ord blir stor

#2,2
# print('Mata in ett flyttal')
# Tal1= float(input())
# svar= 'Det närmsta heltalet är' + " " + str(round(Tal1)) #Avrundar flyttalet till närsta heltalet
# print(svar)  


#2,3
# print('Hej!')
# Förnamn = input('Vad heter du?') #frågar anvädaren efter förnamn och sätter det i en variabel
# print('Haha, jag också')
# Efternamn = input('Vad är ditt efternamn?') #frågar anvädaren efter efternamn och sätter det i en variabel
# print('Hej' + " " + Förnamn.title() + " " + Efternamn.title()) #skriver ut hela namnet med första bokstaven stor för att det är namn


#2,4

# ålder = input('Hur gammal är du? ') #frågar användaren hur gammal den är och sätter svaret i en variabel
# ålder1 = int(ålder) # sätter unputen till int
# årtillmynidg = 18 - ålder1
# print('Du är myndig inom' + " " + str(årtillmynidg) + " " + "år!") #skriver ut svaret i str


#2,5
# print('Hur många vill ha 2 vanliga korvar?') # Frågar användaren hur många korvar av varje sort och sparar svaren i variabler
# tvåvanligakorvar=input()
# print('Hur många vill ha 3 vanliga korvar?')
# trevanligakorvar=input()
# print('Hur många vill ha 2 veganska korvar?')
# tvåveganskakorvar=input()
# print('Hur många vill ha 3 veganska korvar?')
# treveganskakorvar=input()

# a= int(tvåvanligakorvar)*2 # sätter svaren till int och tar antalet personer gånger korvar det innebär
# b= int(trevanligakorvar)*3
# c= int(tvåveganskakorvar)*2
# d= int(treveganskakorvar)*3

# a2= a/2 #räknar ut hur många drickor som behövs
# b2= b/2
# c2= c/2
# d2= d/2

# vanlförp = (a+b)/8 #räknar ur hur många förpackningar som behövs
# vegförp = (c+d)/4

# dricka = (a2+b2+c2+d2) # räknar ut hur många drickor som behövs

# print('Antal förpackningar vanliga korvar som behövs är' + " " + str(vanlförp)) #skriver ut svaren i string
# print('Antal förpackningar veganska korvar som behövs är' + " " + str(vegförp))
# print('Antal drickor som behövs är' + " " + str(dricka) + " " + 'st')
