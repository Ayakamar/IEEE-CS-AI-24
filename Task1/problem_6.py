def summtion(num):
    sum =0
    for i in range(0, num+1 , 2):
        sum = sum + i 
    return sum

num= int(input())
result= summtion(num)
print(result)    