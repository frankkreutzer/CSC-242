from tkinter import *
from tkinter.messagebox import showinfo
    
class UnitError(Exception):
    pass

class Temperature():
    def __init__(self, temp = 0.0, deg = 'C'):
        if deg in 'Cc':
            self.d = 'C'
            self.t = float(temp)
        elif deg in 'Ff':
            self.d = 'F'
            self.t = float(temp)
        else:
            raise UnitError('Unrecognized temperature unit' + deg)
        
    def __repr__(self):
        return "Temperature({},'{}')".format(self.t, self.d)

    def __str__(self):
        return '{}°{}'.format(self.t, self.d)

    def convert(self):
        if self.d in 'Cc':
            cf = self.t * 9/5 + 32
            return Temperature(cf, 'F')
        

        elif self.d in 'Ff':
            cc = (self.t - 32) * 5/9
            return Temperature(cc, 'C')

    def __eq__(self, other):
        if self.d == other.d:
            return self.t == other.t
        else:
            ct = self.convert()
            return ct == other


class TempConverter(Frame):
    def onClick(self):
        self.userTemp = self.tempEntry.get()
        self.userUnit = self.unitEntry.get()
        try:
            showinfo('Conversion', '{}°{}={}'.format(self.userTemp, self.userUnit, Temperature(self.userTemp, self.userUnit).convert()))
        except:
            if self.userUnit not in 'FfCc':
                showinfo('Error:','Unit should be either C or F')
            else:
                showinfo('Error:', 'Temperature must be a decimal or integer')
   
                
    def __init__(self, parent = None):
        Frame.__init__(self, parent)

        #creating the temperature labels and entries
        tempLabel = Label(self, text = 'Temperature: ')
        tempLabel.grid(row = 0, column = 0)
        self.tempEntry = Entry(self)
        self.tempEntry.grid(row = 0, column = 1)

        unitLabel = Label(self, text = 'Unit (C or F): ')
        unitLabel.grid(row = 1, column = 0)
        self.unitEntry = Entry(self)
        self.unitEntry.grid(row = 1, column = 1)

        
        #creating the button
        Button(self, text = 'Click to convert', command = self.onClick).grid(row = 2, column = 0, columnspan = 2)



    


if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab5TEST.py' ))
