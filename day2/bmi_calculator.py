height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi_height=float(height)
bmi_weight=float(weight)

bmi_height_1=bmi_height*bmi_height
bmi=bmi_weight/bmi_height_1
print(int(bmi))


#now the correct code
# bmi=int(weight)/float(height)**2
# bmi_as_int=int(bmi)
# print(bmi_as_int)


