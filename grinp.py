"""
Get Right INPut
general purpose TYPE-SAFE input validation tool for python CLI programs
grimp() returns input value based on option flags or menu

grinp(prompt, [options], *[high and/or low]) -> str [or float, or int]
    if options is given a string flags will be processed, if options is given an iterable
    those specific values inside the iterable will be converted to strings for input comparison
    # menu choices of numerical strings will return a string because the 'f' and 'i' flags are
      not present to be processed

whitelist flags:  (a)lpha  (n)umber  (s)pace  (o)ther
    these flag permitted characters, all are selected by default 

    ex: grinp('prompt for user', 'ano')
    # this will permit alphanumeric input and special characters but not
      permit spaces

requirement flags:  (f)loat  (i)nt
    these flags will ensure conversion to the required type
    none are selected by default

    both 'f' & 'i' take precedance over all other whitelist flags, but
    if both 'f' & 'i' are included, 'f' takes precedence

    ex: grinp('ask for float', 'f')
    # only accepts input that can be converted to float & returns it as float

    ex: grinp('ask for integer', 'i')
    # only accepts input that can be converted to an int & returns it as an int

range value flags:  h(i)gh  (l)ow 
    enforce numerical input to fall within specified range,
    default values are high = float(inf) & low = float(-inf)
    # only used if 'f' or 'i' flags are enabled
    # if both 'h' & 'l' are set, 'l' will take precedence if only one value is given
    
menu can be a tuple, or a list consisting of any basic types (float, int, str)

    ex: grinp('say something', [1, 2.2, 3, 'a', 'b'])
    # a list of specific choices overrides all other flags

"""

def grinp(prompt, options = 'anso', *hilo):
    userInput = input(f'{prompt} ')
    test = isValid(userInput, options, *hilo)

    while test['err'] != None:
        print(test['err'])
        userInput = input(f'{prompt} ')
        test = isValid(userInput, options, *hilo)

    return test['data']



def isValid(testInput, options = 'anso', *hilo):
    test = {'err' : None, 'data' : testInput}

    hilo = setHiLo(hilo, options)
        
    if 'f' in options: return floatIt(test, hilo)
    if 'i' in options: return IntIt(test, hilo)

    if type(options) == str: filterByFlags(test, options)
    else: checkMenu(test, options)  

    return test



def hiLoTest(value, hilo):
    return min(hilo) < value < max(hilo)



def setHiLo(hilo, options):
    if len(hilo) == 2:
        return [hilo[0], hilo[1]]

    if len(hilo) == 1:
        if 'l' in options:
            return [hilo[0], float('inf')]
        elif 'h' in options:
            return [hilo[0], float('-inf')]

    return [float('-inf'), float('inf')]



def floatIt(feedback, hilo):
    try:
        feedback['data'] = float(feedback['data'])
        if not hiLoTest(feedback['data'], hilo):
            feedback['err'] = f"\'{feedback['data']}\' is outside the range {min(hilo)} thru {max(hilo)}"
    except: feedback['err'] = f"\'{feedback['data']}\' cannot be converted to float"

    return feedback



def IntIt(feedback, hilo):
    try:
        feedback['data'] = int(float(feedback['data']))
        if not hiLoTest(feedback['data'], hilo):
            feedback['err'] = f"\'{feedback['data']}\' is outside the range {min(hilo)} thru {max(hilo)}"
    except: feedback['err'] = f"\'{feedback['data']}\' cannot be converted to integer"

    return feedback



def filterByFlags(test, flags):
    for char in test['data']:
        if char.isalpha() and 'a' not in flags:
            test['err'] = 'alpha characters not permitted'
        if char.isdigit() and 'n' not in flags:
            test['err'] = 'numeric characters not permitted'
        if char.isspace() and 's' not in flags:
            test['err'] = 'spaces are not permitted'
        if not char.isalnum() and not char.isspace() and 'o' not in flags:
            test['err'] = 'special characters not permitted'


    
def checkMenu(feedback, menu):
    menu = list(map(lambda x: str(x), menu))
    
    if feedback['data'] not in menu:
        feedback['err'] = f"\'{feedback['data']}\' does not match the menu <{menu}>"       

    return feedback
    


