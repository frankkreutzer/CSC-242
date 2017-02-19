def pascalLine(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        lastrow = pascalLine(n-1)
        return [1] + [lastrow[i] + lastrow[i+1] for i in range(len(lastrow)-1)] + [1]


def levy(n):
    if n == 0:
         return 'F'
    else:
        directions = levy(n-1)
        return directions.replace("F", "LFRRFL")


def base(n, b):
    if n < b:
        return str(n)
    else:
        return str(base(n // b, b)) + str(n % b)
        
            
            





if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'hw5TEST.py'))
