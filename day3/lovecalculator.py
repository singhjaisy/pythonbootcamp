print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowername1=name1.lower()
lowername2=name2.lower()

final=lowername1+lowername2

digit1=int(final.count('t'))+int(final.count('r'))+int(final.count('u'))+int(final.count('e'))
digit2=int(final.count('l'))+int(final.count('o'))+int(final.count('v'))+int(final.count('e'))
value=str(digit1)+str(digit2)
value1=int(value)

if ((value1>=90 ) or (value1<=10)):
    print(f"Your score is {value1}, you go together like coke and mentos.")
elif ((value1>=40 ) and (value1<= 50)):
    print(f"Your score is {value1}, you are alright together.")
else:
    print(f"Your score is {value1}")    

    
    



