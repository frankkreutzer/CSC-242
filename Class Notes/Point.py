# Point.py

##### review #####

'''
>>> "how are you".split()
['how', 'are', 'you']
>>> # Python executing
>>> str.split("how are you")
['how', 'are', 'you']
>>> 
'''

##### Point - v1 everything explicit #####

'''
make this work:
>>> p = Point()
>>> p.setx(3)
>>> p.sety(-2.3)
>>> p.get()
(3,-2.3)
>>> p.move(1,1)
>>> p.get()
(4,-1.3)

... more in v2 ...

in general:
    methods/defs are in class namespace
    data attributes are in object namespace

>>> p = Point()
>>> p.setx(3)
>>> p.sety(77)
>>> p.get()
(3, 77)
>>> vars( Point )
mappingproxy({'get': <function Point.get at 0x02D924B0>, 'setx': <function Point.setx at 0x02D92420>, '__module__': '__main__', '__doc__': None, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, 'sety': <function Point.sety at 0x02D92468>})
>>> vars( p )
{'x': 3, 'y': 77}
>>> 
    
'''

class Point():

    # a method is a function inside a class
    def setx(self,xcoord):
        self.x = xcoord

    def sety(self,ycoord):
        self.y = ycoord

    def get(self):
        return (self.x,self.y)

    def move(self,deltax,deltay):
        self.x += deltax
        self.y += deltay

'''
not everything is perfect ....

>>> p = Point()
>>> p.setx(8)
>>> p.get()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    p.get()
  File "C:/Users/cdminstructor/Documents/csc242Sedgwick/spring1150/Point.py", line 56, in get
    return (self.x,self.y)
AttributeError: 'Point' object has no attribute 'y'
>>> p.sety(8)
>>> p
<__main__.Point object at 0x02CC4A10>
>>> 
'''

##### Point - v2 - implicit methods #####

'''
some code runs implicitly:

__init__ - constructor - runs when an object
           is first created,  it initializes the
           object, main responsibility is to add
           any data attributes that are required

p = Point() --Python--> Point.__init__(p)

__repr__ - representation - returns a str version
           of the object when one is required.
           when do you need a str?: print,
           idle interaction, str(object)

           write this early!!! useful for debugging!

           (there is also __str__ which is similar)

print( p ) ---->   print( Point.__repr__(p) )



>>> # "review"
>>> # default arguments
>>> def f(a,b=0):
	print( a,b)

	
>>> f(2,3)
2 3
>>> f(9)
9 0
>>> 
'''

class Point():

    def __init__(self,xcoord=0,ycoord=0):
        # print( '__init__')
        self.x = xcoord
        self.y = ycoord

    def __repr__(self):
        #print( 'repr' )
        return "Point({},{})".format(self.x,self.y)

    # a method is a function inside a class
    def setx(self,xcoord):
        self.x = xcoord

    def sety(self,ycoord):
        self.y = ycoord

    def get(self):
        return (self.x,self.y)

    def move(self,deltax,deltay):
        self.x += deltax
        self.y += deltay    

# soon - operator overloading, overload ==

##### Point client #####

'''
want this to work:

>>> p = movePointAround()
Enter a point: 1,2
Point(1,2)
Move it how? 1,1
Point(2,3)
Move it how? 5,-5
Point(7,-2)
Move it how?
>>> p
Point(7,-2)
'''

#NOTE: this is NOT part of the Point class
def movePointAround():

    x,y = eval(input('Enter a point: '))
    p = Point(x,y)
    while True:
        ans = input('Move it how? ')
        if ans=="":
            break
        dx,dy = eval(ans)
        p.move(dx,dy)
        print( p )  # calls repr
    return p

##### Point - v3 - operators #####

'''
# still have a problem

>>> 
>>> Point(1,2)==Point(1,2)
False
>>> 

points with same coordinates should be considered
equal

while we are at in, make all this work:
>>> Point(1,2)==Point(1,2)
True
>>> Point(2,3)+Point(1,-1)
Point(3,2)
>>> p = Point(1,2)
>>> p+=Point(3,3)
>>> p
Point(4,5)


operators:
+ -> __add__
- -> __sub__
* -> __mul__

if you implement +, you get += for free

p+q -> Point.__add__(p,q)

Boolean operators:
== -> __eq__
!= -> __ne__
<  -> __lt__
<= -> __le__
>  -> __gt__
>= -> __ge__

p==q ->  Point.__eq__(p,q)

if you define ==, you get != for free

'''

class Point():

    def __init__(self,xcoord=0,ycoord=0):
        # print( '__init__')
        self.x = xcoord
        self.y = ycoord

    def __repr__(self):
        #print( 'repr' )
        return "Point({},{})".format(self.x,self.y)

    # operators
    # p==q
    def __eq__(self,other):
        print( '__eq__')
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
        # any one of these is also ok
        return self.x==other.x and self.y==other.y
        return (self.x,self.y)==(other.x,other.y)
        return self.get()==other.get()

    # p+q
    def __add__(self,other):
        print('__add__')
        return Point(self.x+other.x,self.y+other.y)

    # a method is a function inside a class
    def setx(self,xcoord):
        self.x = xcoord

    def sety(self,ycoord):
        self.y = ycoord

    def get(self):
        return (self.x,self.y)

    def move(self,deltax,deltay):
        self.x += deltax
        self.y += deltay   

    



























