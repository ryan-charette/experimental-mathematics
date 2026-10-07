import math

r =1_000

dict = []

#find all primes up to r (will be needed for prime factorization)
primes = [2,3,5]
for i in range(7,r):
    prime = True
    for x in range(2,int(math.sqrt(i))+2):
        if(i%x==0):
            prime=False
    if(prime): primes.append(i)

#calculate all multiplicities (optimized version)
dict.append(1)
for n in range(1,r):
    cnt = 0
    for a in range(0,int(math.sqrt(n))+2):
        for b in range(a,int(math.sqrt(n))+2):
            if(a**2+b**2==n):
                cnt += 4
                if(a!=b and a!=0 and b!=0):
                    cnt+=4
    dict.append(cnt)

correct_formula = True
for i in range(1,r):

    temp = i

    #find prime factorization
    factors = {}
    while(i>1):
        for p in primes:
            if(i%p==0):
                if(p in factors.keys()):
                    factors[p] += 1
                else:
                    factors[p] = 1
                i /= p

    #calculate f(n) according to formula
    f_n = 4 if (2 in factors.keys()) else 1
    mod_1 = 1
    for p in factors.keys():
        if(f_n==0): break
        if(p%4==3):
            f_n = max(f_n,4) if factors[p]%2==0 else 0
        if(p%4==1):
            mod_1 *= factors[p]+1
    if(f_n!=0 and mod_1!=0): f_n = max(f_n,mod_1*4)

    #compare actual multiplicity to f(n)
    if(f_n!=dict[temp]): formula=False

print("Is formula correct ? " + str(correct_formula))