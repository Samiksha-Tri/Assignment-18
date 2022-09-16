"""7. Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries."""

dict1={'name1':'Abhishek','age1':22}
dict2={'name2':'samiksha','age2':23}
dict3={'name3':'awanish','age3':24}
dict4={**dict1,**dict2,**dict3}
print(dict4)