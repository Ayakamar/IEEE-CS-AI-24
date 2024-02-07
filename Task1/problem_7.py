def fraction(num):
    factor=[]
    divider = 2
    while(num > divider):
        if num %divider ==0: 
            factor.append(divider)
            num //= divider
        divider +=1

    return factor

def is_prime(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

num = int(input())
result1 = fraction(num)
prime_factor = []
for i in range(len(result1)):
    if is_prime(result1[i]):
        prime_factor.append(result1[i])

print(*prime_factor)        

