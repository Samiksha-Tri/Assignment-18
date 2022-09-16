"""Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
"""

sample_dict = {'C': 92,'Java': 66,'Python': 85}
f=0
for e in sample_dict:
    if f==0:
        min=sample_dict[e]
        f=1
    if min>sample_dict[e]:
        min=sample_dict[e]
        key=e
print("key for minimum value :",key)        
