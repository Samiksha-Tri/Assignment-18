"""Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value."""

l1=[1,2,3]
l2=['UP','MP','Bihar']
i=1
dict1={}
for e in l2:
    dict1[i]=e
    i+=1
print("dictionary is :",dict1)    
