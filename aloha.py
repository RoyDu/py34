#import csv
#with open("t1.csv","r") as fileCsv

def testkw(name, cell, **kw):
	print('name:', name, 'cell:',cell, 'other:',kw)

testkw('duzq', 18642, team='DST',status='newmember',act='enrolling')

		
def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

print(fact(10))


L=[]
n=1
while n<100:
	L.append(n)
	n+=2
print(L)

print(L[::5])
