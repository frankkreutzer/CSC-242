def silly(n):
    if n > 0:
        print('*' * n, end='')
        print('!' * n, end='')

def stars(n):
    if n > 0:
        stars(n-1)
        print('*' * n)
        stars(n-1)

def pattern(n):
    if n == 1:
        print(1, end='')
    else:
        pattern(n//2)
        pattern(n//2)
        print(n, end='')

my_pattern = pattern(8)
print(my_pattern)
