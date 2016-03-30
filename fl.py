#test for file operation

with open('C:/AAAcode/py34/a.txt','r') as f:
	for line in f.readlines():
		print(line.strip())
	#print(f.readlines())