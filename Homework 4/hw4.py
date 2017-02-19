from tkinter import *
from tkinter.messagebox import showinfo

def mask(word, exception):
    result = []
    for char in word:
        if char not in exception:
            result.append('?')
        else:
            result.append(char)
            
    return ''.join(result)

class hangman(Frame):
    def __init__(self, word, parent = None):
        Frame.__init__(self, parent)
        self.word = word.upper()

        #entries/labels
        wordLabel = Label(self, text = 'Word: ')
        wordLabel.grid(row = 0, column = 0, columnspan = 2)  
        self.wordEntry = Entry(self)             
        self.wordEntry.grid(row = 0, column = 2, columnspan = 4)
        
        rightLabel = Label(self, text = 'Right: ')
        rightLabel.grid(row = 1, column = 0, columnspan = 2)
        self.rightEntry = Entry(self)
        self.rightEntry.grid(row = 1, column = 2, columnspan = 4)
        
        wrongLabel = Label(self, text = 'Wrong: ')
        wrongLabel.grid(row = 2, column = 0, columnspan = 2)
        self.wrongEntry = Entry(self)
        self.wrongEntry.grid(row = 2, column = 2, columnspan = 4)

        #buttons
        labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for i in range(len(labels)):
            def cmd(key = labels[i]):
                self.click(key)
                
            b = Button(self, text = labels[i], width = 4, height = 2, command = cmd)
            b.grid(row = i//6+3, column = i%6)
            
        self.wordEntry.insert(END, mask(self.word, ''))

    def click(self, key):
        if key in self.word:
            if key not in self.rightEntry.get():
                self.rightEntry.insert(END, key)
                self.wordEntry.delete(0, END)
                self.wordEntry.insert(END, mask(self.word, self.rightEntry.get()))


        elif key not in self.word:
            if key not in self.wrongEntry.get():
                self.wrongEntry.insert(END, key)

        if '?' not in self.wordEntry.get():
            showinfo('Hangman', 'You win!')
        elif len(self.wrongEntry.get()) == 6:
            showinfo('Hangman', 'You lose')


    
hangman('pineapple').pack()
  
'''if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'hw4TEST.py'))'''
