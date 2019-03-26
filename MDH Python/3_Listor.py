male=['Erik','Lars','Karl','Anders','Johan']
female=['Maria','Anna','Margareta','Elisabeth','Eva']

#3.1

# del male[2]
# del male[2]
# del male[2]

# del female[0]
# del female[0]
# del female[1]

#3.2

# del male[1]
# del male[1]

# del female[0]

#3.3

# male.append('Victor')

#3.4

# male[0]='Anders'
# male[1]='Erik'
# male[2]='Johan'
# male[3]='Karl'

# female[0]='Anna'
# female[1]='Elisabeth'
# female[2]='Eva'
# female[3]='Margareta'

#3.5

name=input('Vilket namn ska plockas bort från listorna?')

if name in male:
    male.remove(name)

if name in female:
    female.remove(name)

print('Män:', male)
print('Kvinna:', female)