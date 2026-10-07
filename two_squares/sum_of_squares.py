from sympy.ntheory import factorint
'''
function to create a list of numbers less than or equal to n
such that n can be written as a sum of squares.
'''
def sum_of_squares(n):

    squares = []
    square_sums = []
    max_num = int(n**0.5) + 1

    for num in range(1, max_num):
        squares.append(num**2)

    for a in squares:
        for b in squares:
            c = a + b
            if not c in squares and not c in square_sums and c <= n:
                square_sums.append(c)
            
    square_sums += squares
    square_sums.sort()

    return square_sums


n = 100
S = sum_of_squares(n)
S_C = [i for i in range(1, n+1) if i not in S]

S_4 = [s % 4 for s in S] 
S_8 = [s % 8 for s in S] 
S_16 = [s % 16 for s in S] 

print('S =', S)
print('S (mod 4) =', S_4) # 3 is not in the set
print('S (mod 8) =', S_8) # 3, 6, and 7 are not in the set
print('S (mod 16) =', S_16) # 3, 6, 7, 11, 12, 14, and 15 are not in the set

'Conjecture: Primes of form 4k + 3 and some of their multiples are not in S'

'''
Theorem I: 

If an integer n = 3 (mod 4), then n is not in S.

Proof: 

Let a and b be integers, and c = a^2 + b^2 be an element in S.

Case 1: a and b are both even. Then a = 2k and b = 2j for some integers
k and j. Thus, c = 4(k^2 + j^2) = 0 (mod 4)

Case 2: Either a or b, but not both, are even. Without loss of generality,
suppose a is even. Then a = 2k and b = 2j + 1 for some integers k and j.
Thus, c = 4(k^2 + j^2 + j) + 1 = 1 (mod 4)

Case 3: a and b are both odd. Then a = 2k + 1 and b = 2j + 1 for some
integers k and j. Thus, c = 4(k^2 + k + j^2 + j) + 2 = 2 (mod 4).

There is no case in which the sum of squares of two integers is congruent to
3 (mod 4), so any such integer is not an element of S.
'''

print('The prime factorization of each element s <= 100 in S is as follows:')
for num in S:
    print((num, factorint(num)))

prime_factors_3_mod_4 = []
for num in S:
    factor_dict = factorint(num)
    for factor in factor_dict.keys():
        if not factor in prime_factors_3_mod_4 and factor % 4 == 3:
            prime_factors_3_mod_4.append(factor)

print('4k + 3 primes that divide at least one element s <= 100 in S:', 
prime_factors_3_mod_4)
print('''The unique prime factorization of each multiple, m, of a 4k + 3
prime, p, such that p|s for some element s < 100 in S and m is not in S:''')
for factor in prime_factors_3_mod_4:
    for k in range(1, int(n/factor)):
        if not factor*k in S:
            print(factor*k, factorint(factor*k))

'''
Conjecture: 

A natural number $n$ can be written as a sum of two squares of natural numbers
if and only if every prime congruent to 3 modulo 4 in the unique prime 
factorization of $n$ occurs to an even power.
'''
S_1000 = sum_of_squares(1000)
prime_factors_1000 = []
for num in S_1000:
    factor_dict = factorint(num)
    for factor, count in factor_dict.items():
        if factor % 4 == 3:
            prime_factors_1000.append((factor, count))

print('(4k + 3 prime, exponent) for each element in S up to 1000', prime_factors_1000)

conjecture = True
for factor, exponent in prime_factors_1000:
    if exponent % 2 == 1:
        conjecture = False

print("Evidence seems to suggest that our conjecture is", conjecture)