def fraction(num):
    if num ==1  or num ==0:
        return 1
    else:
        return  num * fraction(num-1)
        

num =int(input())
result= fraction(num)
print("The factorial of",num,"is",result)    