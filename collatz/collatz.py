import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize 

# Questions 1, 2, & 3

# classic Collatz function
def f(n, increment=0):
    i = increment + 1
    if n == 1:
        return i
    if n % 2 == 0:
        return f(n/2, i)
    else:
        return f(3*n+1, i)

# Factor out all twos version
def g(n, increment=0):
    i = increment + 1
    if n == 1:
        return i
    if n % 2 == 0:
        while n % 2 == 0:
            n = n / 2
        return g(n, i)
    else:
        return g(3*n+1, i)

# plots the graph of a(n) vs b(n)
a_list = []
b_list = []
n_list = []

for n in range(1, 10_000, 2):
    n_list.append(n)
    a_list.append(f(n))
    b_list.append(g(n))

a_list = np.array(a_list)
b_list = np.array(b_list)
n_list = np.array(n_list)

plt.bar(n_list, a_list)
plt.title('Number of steps for f(n) to reach 1')
plt.xlabel('n')
plt.ylabel('a(n)')
plt.show()

plt.bar(n_list, b_list)
plt.title('Number of steps for g(n) to reach 1')
plt.xlabel('n')
plt.ylabel('b(n)')
plt.show()

plt.plot(a_list[50:], b_list[50:])
plt.title('Steps to 1 for f(n) vs g(n)')
plt.xlabel('a(n)')
plt.ylabel('b(n)')

# Linear least squares regression
A = np.vstack([a_list[50:], np.ones(len(a_list[50:]))]).T
m, k = np.linalg.lstsq(A, b_list[50:], rcond=None)[0]

plt.plot(a_list[50:], m*a_list[50:] + k, color='tab:red')
plt.show()

print(m)

'''
Remarks:
There are plateaus in the data (e.g. from 4457-4501, a(n) = 47 fourteen 
out of twenty-two times). This suggests that there may be some "expected" 
value of the function with other values being outliers, in a sense.

We get a slope of 0.7691880033183106 for b(n) / a(n) indicating that we
reduce the number of iterations required to reach one by about 23% when
we factor out all 2's in each even.
'''

# Questions 4 & 5

# Classic Collatz function, terminates when n < n0
def c(n0, n, increment=0):
    i = increment + 1
    if n < n0:
        return i
    elif n % 2 == 0:
        return c(n0, n/2, i)
    else:
        return c(n0, 3*n+1, i)

# Factor out all twos version, terminates when n < n0
def d(n0, n, increment=0):
    i = increment + 1
    if n < n0:
        return i
    elif n % 2 == 0:
        while n % 2 == 0:
            n = n / 2
        return d(n0, n, i)
    else:
        return d(n0, 3*n+1, i)

c_list = []
d_list = []
n_list = []

for n in range(3, 10_000, 2):
    n_list.append(n)
    c_list.append(c(n, n))
    d_list.append(d(n, n))

c_list = np.array(c_list)
d_list = np.array(d_list)
n_list = np.array(n_list)

plt.bar(n_list, c_list)
plt.title('Number of steps for f(n) to reach a number less than n')
plt.xlabel('n')
plt.ylabel('c(n)')
plt.show()

plt.bar(n_list, d_list)
plt.title('Number of steps for g(n) to reach a number less than n')
plt.xlabel('n')
plt.ylabel('d(n)')
plt.show()

plt.plot(c_list[50:], d_list[50:])
plt.title('Steps to a number less than n for f(n) vs g(n)')
plt.xlabel('c(n)')
plt.ylabel('d(n)')

A2 = np.vstack([c_list[50:], np.ones(len(c_list[50:]))]).T
m2, k2 = np.linalg.lstsq(A2, d_list[50:], rcond=None)[0]

# Linear least squares regression
plt.plot(c_list[50:], m2*c_list[50:] + k2, color='tab:red')
plt.show()

print(m2)

'''
Remarks:
It appears that for almost all values of n, c(n)=4 and d(n)=3.
This strengthens the idea that there is a typically occuring
pattern with occasional deviations.

The slope of d(n) / c(n) is 0.7736097450924649, indicating that
factoring out all 2's in each even reduces the number of iterations
by about 23%. This is roughly the same as that of b(n) / a(n). 
This may indicate that the number of steps required to reach a number 
less than n is roughly proportional to the number of steps required 
to reach 1. 
'''


# Question 6

def alpha(k):

    big = 0
    total = 0

    for n in range(101, 10000, 2):
        total += 1
        if c(n, n) >= k: 
            big += 1

    return big / total

alpha_list = []
k_list = []

for k in range(1, 300):
    k_list.append(k)
    alpha_list.append(alpha(k))

plt.plot(k_list, alpha_list)
plt.title('Proportion of n such that c(n)>k')
plt.xlabel('k')
plt.ylabel(r'$\alpha$(n)')

fit_func = lambda x, a: a * (1/x)
a_fit = optimize.curve_fit(fit_func, k_list, alpha_list)[0]

plt.plot(k_list, a_fit * (1/np.array(k_list)), color='tab:red', label=r'f(k) = {} / k'.format(round(a_fit[0], 3)))
plt.legend()
plt.show()

'''
Remarks:
alpha(n) rapidly approaches 0 as k increases. This indicates that, 
generally speaking, we expect the sequence to reach a number less than n 
in relatively few steps. Interestingly, for odd n < 10,000, we see that
50% of all possible starting values take 5 or fewer steps, 90% take 23 or
fewer steps, and 95% take 34 or fewer steps. This aligns with the earlier
observation that most values of n take 4 steps, and other values are mostly
outliers.
'''