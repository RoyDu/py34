from functools import reduce

'''
def f(x):
	return x*x

r=map(f,[1,2,3,4,5,6])
print(list(r))

def addd(a,b):
	return a+b
li=[1,2,3,4,5,6]
a = reduce(addd,li)
print(a)

def modf(a,b):
	return a*10+b
b=reduce(modf,li)
print(b)

def normalize(name):

L1 = ['adam', 'NISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)	
'''

# multiple the memebers in list
def prod(L):
	def mul(a,b):
		return a*b
	return(reduce(mul,L))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))




