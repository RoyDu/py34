'''
class fab(object): 

    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 

    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()


'''

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

f=fab
for n in f(5):
    print(n)

'''
f=fab(5)
for n in f:
    print(n)

for n in fab(5):
    print(n)'''
