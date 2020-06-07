#pw_lab02_makeChange.py;
#depencancies: none;
#last edit: 2020-05-18, by pWurster;
#takes integer value from user (in cents) and converts to quantities of  
#enumerated 'coin' representations

#init vars to 0
coins = {'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
total = 0

try:
    #cast input to int
    total = int(input('Enter a number of cents less than a dollar: '))

    #process data
    coins['quarters'] = total // 25
    coins['dimes'] = total % 25 // 10
    coins['nickels'] = total % 25 % 10 // 5
    coins['pennies'] = total % 25 % 10 % 5

    #build output string
    output = f'{total} cents converts to:\n'
    for key in coins.keys():
        output += f'\t{coins[key]} {key}\n'

    #display results
    print(output)

except:
    #quit if input cannot be cast to int
    input('Must be an integer, press [enter] to exit program...')


