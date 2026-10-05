numbers=[1,2,3,4,5,6]
max=numbers[0]
min=numbers[0]
total=0
for num in numbers :
    if max>num :
        max=num
    if min<num:
        min=num
    total=total+num
print("maximum:",max)
print("minimum:",min)
print('total',total)