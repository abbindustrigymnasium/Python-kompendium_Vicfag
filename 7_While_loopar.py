#7.1

# nummer = int(input('Ange en multiplikationstabell:'))

# mult = 1
# raknare = 0 
# times = 4

# while True:      
#     print(nummer*mult)
#     mult += 1
#     if mult == times:
#         svar = str(input('Fortsätt?'))
#         if svar.lower() == 'ja' :
#             times += 3
#             continue
#         elif svar.lower() == 'nej' :
#             break
#         else:
#             break

    








#7.2
import random

x = random.randint(1,100)

print('Higher Lower')
print('A number between 0 and 99 will be randomized. Can you guess it?')

guesses = 0

while True:
    nummer = int(input('What do you guess?'))
    if nummer < x:
        print('too low')
        guesses += 1
        continue
    elif nummer > x:
        print('too high')
        guesses += 1
        continue
    elif nummer == x:
        print('Antal försök:')
        print(guesses)
    break
    