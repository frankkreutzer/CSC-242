# guis.py

##### hw #####

'''
next hw posted
start now!!!
'''


##### midterm #####
'''
2 weeks from today
    usual room, usual time
    in class on computer
    you may bring: 2 double sided -OR- 4 single sided pages
                   of HARDCOPY NOTES (print before you come)
                   will be collected
    review hw, labs, classes
    read book
'''

##### Pizza #####

'''
start early
run the doctest
if you get stuck, email me your .py file


class Pizza:

    def __init__(self,size='M',toppings=[]):
        self.toppings = set( toppings )
        self.size = size

    def price(self):

        # use elifs!
        if self.size=='S':
            return .20+.75*len(self.toppings)
        elif self.size=='M':
            return .20+.75*len(self.toppings)
        elif self.size=='L':
            return .20+.75*len(self.toppings)

    def __eq__(self,other):

        if self.size==other.size and self.toppings==other.toppings:
            return True
        else:
            return False
        # like this more
        return self.size==other.size and self.toppings==other.toppings
    
        
        
def orderPizza():
    pie = Pizza()
    pie.setSize( ...size from user ...)

    while:
        pie.addTopping( ... topping from user ...)

    # print message
    return pie

'''


##### intlist #####

class NotIntError(Exception):
    pass



class intlist(list):


    def evens(self):
        ''' returns an intlist with all of the evens '''
        # create an empty intlist
        # iterate over self, add any even to the new intlist
        # return the new intlist

##### Mapping #####

'''
class Mapping(dict):

    # getitem for free

    def __setitem__(self,key,value):
        # remove old stuff first
        if key in self:
            self.pop(key)
        self[key]=value
        self[value==key


    def pop(self,key):
        val = self[key]
        dict.pop(self,key)
        if key!=val:
            dict.pop(self,val)
        
'''


##### GUIs/tkinter #####
'''
GUI - graphical user interface - "point and click" interface

API - application programming interface
      libarary of classes/function/methods
      that allow you to manipulate object in some enviroment

tkinter is a Python GUI API - lots of prebuilt "widgets"

tkinter widgets - building blocks

    Tk - main (root) window

    Frame - non-root window, customizable
            good for subclassing/inheriting from

    Label - displays text (mainly static - doesnt change)

    Entry - text box that a user can edit
       get() - method retrieves text
       insert(END,stuff) - appends to text
       delete(0,END) - delets

    Button - what it sounds like
       text = "text on button"
       command = eventhandler, will run eventhandler
                 when button is clicked
       bind() - we wont use this, but more flexible than command

    dialogs - seperate windows that can be opened
       showinfo

widget layout - 2 basic ways, cant mix them within a particular
    container

    pack() - adds it without much control

    grid(row=r,column=c,columnspan=cspan, rowspan=rspan)
        places widget in a grid at positiion (r,c)
        that spans cspan columns and rspan rows

        spans are optional and default to 1
'''

##### import #####

'''
import math
math.pi

from math import pi
from math import *
pi
'''

    
###### tkinter #####

'''
>>> from tkinter import Tk, Label
>>> root = Tk() # main window
>>> root.mainloop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    root.mainloop()
  File "C:\Python\lib\tkinter\__init__.py", line 1120, in mainloop
    self.tk.mainloop(n)
KeyboardInterrupt
Entry - text box that a user can edit
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> from tkinter import Tk, Label
>>> root = Tk() # main window
>>> hello = Label(master=root,text='hello,world')
>>> hello.pack()
>>> Label(root,text='more text').pack()
>>> Button(root,text='click me').pack()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Button(root,text='click me').pack()
NameError: name 'Button' is not defined
>>> from tkinter import *
>>> Button(root,text='click me').pack()
>>> def f():
	print('clicked!!!')

	
>>> Button(root,text='click me',command=f).pack()
>>> clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
Button(root,text='click me',command=f).pack()
>>> clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
clicked!!!
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> root.mainloop()

# creating an Entry

>>> root = Tk()
>>> e = Entry(root)
>>> e.pack()
>>> 

# showinfo, is not packed

>>> from tkinter.messagebox import showinfo
>>> showinfo( 'Title', 'main text')
'ok'
>>> 

>>> 
'''


##### pigLatin translator #####

# want this translator to be a widget
'''
want this to work:

>>> root = Tk()
>>> t = PigLatinTranslator(root)
>>> t.pack()

'''

from tkinter import *
from pigLatin import *
from tkinter.messagebox import showinfo

# inherit from Frame

class PigLatinTranslator(Frame):

    # add any sub widgets
    def __init__(self,parent=None):
        # always call Frame constructor
        Frame.__init__(self,parent)
        # entry, for named objects, two steps
        self.entry = Entry(self)  # creation, naming
        self.entry.pack()   # placement  
        # button, not named, 1 step
        Button(self,text='click to translate',command=self.onClickTranslate).pack()


    def onClickTranslate(self):
        print('translate')
        userinput = self.entry.get()
        showinfo('Pig Latin Translator', userinput + ' = ' + pigLatin(userinput) )

'''
root = Tk()
t = PigLatinTranslator(root)
t.pack()

'''

##### gridLayout ####

# layout in a grid, but cells can be combined



# not such a great example
class ButtonGrid(Frame):

    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        # create and layout buttons
        Button(self,text='1',width=10,height=10).grid(row=0,column=0,rowspan=2)
        Button(self,text='2',width=20,height=10).grid(row=0,column=1,rowspan=2,columnspan=2)
        Button(self,text='3',width=20,height=5).grid(row=2,column=0,columnspan=2)
        Button(self,text='4',width=10,height=5).grid(row=2,column=2)

# better example

class MyGrid(Frame):

    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        # create and layout buttons
        Label(self,text='type stuff here').grid(row=0,column=0)
        self.e1 = Entry(self,width=10)
        self.e1.grid(row=0,column=1)
        Label(self,text='type stuff here').grid(row=1,column=0)
        self.e2 = Entry(self,width=10)
        self.e2.grid(row=1,column=1)
        Button(self,text='click me').grid(row=2,column=0,columnspan=2)
        

    
# MyGrid().pack()






















        
    




