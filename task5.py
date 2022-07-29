x = int(input('введіть число:'))

def is_prime(x):
    if 0 > x > 1000:
        print('EROR')
    elif x % 2 == 0 or x % 3 == 0:
        print('FALSE')
    else: print('TRUE')

is_prime(x)
