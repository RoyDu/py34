class Student(object):
	@property
	def age(self):
	    return self._age
	
	@age.setter
	def age(self, value):
		self._age = value

	def __str__(self):
		return 'this class is Student!'

	__repr__ = __str__;

'''	@property
	def name(self):
		return self._name'''

s = Student()
s.age = 18
print(s.age)
s.name='lucy'
print(s.name)
s
#print(s)	