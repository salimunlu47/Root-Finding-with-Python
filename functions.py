# Name: SALIM UNLU
# Date: 10/30/2013

import math

# OA2801 - Lab 4 (Root Finding)
# This file contains definitions of the functions used in the lab.

def f1(x):
    return x ** 2 - 3

def f2(x):
    return math.sin(x) - 2.0 * x / 3.0

def f3(x):
    return math.sin(x)

def f4(x):
    return math.pow(x,7) - 3.0

def f5(x):
    return math.pow(x,3) + (2 * math.pow(x,2)) - (3.0 * x) - 1.0

def f6(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

# Function f7 _ $14000 initial investment with $250 per month.    
def f7(x):
    return 14000 * math.pow((1+x/12.0), 36) + (250 * (math.pow((1+x/12.0), 36) - 1)) / (x/12.0) - 25000
    
# Function f7 _ $12500 initial investment with $300 per month.
def f8(x):
    return 12500 * math.pow((1+x/12.0), 36) + (300 * (math.pow((1+x/12.0), 36) - 1)) / (x/12.0) - 25000    
            
def f1_prime(x):
    return 2*x

def f2_prime(x):
    return math.cos(x) - 2.0 / 3.0

def f3_prime(x):
    return math.cos(x)

def f4_prime(x):
    return 7*math.pow(x,6)

def f5_prime(x):
    return 3*math.pow(x,2) + (4 * math.pow(x,1)) - 3.0

def f6_prime(x):
    return 4.0/math.pow((math.exp(x)+math.exp(-x)), 2)


# This function estimates the root of a given function f using the bisection method
# on a given interval [a,b] and using tolerance epsilon.
def bisection(f, a, b, epsilon):
    print ("running bisection with arguments %s, %f, %f, %f" % (f, a, b, epsilon))
    i=0
    while (abs(b-a)/2.0) > epsilon:
        mid=(a+b)/2.0
        val=math.sqrt(3)
        error=abs(b-a)/2.0
        print ('x%d=%.9f, low=%.9f, high=%.9f, e%d=%.9f' % (i, mid, a, b, i, error))
        if (f(a)*f(mid)) > 0:
            a=mid
        else:
            b=mid
        i=i+1
    mid=(a+b)/2.0
    error=abs(b-a)/2.0
    print ('x%d=%.9f, low=%.9f, high=%.9f, e%d=%.9f' % (i, mid, a, b, i, error))
    print ('iterations: %d' % i)
    print ('bisection answer: %.9f' % mid)
    return mid
# end of bisection
    
# This function estimates the root of a given function f having derivative fprime
# using Newton's method, given an initial estimate x0, and using tolerance epsilon
def newtons(f, fprime, x0, epsilon):
    print ("running newtons with arguments %s, %s, %f, %f" % (f, fprime, x0, epsilon))
    x=x0
    i=0
    while abs(f(x)) > epsilon:
        print ('x%d = %.9f, f(x%d) = %.9f' % (i, x, i, f(x)))
        x=x-f(x)/fprime(x)
        i=i+1
    print ('x%d = %.9f, f(x%d) = %.9f' % (i, x, i, f(x)))
    print ('total iterations: %d' % i)
    print ('newtons answer: %.9f' % x)
    return x
# end of newtons

