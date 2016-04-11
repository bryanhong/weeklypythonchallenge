'Goal:  Learn common argument passing tools in Python'

def mypow(base, exp):
    'Raises a base to the exp power'
    return base ** exp

print mypow(2, 5)                        # positional arguments where the order matters
print mypow(exp=5, base=2)               # keywords arguments where the name matters, not the order
print mypow(2, exp=5)                    # hybird arguments where positional arguments go before keywords

arguments = 2, 5
print mypow(arguments[0], arguments[1])  # unpack a suitcase of arguments to pass in to the function
print mypow(*arguments)                  # 1 star unpacks a sequence into positional arguments

arguments = {'exp': 5, 'base': 2}
print mypow(exp=arguments['exp'], base=arguments['base']) # unpack a suitcase of arguments to pass in to the function
print mypow(**arguments)                 # 2 stars unpacks a mapping into keyword arguments

def f(a, b, c=0, d=0):                   # Optional arguments with defaults go AFTER the required arguments
    print a + b + c + d

def f(a, b, *args):                      # 1-star in a definition packs positional arguments into a tuple
    print a, b, args

def f(a, b, *args, **kwargs):            # 2-star packs keyword arguments into a dictionary
    print a, b, args, kwargs

def logging_pow(*args, **kwargs):
    'Add a wrapper around mypow() to display inputs and outputs'
    print 'mypow() called with %r and %r' % (args, kwargs)
    answer = mypow(*args, **kwargs)
    print 'the answer is %r' % answer
    return answer

y = logging_pow(2, 5)
y = logging_pow(exp=5, base=2)
y = logging_pow(2, exp=5)
