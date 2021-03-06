import os, time, random
from multiprocessing import Process
from multiprocessing import Pool

def long_time_task(name):
	print('run task %s (%s)...' %(name, os.getpid()))
	start = time.time()						
	time.sleep(random.random() *3)
	end = time.time()
	print('task %s runs %0.2f seconds.' %(name,(end-start)))

if __name__=='__main__':
	print('parent process is %s .' %os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('waiting for all children done...')
	p.close()
	p.join()
	print('All done.')
	



'''
print(os.name)
print(os.path.abspath('.'))    #environment 
print(os.environ.get('SYSTEMROOT'))
os.rmdir('C:\AAAcode\py250')
print(os.listdir('../'))
os.mkdir('C:\AAAcode\py250')
print(os.listdir('../'))

print('Process (%s) start...' % os.getpid())

def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()) )

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('child process will start.')
	p.start()
	p.join()
	print('Child process end.')
'''
