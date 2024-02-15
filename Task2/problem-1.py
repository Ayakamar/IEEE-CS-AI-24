def is_leap(year):
    if year %400 ==0:
        return True
    if year% 4!=0 or year %100==0:
        return False
    if year % 4== 0:
        return True 
         
            
year = int(input())
print(is_leap(year))