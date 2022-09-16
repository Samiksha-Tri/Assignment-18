# Write a python program to merge two python dictionaries into one dictionary.

d1={1: 'UP', 2: 'MP', 3: 'Bihar'}
d2={'a':'India','b':'USA','c':'UK'}
print("dict1 :",d1)
print("dict2 :",d2)
finaldict={**d1,**d2}
print("final dictionary :",finaldict)