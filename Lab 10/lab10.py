def maximum(lst):
    if type(lst) == int:
        return lst
    if len(lst) == 0:
        return 0
    else:
        maxes = []
        for branch in lst:
            maxes.append(maximum(branch))
        return max(maxes)
            


def printstack(n, indent=0):
    if n > 0:
         printstack(n-1, indent+1)
         print(' ' * indent + 'U ' * n)


         
if __name__=='__main__':
    import doctest
    print(doctest.testfile( 'lab10TEST.py'))
