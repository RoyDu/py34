import os
from multiprocessing import Process

print(os.name)
print(os.path.abspath('.'))    #environment 
print(os.environ.get('SYSTEMROOT'))
os.rmdir('C:\AAAcode\py250')
print(os.listdir('../'))
os.mkdir('C:\AAAcode\py250')
print(os.listdir('../'))

print('Process (%s) start...' % os.getpid())