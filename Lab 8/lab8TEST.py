# lab8TEST.py

>>> from lab8 import *

##### printPattern #####

>>> printPattern(8,0)
*
**
 *
****
  *
  **
   *
********
    *
    **
     *
    ****
      *
      **
       *

>>> printPattern(4,2)
  *
  **
   *
  ****
    *
    **
     *
>>> printPattern(4)
*
**
 *
****
  *
  **
   *
>>> [printPattern(n,k) for n in (2,4) for k in (1,3)]
 *
 **
  *
   *
   **
    *
 *
 **
  *
 ****
   *
   **
    *
   *
   **
    *
   ****
     *
     **
      *
[None, None, None, None]
>>> 

##### gcd #####


>>> gcd(5,0)
5
>>> gcd(15,5)
5
>>> gcd(5,7)
1
>>> gcd(24,144)
24
>>> gcd(124,144)
4
>>>
>>> [ (m,n,gcd(m,n)) for m in range(0,12,3) for n in range (0,12,4)]
[(0, 0, 0), (0, 4, 4), (0, 8, 8), (3, 0, 3), (3, 4, 1), (3, 8, 1), (6, 0, 6), (6, 4, 2), (6, 8, 2), (9, 0, 9), (9, 4, 1), (9, 8, 1)]

##### count #####

>>> count( [1,2,3,[4,5,5],[[5,2,1],4,5],[3]], 1 )
2
>>> count( [1,2,3,[4,5,5],[[5,2,1],4,5],[3]], 5 )
4
>>> count( [1,2,3,[4,5,5],[[5,2,1],4,5],[3]], 0 )
0
>>> count( [[[[[4, 6], 0], [1, 4]], [[4, [1, 4]], 8]], [[6, 3], [0, [[4, 5], 5]]]], 4 )
5
