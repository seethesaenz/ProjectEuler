# Find the sum of all the multiples of 3 or 5 below 1000.

list1 = [0]
i =0
def unique(list1):
    list_set = set(list1)
    unique_list = (list(list_set))
    for x in unique_list:
        listUni.append(x)
while i <= 997:
    list1.append(i+3)
    i = i+3
i=0
while i <= 990:
    list1.append(i+5)
    i = i+5
list1.sort()
listUni=[]

print(list1)
unique(list1)
print(listUni)
print(sum(listUni))
