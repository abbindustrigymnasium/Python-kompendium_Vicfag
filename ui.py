def line(tof = False):
    if tof == True:
        print('******************************')
    else:
        print('------------------------------')

def header(wrd):
    centerwrd = wrd.center(25)
    print('|',centerwrd,'|')


def echo(wrd):
    print('|',wrd,)

def promt(fraga):
    return str(input(fraga))