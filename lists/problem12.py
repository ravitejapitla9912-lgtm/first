lst=[1,1,2,3,4,4,5,6,7]
new=[]
for elements in lst:
    if(elements not in new):
        new.append(elements)
print("withouth duplicates is",new)    