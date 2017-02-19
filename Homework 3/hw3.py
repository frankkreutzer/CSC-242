class EmptyStatError(Exception):
    pass

class Stat():
    def __init__(self, lst = []):
        self.s = list(lst)

    def __repr__(self):
        return "Stat({})".format(self.s)

    def add(self, item):
        self.s.append(item)

    def __len__(self):       
        return len(self.s)

    def min(self):
        if len(self.s) == 0:
            raise EmptyStatError("empty Stat does not have a min")
        else:
            return min(self.s)
        
    def max(self):
        if len(self.s) == 0:
            raise EmptyStatError("empty Stat does not have a max")
        else:
            return max(self.s)

    def sum(self):
        return sum(self.s)

    def mean(self):
        if len(self.s) == 0:
            raise EmptyStatError("empty Stat does not have a mean")
        else:
            return sum(self.s) / len(self.s)
            
    def clear(self):
        self.s *= 0 


class NotIntError(Exception):
    pass

class intlist(list):
    
    def validate(item):
        if type(item) != int:
            raise NotIntError(str(item) + ' not an int')

    def __init__(self, lst = None):
        if lst != None:
            for i in lst:
                if type(i)!=int:
                    raise NotIntError('Not an integer')
                else:
                    self.append(i)

    def __repr__(self):
        return 'intlist({})'.format(list.__repr__(self))

    def append(self, item):
        intlist.validate(item)
        list.append(self, item)

    def insert(self, index, item):
        intlist.validate(item)
        list.insert(self, index, item)

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def __setitem__(self, index, item):
        intlist.validate(item)
        list.__setitem__(self, index, item)

    def odds(self):
        odds = intlist()
        for num in self:
            if num % 2 == 1:
                odds.append(num)
        return odds

    def evens(self):
        evens = intlist()
        for num in self:
            if num % 2 == 0:
                evens.append(num)
        return evens
            



if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'hw3TEST.py'))
