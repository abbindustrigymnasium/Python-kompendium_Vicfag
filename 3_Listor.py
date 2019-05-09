male=['Erik','Lars','Karl','Anders','Johan']
female=['Maria','Anna','Margareta','Elisabeth','Eva']

#3.1

# del male[2] #tar bort namnen i listorna som vi inte vill skriva ut
# del male[2]
# del male[2]

# del female[0]
# del female[0]
# del female[1]
# print(male) #skriver ut listorna
# print(female)

#3.2

# del male[1] #-||-
# del male[1]

# del female[0]

#3.3

# male.append('Victor') #lägger till mitt namn

#3.4

# male[0]='Anders' #redigerar ordningen
# male[1]='Erik'
# male[2]='Johan'
# male[3]='Karl'
# male[4]='Lars'

# female[0]='Anna'
# female[1]='Elisabeth'
# female[2]='Eva'
# female[3]='Margareta'
# female[4]='Maria'

# print(male)
# print(female)
#3.5

# name=input('Vilket namn ska plockas bort från listorna?') #Frågar efter ett namn

# if name in male: #kollar om namnet finns i male och om det gör det tar den bort det
#     male.remove(name)

# if name in female: #kollar om namnet finns i female och om tar det bort det
#     female.remove(name)

# print('Män:', male)
# print('Kvinnor:', female)