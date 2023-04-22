total=input("What is the total bill?\n")
tipper=input("what percentagetip would you like to give?10. 12, or 15?\n")
persons=input("How many peopleto split the bill?\n")
myshare=int(total)/int(persons)
tip=int(myshare)*(100+int(tipper))/100
print(round(tip,2))