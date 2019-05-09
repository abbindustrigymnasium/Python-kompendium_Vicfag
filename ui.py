def line(tof = False): #skriver * eller - beroende om man skriver ut True eller False i ui.py()
    if tof == True:
        print('******************************')
    else:
        print('------------------------------')

def header(wrd):
    centerwrd = wrd.center(25) #har ordet man skriver i ui.header() i mitten av 25 spaces och | på sidorna
    print('|',centerwrd,'|')

    
def echo(wrd):
    print('|',wrd,) #skriver | sedan ordet eller orden man skriver i ui.echo()

def promt(fraga):
    return str(input(fraga)) #samma sak som funktionen input