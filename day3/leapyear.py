#enter the year
year = int(input("Which year do you want to check? "))

if year%4==0:
    # if year%100!=0:
    #     print("Not a leap year ")
    # elif year%400!=0:
        print("leap year")
else :
    print("Not leap year")
