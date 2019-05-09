# #7.1

# nummer = int(input('Ange en multiplikationstabell:')) # man väljer en multiplikationstabell

# mult = 1 # vad input ska multipliceras med
# times = 4 # gör så att vi kan stoppa loopen

# while True:    # skapar en while-loop  
#     print(nummer*mult) #skriver ut nummretmna skriver in i nummer gånger mult
#     mult += 1 # öker med 1 varje gång loopen körs
#     if mult == times: #om mult = times så frågar den om man vill fortsätta loopen
#         svar = str(input('Fortsätt?'))
#         if svar.lower() == 'ja' :
#             times += 3 #ökar times med 3 för att loopen ska köras 3 gånger till om man svarar ja 
#             continue
#         elif svar.lower() == 'nej' :# annars bryter den loopen
#             break
#         else:
#             break

    








#7.2
# import random #hämtar random

# x = random.randint(1,100)#väljer intervallet

# print('Higher Lower')
# print('A number between 0 and 99 will be randomized. Can you guess it?')

# guesses = 0 #gör så att guesses startar på 0

# while True: #skapar while-loop
#     nummer = int(input('What do you guess?'))
#     if nummer < x: #om det man gissar är lägre än det randomiserade talet skriver den det och lägger till 1 till guesses
#         print('too low')
#         guesses += 1
#         continue
#     elif nummer > x: #samma sak som ovan fast om man gissar för högt
#         print('too high')
#         guesses += 1
#         continue
#     elif nummer == x: #om det man skriver ut stämmer överens med det randomiserade nummret skriver det ut antal försök det tog att hitta rätt
#         print('Guesses:', guesses)       
#     break
    