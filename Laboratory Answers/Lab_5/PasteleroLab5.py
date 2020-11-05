'''
  --------Lab Exercise 5 (Snakes)-------
  Name: Cyrus David G. Pastelero
  Subject: Programming Paradigms
  Section: A
  Date: Nov 5, 2020
  -------------------------------------
'''
from math import sqrt

#def doubledInt(x:int) -> int:
def doubleInt(x):
    return x * 2

#def largest(x:float,y:float) -> float:
def largest(x, y):
    return x if x > y else y

#def isVertical(a:(float,float),b:(float,float)) -> bool:
def isVertical(a, b):
    return True if a[0] == b[0] and a[1] != b[1] else False

#def primes(n:int) -> [int]:
def primes(n):
    ans = []
    curr = 2
    while (len(ans) <= n):
        for x in range(2, int(sqrt(curr) + 1)):
            if curr %  x == 0:
                break
        else:
            ans.append(curr)
        curr += 1
    return ans

#def fibonacciSequence(n:int) -> [int]:
def fbonacciSequence(n):
    fib = [0, 1]
    while (len(fib) <= n):
        fib.append(fib[-2] + fib[-1])
    return fib

#def sortedIntegers(l:[int]) -> [int]:
def sortedIntegers(l):
    for i in range(len(l)):
        min = i
        for x in range(i + 1, len(l)):
            if l[x] < l[min]:
                min = x
        l[i], l[min] = l[min], l[i]
    return l

#def sublists(l:[int]) -> [[int]]:
def sublists(l):
    subl = [[]]
    for i in range(len(l) + 1):
        for j in range(i + 1, len(l) + 1):
            subl.append(l[i:j])
    return subl

#def fme(b:int,p:int,m:int) -> int:
def fme(b, p, m):
    ans = 1
    while p:
        if p & 1: #if the last digit of binary form p is 1
            ans = (ans * b) % m
        b = (b * b) % m
        p >>= 1 #moves binary to right one place
    return ans

#TEST CASES:

def main():
    #1
    print("Number 1: double of {} is {}".format(2, doubleInt(2)))

    #2
    print("Number 2: largest between {} and {} is {}".format(4.3, 4.2, largest(4.3, 4.2)))
    print("Number 2: largest between {} and {} is {}".format(4.34, 4.32, largest(4.34, 4.32)))

    #3
    print("Number 3: is p({},{}) to p({},{}) vertical? {}".format(2, 3, 1, 3, isVertical((2,3), (1,3)))) #horizontal line
    print("Number 3: is p({},{}) to p({},{}) vertical? {}".format(2, 2, 1, 3, isVertical((2,2), (1,3)))) #diagonal line
    print("Number 3: is p({},{}) to p({},{}) vertical? {}".format(1, 2, 1, 3, isVertical((1,2), (1,3)))) #vertical line
    print("Number 3: is p({},{}) to p({},{}) vertical? {}".format(1, 3, 1, 3, isVertical((1,3), (1,3)))) #Point

    #4
    print("Number 4: First 10 primes are {}".format(primes(10)))

    #5
    print("Number 5: First 10 fiboncci sequence are {}".format(fbonacciSequence(10)))

    #6
    print("Number 6: The sorted list of {} is {}".format([1,2,0,-3,23,1,4,5,9], sortedIntegers([1,2,0,-3,23,1,4,5,9])))

    #7
    print("Number 7: Sublists of {} are {}".format([1,2,3,4], sublists([1,2,3,4])))

    #8
    print("Number 8: {}^{} mod {} = {}".format(21231120121, 117, 311211, fme(21231120121, 117, 311211)))
    print("Number 8: {}^{} mod {} = {}".format(7, 256, 13, fme(7, 256, 13)))
    print("Number 8: {}^{} mod {} = {}".format(5, 117, 19, fme(5, 117, 19)))
    print("Number 8: {}^{} mod {} = {}".format(7, 1000000000, 13, fme(7, 1000000000, 13)))

main()
