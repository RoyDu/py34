# the usage of filter high-order func

def iseven(n):
	if n%2 == 1 :
		return n
L=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(iseven,L)))

L1=['a','','b','','dsaf','dsf','','d']

def isnil(s):
	return s.strip()
print(list(filter(isnil,L1)))

class Student(object):
	def __init__(self,name,gen):
		self.__name=name
		self._gen=gen



xiaodong = Student('liuxiaodong','male')
xiaozhang= Student('zhangxiao','female')
xiaozhang.age=23
print(xiaozhang.age)
#print(xiaodong.age)
print(xiaodong._Student__name)

class MaleStudent(Student):
	pass

liming = MaleStudent('liming','male')
print(liming._gen)
print(liming._Student__name)

print(isinstance(liming, Student))
print(isinstance(liming, MaleStudent))
print(isinstance(Student,MaleStudent))
print(type(Student))
print(type(123))
print(type(liming))
print(dir(liming))
print(hasattr(xiaozhang, 'age'))
setattr(liming,'grade',9)
print(hasattr(liming, 'grade'))
print(liming.grade)

def set_grp(self, grp):
	self.grp = grp;

from types import MethodType
liming.set_grp = MethodType(set_grp,liming)
liming.set_grp('basketball')
print(liming.grp)