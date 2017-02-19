class Stack():
    def __init__(self, lst = []):
        self.s = list(lst)

    def __repr__(self):
        return('Stack({})'.format(self.s))

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop()

    def isEmpty(self):
        return len(self.s) == 0

    def __getitem__(self, index):
        return self.s[index]

    def __len__(self):
        return len(self.s)

def parenthesesMatch(string):
    s = Stack()
    openChars = '([{'
    closeChars = ')]}'
    for char in string:
        if char in openChars:
            s.push(char)
        elif char in closeChars and s.isEmpty() == True:
            return False
        elif char in closeChars and s.isEmpty() == False:
            pair = s.pop() + char
            if pair not in '()[]{}':
                return False

    return s.isEmpty() == True






if __name__=='__main__':
    import doctest
    print( doctest.testfile('lab3TEST.py') )
