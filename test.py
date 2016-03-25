import os

def myabs(b):
	if b>=0:
		return b
	else:
		return -b
print(myabs(-2.5))

print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s,str)])

L2 = [x*x for x in range(20)]
print(L2)

g = (x*x for x in range(20))
for gm in g:
	print(gm)


def triangles():
    L=[1]
    while True:
        yield L
        L = [1]+[L[I]+L[I+1] for I in range(len(L)-1)]+[1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

L=[1,2,3,4,5,6,7,8,9,10]
#print([L[i]+L[i+1] for i in range(len(L)-1)])
print(L[0]+L[1])

