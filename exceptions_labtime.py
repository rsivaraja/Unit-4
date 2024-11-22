try:
    value=int(input('Enter a value:'))
except ValueError:
    print('Bad input...')
except ZeroDivisionError:
    print('Very bad input...')
except:
    print('Booo!')