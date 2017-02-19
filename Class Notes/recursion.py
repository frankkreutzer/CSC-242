# recursion.py

##### recursive function #####

'''
recursive function is a function that
calls itself

generally, 2 parts:

    1) base case(s) - deal with "smallest" inputs
       directly, no recursion
    2) recursive case(s) - general cases, call
       the function with "smaller" inputs

advice:

    1) write base case(s) first
    2) play around with examples until you
       see the pattern, then write it
'''


##### "review" #####

def h(n):
    print( 'start h', vars() )
    print(n)
    print( 'end h', vars() )

def g(n):
    print( 'start g', vars() )
    h(n-1)
    print( 'end g', vars() )

def f(n):
    print( 'start f', vars() )
    g(n-1)
    print( 'end f', vars() )

'''
like nesting russian dolls:

notice that that n exists
simulaneously with different values
in different namespaces
(and that is ok)
'''

##### recursive functions that print #####

'''
pattern: if it looks like a loop might work
try a peel off one strategy
'''


def countdown(n):
    print(n)
    if n==0:   # base case, no recursive call
        print( 'Blast off!')
    else:
        countdown(n-1)   # recursive call


# bad - no base case - infinite recursion
def f(n):
    print( n )
    f(n-1)

'''
>>> f(3)
????
'''

'''
make this work: (no loops or strs)
>>> vertical(3124)
3
1
2
4
>>> vertical(7)
7
>>> vertical(76)
7
6
>>> vertical(3124) -> 312 4
3
1 <- vertical(312)
2

4  print(4)
>>> vertical(12345) -> 1234 5
1
2 <- vertical(1234)
3
4

5 print(5)
>>> vertical(n) -> n//10  n%10
vertical(n//10)
print(n%10)
'''

def vertical(n):
    ''' n>=0 integer'''
    if n<10:
        print(n)
    else:
        vertical(n//10)
        print(n%10)

'''
vertical(123) ->
vertical(12), print(3) ->
vertical(1), print(2), print(3) ->
print(1), print(2), print(3)
'''

'''
make this work:  no loops or str
>>> reverse(1234)
4321
>>> reverse(7)
7
>>> reverse(345) -> 34 5
5 reverse(34)
543
>>> reverse(1234) -> 123 4
4 reverse(123)
>>> reverse(n) -> n//10  n%10
n%10 reverse(n//10)
'''

def reverse(n):

    if n<10: # base case, single digit
        print(n,end='')
    else:
        print(n%10,end='')
        reverse(n//10)

'''
make this work:
>>> cheers(0)
Hooray!
>>> cheers(1)
Hip Hooray!
>>> cheers(2)
Hip Hip Hooray!
>>> cheers(3)
Hip Hip Hip Hooray!
Hip cheers(2)
>>> cheers(n)
Hip cheers(n-1)
'''

def cheers(n):
    if n==0:
        print('Hooray!')
    else:
        print('Hip ',end='')
        cheers(n-1)

# something different, not so clear
# how to write with a loop

'''
>>> pattern(0)
0
>>> pattern(1)
010
>>> pattern(2)
0102010
>>> pattern(3)
010201030102010
pattern(2) 3 pattern(2)
>>> pattern(n)
pattern(n-1) n pattern(n-1)
'''

# v1 - with explicit base case
def pattern(n):
    if n==0:
        print(0,end='')
    else:
        pattern(n-1)
        print(n,end='')
        pattern(n-1)


# v2 - with empty base case
def pattern(n):
    if n>=0:
        pattern(n-1)
        print(n,end='')
        pattern(n-1)


### returning values ###
def factorial(n):
    if n <= 1:   # base cases
        return 1
    else:
       return n * factorial(n-1)

#recursive
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

#iterative
def fib(n):
    curr, prev = 1, 0
    for i in range(n):
        curr, prev = curr + prev, curr
    return curr

def pattern(n):
    if n==0:
        return '0'
    else:
        #return pattern(n-1) + str(n) + pattern(n-1)

        #more efficient
        prev = pattern(n-1)
        return prev + str(n) + prev


### turtle graphics ###
from turtle import Screen, Turtle

def draw(directions, length = 100, angle = 90, x = 0, y = 0):
    s = Screen()
    t = Turtle()
    t.up()
    t.setpos(x,y)
    t.down()

    for move in directions:
        if move == 'F':
            t.forward(length)
        elif move == 'L':
            t.left(angle)
        elif move == 'R':
            t.right(angle)
        else:
            print('bad move')
    s.exitonclick()

'''
k=0: koch(0) -> 'F'
k=1: koch(1) -> 'FLFRRFLF'
K=2: KOCH(3) -> 'FLFRRFLF + L + FLFRRFLF + RR + FLFRRFLF + L + FLFRRFLF
'''

def kock(n):
    if n == 0:
        return 'F'
    else:
        k = koch(n-1)
        return k + 'L' + k + 'RR' + k + 'L' + k


### pascalLine on hw ###
'''
def pascalLine(n):
    start = 1
    row = [start]
    for i in range (n):
        newValue = (newValue * (n-i)) / ( i + 1 )
        row.append(newValue)

    print(row)
    print()
'''

### base on hw ###
'''
base(134, 7) = base(134//7, 7) + str(134%7)
base case: if n < base
'''

### help on the lab ###
'''
>>> patt(1)
1
>>> patt(2)
22
 1
 1
>>> patt(3)
333
 22
  1
  1
 22
  1
  1
>>> patt(4)
4444
 333
  22
   1
   1
  22
   1
   1
 333
  22
   1
   1
  22
   1
   1
'''

def patt(n, shift = 0):
    if n == 1:
        print(shift * ' ' + '1')
    else:
        print(shift * ' ' + n * str(n))
        patt(n - 1, shift + 1)
        patt(n - 1, shift + 1)

### trees ###

def traverse(tree):
    if type(tree) != list:
        print(tree)
    else:
        for branch in tree:
            taverse(branch)
