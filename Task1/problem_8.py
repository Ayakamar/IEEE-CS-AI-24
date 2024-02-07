def fraction(num):
    factor=[]
    sum =0
    divider = 1
    while(num > divider):
        if num %divider ==0: 
            factor.append(divider)
            num //= divider
        sum +=divider
        divider +=1

    return sum
num = int(input())
result= fraction(num)
if result == num:
    print(num," is a prefecr number")
else:
     print(num," is not a prefecr number")   

