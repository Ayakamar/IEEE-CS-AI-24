day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

if month % 2 ==0 and month !=2 :
    if day == 30:
        day =1
        if month > 12:
            month =1
            year +=1
        else :
            month+=1
    else :
        day +=1 

elif month ==2 and year %4 != 0 :
    if day == 28:
        day =1
        month == 3
    else :
        day +=1
elif month ==2 and year %4 ==0:
        if day == 29:
            day =1
            month == 3
        else :
            day +=1
else: 
    if day == 31:
        day =1
        if month > 12:
            month =1
            year +=1
        else :
            month+=1
    else :
        day +=1         

print("Day :", day, "    Month:", month, "    Year:", year)