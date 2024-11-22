try:
    value1=float(input('Enter a value:'))
    value2=float(input('Enter a value:'))
except ValueError:
    print('Sorry,this is not a number')
except:
    print('This is not a good input...')


def add(num1,num2):
    return int(num1+num2)
print(add(4,5))

tup=(3,6,7,9)

try:
    tup.append(2)
except AttributeError:
    print('Tuples are immutable')