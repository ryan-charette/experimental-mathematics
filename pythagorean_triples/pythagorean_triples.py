from numpy import gcd

primitives = []
triples = []

for a in range(1,1_000):
    for b in range(1,1_000):
        if a <= b:
            c = (a**2+b**2)**0.5
            if int(c) == c:
                triples.append((a,b,int(c)))
                if gcd(a,b) == 1:
                    primitives.append((a,b,int(c)))

print(primitives)

odd_legs = []
odd_not_legs = []
odd_hypotenuse = []

for odd in range(1, 100, 2):
    for primitive in primitives:
        a, b, c = primitive
        if (a == odd or b == odd) and (not odd in odd_legs):
            odd_legs.append(odd)
        if c == odd and not odd in odd_hypotenuse:
            odd_hypotenuse.append(odd)
    if odd not in odd_legs:
        odd_not_legs.append(odd)

print('odd legs:', odd_legs)
print('odd not legs:', odd_not_legs)
print('odd hypotenuse:', odd_hypotenuse)

even_legs = []
even_not_legs = []

for even in range(2, 100, 2):
    for primitive in primitives:
        a, b, c = primitive
        if (a == even or b == even) and (not even in even_legs):
            even_legs.append(even)
    if even not in even_legs:
        even_not_legs.append(even)

print('even legs:', even_legs)
print('even not legs:', even_not_legs)

even_legs_all = []
even_not_legs_all = []

for even in range(2, 100, 2):
    for triple in triples:
        a, b, c = triple
        if (a == even or b == even) and (not even in even_legs_all):
            even_legs_all.append(even)
    if even not in even_legs_all:
        even_not_legs_all.append(even)

print('even legs all:', even_legs_all)
print('even not legs all:', even_not_legs_all)