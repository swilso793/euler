"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""
dc = dict()

def fib(n):
    if n<2:
        return n
    if n-1 not in dc.keys():
        dc[n-1] = fib(n-1)
    if n-2 not in dc.keys():
        dc[n-2] = fib(n-2)
    return dc[n-1] + dc[n-2]   


(fib(60))
print(sum([i for i in dc.values() if i<4000000 and i%2==0]))