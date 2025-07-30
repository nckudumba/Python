# RECURSION

import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

c = 0
def python():
    global c
    c += 1
    print("Python y", c)
    python()

python()