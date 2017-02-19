def printPattern(n, shift = 0):
    if n == 1:
        print(shift * ' ' + '*')
    else:
        printPattern(n // 2, shift)
        print(shift * ' ' + n * '*')
        printPattern(n // 2, shift + n // 2)


def gcd(m, n):
    if n == 0:
        return m
    elif m == 0:
        return n
    elif m >= n:
        return gcd(n, m - n)
    elif n > m:
        return gcd(m, n - m)



def count(lst, target):
    if type(lst) != list:
        return lst
    else:
        counter = 0
        for num in lst:
            if num == target:
                counter += 1
            elif type(num) == list:
                counter += count(num, target)
        return counter





if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab8TEST.py' ))
