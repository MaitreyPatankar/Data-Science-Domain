# Algorithms

# NAIVE GCD ALGORITHM

def gcd(m,n):

    # empty list to store the factors of m
    fm = []
    for i in range(1, m+1):
        if (m % i) == 0:
            fm.append(i) # append means add the element to the end of the list

    # empty list to store the factors of n
    fn = []
    for j in range(1, n+1):
        if (n % j) == 0:
            fn.append(j)

    # empty list to store the common factors of m & n
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    # to return the last element from left side or the first element from right side
    return cf[-1]

'''
Program is a sequence of steps.
Some steps are repeated while some are executed conditionally.

takes time proportional to number
'''

# *******************************************

'''
Why not a single scan from 1 to max(m,n)?
    For each i in 1 to max(m.n), add i to fm if i divides m and add i to fn if i divides n
Why compute two lists and then compare them?
    For each i in 1 to max(m,n), if i divides m and i also divides n, then add i to cf.
Any common factor must be less than min(m,n)
'''

def gcd2(m,n):
    cf = []
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            cf.append(i)

    return cf[-1]

# -----------------------------------------

'''
Do we need lists at all?
We only need the largest common factor
    Discard the previous factor if it is smaller than the current one
'''

def gcd3(m,n):
    for i in range(1, min(m,n)+1):
        if (m%i) == 0 and (n%i) == 0:
            mrcf = i # most recent common factor
    return mrcf

# -----------------------------------------

'''
To find the largest common factor, start at the end and work backwards
Let i run from min(m,n) to 1
First common factor will be the gcd
'''

def gcd4(m,n):
    i = min(m,n)

    while i > 0:
        if (m%i) == 0 and (n%i) == 0:
            return i
        else:
            i = i-1 # update i
    return None

'''
While loop is used when number of steps are not known.
The loop must terminate.
'''

# -----------------------------------------

# EUCLID'S ALGORITHM FOR GCD
'''
The efficiency of the above all algorithms are the same.

Euclid's Algorithm (Recursion) - First Version
    Suppose d divides both m and n and m > n
    m = ad & n = bd
    m - n = ad - bd = (a-b)d > 0
    d divides m-n as well
    gcd (m,n) = gcd(min(m,n), m-n)
'''
# Assume m >= n
def euclid_gcd(m,n):
    if m < n:
        (m,n) = (n,m) # swap

    if (m%n) == 0:
        return n
    else:
        diff = m-n
        # diff > n? Possible!
        return euclid_gcd(max(n,diff), min(n,diff))

'''
Recursion
    Solve a smaller problem for the given big problem and returning that answer.
    Like a while loop which invokes a function.
'''

# -----------------------------------------

'''
Euclid's Algorithm (Recursion) - Second Version
    replace recursive call by a while loop
'''

def euclid_gcd2(m,n):
    if m<n:
        (m,n) = (n,m)

    while (m%n) != 0:
        diff = m-n
        (m,n) = (max(n,diff),min(n,diff))
    return n

'''
while loop replaces the computation of (m,n) to (max(n,diff),min(n,diff))
Do this until we hit at most 1.
'''

# -----------------------------------------

'''
Even Better Solution
    Suppose n does not divide m
    Then m = qn + r, where q is quotient and r is the remainder.
    Assume d divides both m and n (m = ad and n = bd).
    ad = q(bd) + r which means d also divides r.

takes time proportional to number of digits
'''

def euclid_gcd3(m,n):
    if n>m:
        (m,n) = (n,m)

    if (m%n) == 0:
        return n
    else:
        r = m%n
    return euclid_gcd3(n,r)

# -----------------------------------------

# while loop

def euclid_gcd4(m,n):
    if n>m:
        (m,n) = (n,m)

    while (m%n) != 0:
        (m,n) = (n,m%n) # m%n < n always
    return n

# -----------------------------------------