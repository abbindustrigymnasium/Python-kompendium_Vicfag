#2,1
# citat='datatyper har inbyggda metoder'
# Nyttcitat= citat.title()
# print(Nyttcitat)          
# Gör så att första bokstaven i varje ord blir stor

#2,2
# print('Mata in ett flyttal')
# Tal1= float(input())
# Tal2= int(Tal1)
# svar= 'Det närmsta heltalet är' + " " + str(Tal2)
# print(svar)  
#omvandlar ett decimaltal till ett heltal

#2,3
# print('Hej!')
# print('Vad heter du?')
# Förnamn = input()
# print('Haha, jag också')
# print('Vad är diitt efternamn?')
# Efternamn = input()
# print('Hej' + " " + Förnamn + " " + Efternamn)
#frågar efter ditt namn och skriver ut det

#2,4
# print('Hur gammal är du?')
# ålder = input()
# ålder1 = float(ålder)
# årtillmynidg = 18 - ålder1
# print('Du är myndig inom' + " " + str(årtillmynidg) + " " + "år!") 
#frågar om din ålder och svarar inom hur många år du är myndig

#2,5
print('Hur många vill ha 2 vanliga korvar?')
tvåvanligakorvar=input()
print('Hur många vill ha 3 vanliga korvar?')
trevanligakorvar=input()
print('Hur många vill ha 2 veganska korvar?')
tvåveganskakorvar=input()
print('Hur många vill ha 3 veganska korvar?')
treveganskakorvar=input()

a= int(tvåvanligakorvar)*2
b= int(trevanligakorvar)*3
c= int(tvåveganskakorvar)*2
d= int(treveganskakorvar)*3

a2= a/2
b2= b/2
c2= c/2
d2= d/2

vanlförp = (a+b)/8
vegförp = (c+d)/4

dricka = (a2+b2+c2+d2)

print('Antal förpackningar vanliga korvar som behövs är' + " " + str(vanlförp))
print('Antal förpackningar veganska korvar som behövs är' + " " + str(vegförp))
print('Antal drickor som behövs är' + " " + str(dricka) + " " + 'st')
