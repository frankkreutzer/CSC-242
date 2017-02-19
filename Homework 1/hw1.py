class BankAccount():

    def __init__(self, initialBalance = 0):
        self.accBalance = initialBalance 

    def __repr__(self):
        return("BankAccount({})".format(self.accBalance))

    def set(self, amount):
        self.accBalance = amount

    def deposit(self, amount):
        self.accBalance += amount

    def withdraw(self, amount):
        self.accBalance -= amount

    def balance(self):
        return(self.accBalance)
    

def processAccount(filename ):
    with open(filename,'r') as f:
        b = BankAccount()
        startBal = f.readline().split()
        startBal = float(startBal[0])
        b.set(startBal)
        
        for line in f:
            fields = line.strip().split()
            if fields[0] in 'Ww':
                b.withdraw(float(fields[1]))
            elif fields[0] in 'Dd':
                b.deposit(float(fields[1]))
    
    return b





if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'hw1TEST.py'))

