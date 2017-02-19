from tkinter import *
from tkinter.messagebox import showinfo
from random import *

class ScoreError(Exception):
    pass

class ScoreList(list):
    def validate(item):
        if item < 0 or item > 100:
            raise ScoreError('score ' + str(item) + ' not between 0 and 100')

    def __init__(self, lst = None):
        if lst != None:
            for i in lst:
                if i < 0 or i > 100:
                    raise ScoreError('score ' + str(i) + ' not between 0 and 100')
                else:
                    self.append(i)

    def __repr__(self):
        return 'ScoreList({})'.format(list.__repr__(self))

    def add(self, item):
        ScoreList.validate(item)
        list.append(self, item)

    def avg(self):
        total = sum(self)
        total = float(total)
        return total/len(self)

    def passing(self):
        if ScoreList.avg(self) >= 60:
            return True
        else:
            return False

    def min(self):
        return min(self)

    def max(self):
        return max(self)

    def len(self):
        return len(self)


class Scrambler(Frame):
    def __init__(self, word, parent = None):
        Frame.__init__(self, parent)
        self.word = word
        scramble = list(word)
        shuffle(scramble)
        scramble = ''.join(scramble)

        Label(self, text = scramble).pack()
        self.entry = Entry(self)
        self.entry.pack()

        Button(self, text = 'Guess', command = self.click).pack()
        self.guesses = 3

    def click(self):
        self.guesses -= 1
        guess = self.entry.get()

        if guess != self.word and self.guesses > 1:
            showinfo("Wrong", "You have " + str(self.guesses) + " guesses left.")

        elif guess != self.word and self.guesses == 1:
            showinfo("Wrong", "You have " + str(self.guesses) + " guess left.")

        elif guess == self.word:
            showinfo("Correct", "You got it!")

        elif guess != self.word and self.guesses == 0:
            showinfo("Lose", "Sorry, you lose.")



if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'lab6TEST.py'))
