# queues.py
# DO NOT call this queue.py


##### hw #####



##### review #####

'''
generally, for a class

    - data attributes in object namespace
    - methods in class namespace
    - some methods are called explicitly:
      get, set, ...
    - some methods are called implicitly:
      __init__,__repr__, operators

'''

##### Queue #####
'''
Queue class is used for representing a queue (line)
of objects, see  queuesTEST.py for client code.

We will base Queue on list, and provide
two implementations

v1 - composition, a Queue HAS A list atrribute
v2 - inheritance, a Queue IS A list


note about assignments and making copies

case 1: one list, lst and lst2 both refer to it

>>> lst = []
>>> lst2 = lst
>>> lst.append( 5 )
>>> lst
[5]
>>> lst2
[5]

case 2: two lists, lst2 is a copy of lst (constructor call)

>>> lst = []
>>> lst2 = list(lst)
>>> lst.append( 5 )
>>> lst
[5]
>>> lst2
[]
>>> 

'''

class Queue():

    # method is run many times
    # but its definition is run only ONCE
    # default arguments are only constructed once
    def __init__(self,lst=[]):
        # composition - self has a list, self.q
        # MUST call list constructor inside body of method! 
        self.q = list(lst) # very important, list() makes a copy!!!

    def __repr__(self):
        return 'Queue({})'.format(self.q)

    def enqueue(self,item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)

    # retrieves by index, q[1]    
    def __getitem__(self,index):
        return self.q[index]

    # we do NOT want to support indexed assignment
    # if we did, we could  uncomment this
    #def __setitem__(self,index,item):
    #    self.q[index]=item

    def __len__(self):
        return len(self.q)
        

##### review exceptions - try/except #####

'''
>>> # lots of code can cause errors
>>> 2+'3'
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    2+'3'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> eval('3')
3
>>> eval('three')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    eval('three')
  File "<string>", line 1, in <module>
NameError: name 'three' is not defined
>>> int('three')
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    int('three')
ValueError: invalid literal for int() with base 10: 'three'
>>> int('3')
3
>>> q
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    q
NameError: name 'q' is not defined
>>> 'abc'[99]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    'abc'[99]
IndexError: string index out of range
>>> open('hello.txt')
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    open('hello.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'hello.txt'
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> x = 0
>>> try:
	print(1/x)
except:
	print('uh oh, that didnt work')

	
uh oh, that didnt work
>>> try:
	print(1/x)
	int('three')
except ZeroDivisionError:
	print('uh oh, that didnt work')

	
uh oh, that didnt work
>>> x=77
>>> try:
	print(1/x)
	int('three')
except ZeroDivisionError:
	print('uh oh, that didnt work')

	
0.012987012987012988
Traceback (most recent call last):
  File "<pyshell#112>", line 3, in <module>
    int('three')
ValueError: invalid literal for int() with base 10: 'three'
>>> try:
	print(1/x)
	int('three')
except ZeroDivisionError:
	print('uh oh, that didnt work')
except ValueError:
	print( 'bad value')

	
0.012987012987012988
bad value
>>> 


how to raise (cause an error)!

'''

##### inheritance #####

# MyList inherits from list
# a MyList IS A list!!!!!
class MyList(list):
    pass

# inherit error classes

class CuttingError(Exception):
    pass

    

###### set #####

'''
>>> s = {2,3,4,2,2,23,2,2,2,7,7,9,'apple','pear'}
>>> s
{2, 3, 4, 7, 9, 'pear', 23, 'apple'}
>>> # to create an empty set
>>> # dont do this
>>> s = {}
>>> type(s)
<class 'dict'>
>>> # do this
>>> s = set()
>>> 
>>> s.add(9)
>>> s.add(9)
>>> s.add(7)
>>> d
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> s
{9, 7}
>>> s.remove(9)
>>> s
{7}
>>> s.add(8)
>>> len(s)
2
>>> for item in s:
	print( item )

	
8
7
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    s[0]
TypeError: 'set' object does not support indexing
>>> 
'''

##### Queue - v2 - inherit from list #####

# remember:  self IS A list !!!!

class CuttingError(Exception):
    pass

class Queue(list):

    # __init__, inherit it from list

    def __repr__(self):
        #return "Queue({})".format(list(self)) # probably ok
        return "Queue({})".format( list.__repr__(self) )

    def enqueue(self,item):
        self.append(item)
        # list.append(self,item)

    def dequeue(self):
        return self.pop(0)
        # return list.pop(self,0)

    # __getitem__ is inherited

    # override __setitem__
    def __setitem__(self,index,item):
        raise CuttingError('no cutting, you jerk')
        
if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'queuesTEST.py'))
        


















