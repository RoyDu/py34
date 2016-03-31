#test for file operation

import os
print(os.name)
print(os.path.abspath('.'))    #environment 
print(os.environ.get('SYSTEMROOT'))
os.rmdir('C:\AAAcode\py250')
print(os.listdir('../'))
os.mkdir('C:\AAAcode\py250')
print(os.listdir('../'))

print('Process (%s) start...' % os.getpid())








with open('C:/AAAcode/py34/a.txt','r') as f:
	for line in f.readlines():
		print(line.strip())
	#print(f.readlines())

#with open('C:/Users/Public/Pictures/Sample Pictures/Desert.jpg','rb') as img:
	#print(img.read())

from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('GBK'))
print(f.getvalue())

