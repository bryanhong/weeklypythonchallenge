# oop.py

from time import sleep

'''
        initalize       __init__
        x == y          __eq__
        repr(x)         __repr__
        len(x)          __len__
        iter(x)         __iter__
        x + y           __add__
        x - y           __sub__
        x * y           __mul__
        x | y           __or__
        x[i]            __getitem__
        x()             __call__
'''

class Machine(object): # new-style object
    manufacturer = 'Cisco'
    def __init__(self, asset_tag):
        self.asset_tag = asset_tag

    def __eq__(self, other):
        return self.asset_tag == other.asset_tag

class Computer(Machine):
    category = 'Computing Device'

    def compute(self, expr):
        return eval(expr)

class Laptop(Computer):
    pass

class Server(Computer):
    pass

class Macbook(Laptop):
    manufacturer = 'Apple'
    def __init__(self, screen_size, has_usb3=True, *args, **kwargs): # "explicit self"
        self.screen_size = screen_size
        self.has_usb3 = has_usb3
        super(Macbook, self).__init__(*args, **kwargs)

    def compute(self, *args, **kwargs):
        sleep(.5)
        return super(Macbook, self).compute(*args, **kwargs)

    def __repr__(self):
        return 'Macbook(screen_size = %r, has_usb3 = %r, asset_tag = %r)' % (self.screen_size, self.has_usb3, self.asset_tag)

mb1 = Macbook(13,        asset_tag = '12kj')
mb2 = Macbook(15, False, asset_tag = '2i3m')
mb3 = Macbook(15, True,  asset_tag = 'zm78')
mb4 = Macbook(17,        asset_tag = '12kj')

class XServer(Server):
    def __init__(self, cores=8, *args, **kwargs):
        self.cores = cores
        super(XServer, self).__init__(*args, **kwargs)
    def __repr__(self):
        return 'XServer(cores = %r, asset_tag = %r)' % (self.cores, self.asset_tag)

xs1 = XServer(16, asset_tag='wu23')
xs2 = XServer(8,  asset_tag='i96e')

class Cluster(object):
    def __init__(self, *machines):
        self.machines = set(machines)

    def __add__(self, other):
        return Cluster(*(self.machines | other.machines))

    def __len__(self):
        return len(self.machines)

    def __iter__(self):
        return iter(self.machines)

    def __repr__(self):
        output = []
        for machine in self:
            output.append(repr(machine))
        return 'Cluster(machines=[%s])' % ', '.join(output)

    def __call__(self, expr):
        for machine in self:
            print machine, machine.compute(expr)

    def __getitem__(self, asset_tag):
        for machine in self:
            if machine.asset_tag == asset_tag:
                return machine
        raise KeyError('no such machine with asset_tag %r' % asset_tag)

c1 = Cluster(mb1, mb2, mb3, mb4)
c2 = Cluster(xs1, xs2)

