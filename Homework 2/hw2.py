
class Pizza():
    def __init__(self, size = 'M', toppings = set()):
        self.s = size
        self.t = set(toppings)

    def __repr__(self):
        return("Pizza('{}',{})".format(self.s, self.t))

    def setSize(self, size):
        self.s = size

    def getSize(self):
        return self.s

    def addTopping(self, toppings):
        self.t.add(toppings)

    def removeTopping(self, toppings):
        self.t.remove(toppings)

    def price(self):
        if self.s == 'S':
            return(6.25 + (len(self.t) * 0.70))
        elif self.s == 'M':
            return(9.95 + (len(self.t) * 1.45))
        elif self.s == 'L':
            return(12.95 + (len(self.t) * 1.85))

    def __eq__(self, other):
        return self.s == other.s and set(self.t) == set(other.t)


def orderPizza():
    pie = Pizza()
    print("Welcome to Python Pizza!")

    size = str(input("What size pizza would you like (S,M,L): "))
    pie.setSize(size)

    while True:
        topping = str(input("Type topping to add (or Enter to quit): "))
        pie.addTopping(topping)
        if topping == '':
            pie.removeTopping('')
            break

    print("Thanks for ordering!")
    print("Your pizza costs ${}".format(pie.price()))
    return pie



if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'hw2TEST.py'))
