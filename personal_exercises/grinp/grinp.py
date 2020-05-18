#grinp.py;
#depencancies: none;
#last edit: 2020-05-18, by pWurster;
#
#whitelist flags:  (a)lpha  (n)umber  (s)pace  (o)ther
#requirement flags:  (f)loat  (i)nt
#range value flags:  h(i)gh  (l)ow

def grinp(prompt, options = 'anso', *hilo):
    """
    Get Right INPut
    general purpose TYPE-SAFE input validation tool for python CLI programs
    grimp() returns input value based on option flags or menu

    grinp(prompt, [options], *[high and/or low]) -> str [or float, or int]
    if options is given a string, flags will be processed; if options is given an
    iterable (instead of flags) those specific values inside the iterable will be
    converted to strings for input comparison
    """
    userInput = input(f'{prompt} ')
    test = isValid(userInput, options, *hilo)

    while test['err'] != None:
        print(test['err'])
        userInput = input(f'{prompt} ')
        test = isValid(userInput, options, *hilo)

    return test['data']



def isValid(testInput, options = 'anso', *hilo):
    test = {'err' : None, 'data' : testInput}

    if type(options) != str: return checkMenu(test, options)
    else:
	    if 'f' in options or 'i' in options:
	    	hilo = setHiLo(hilo, options)
	    	return floatIntTest(test, options, hilo)

	    return filterByFlags(test, options)



def hiLoTest(value, hilo):
    return min(hilo) <= value <= max(hilo)



def setHiLo(hilo, flags):
    if len(hilo) == 2: return [hilo[0], hilo[1]]

    if len(hilo) == 1:
        if 'l' in flags: return [hilo[0], float('inf')]
        elif 'h' in flags: return [hilo[0], float('-inf')]

    return [float('-inf'), float('inf')]



def floatIntTest(test, flags, hilo):
	try:
		test['data'] = float(test['data']) if 'f' in flags else int(float(test['data']))
		if not hiLoTest(test['data'], hilo):
			test['err'] = f"\'{test['data']}\' is outside the range {min(hilo)} thru {max(hilo)}"
	except: test['err'] = f"\'{test['data']}\' cannot be converted to {'float' if 'f' in flags else 'integer'}"

	return test



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

    return test


    
def checkMenu(test, menu):
    menu = list(map(lambda x: str(x), menu))
    
    if test['data'] not in menu:
        test['err'] = f"\'{test['data']}\' does not match the menu <{menu}>"       

    return test

