''' Learn the direct implementation of object oriented programming in Python.

    Object:  unique data associated with shared data and functions
    
        __dict__     A dictionary with information UNIQUE to each instance
        __class__    A reference to the class that has the SHARED information

    Class:   named group of shared functions and data plus references to other classes

        __name__     A str with the name given at birth
        __bases__    A tuple of other class so we can REUSE their code
        __dict__     A dictionary of information SHARED by all instances

    Benefits:
        * better organization of code
        * ability to introspect with dir(d)
        * prevention of calling wrong function with wrong data
        * learnability by using the same method name in multiple classses
        * polymorphism eliminates big if-elif chains
        
    Learn the common dunder methods in Python:

        Keywords
        --------
        with s:                ==> s.__enter__()
                                   s.__exit__()
        for x in s             ==> s.__iter__()
        print s                ==> s.__str__()

        Operators
        ---------
        s[i]                   ==> s.__getitem__(i)
        s(a, b)                ==> s.__call__(a, b)
        s + t                  ==> s.__add__(t)
        s * t                  ==> s.__mul__(t)
        s ** t                 ==> s.__pow__(t)

        Functions
        ---------
        len(s)                 ==> s.__len__()
        abs(s)                 ==> s.__abs__()
        

    Learn how to take advantage of polymorhism:
        * using the same method name in multiple classes
        * to improve learnability and
        * to get automatic dispatch instead of if-elifi haings

'''

class Mammal:
    'Order of mammals'

    repro = 'gives birth to live young'

    def __init__(self, name):
        self.name = name

class Dog(Mammal):
    'A simple canine class'

    kind = 'canine'
        
    def talk(dog):
        print 'Woof!  %s is barking' % dog.name

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        return 111 * index

class Cat(Mammal):
    'A simple feline class'

    kind = 'feline'

    def talk(cat):
        print 'Meow!  %s is purring' % cat.name

###########################################

c = Cat('Socks')
d = Dog('Fido')
e = Dog('Buddy')
f = Dog('Checkers')

pets = [c, d, e, f]
for pet in pets:
    pet.talk()

