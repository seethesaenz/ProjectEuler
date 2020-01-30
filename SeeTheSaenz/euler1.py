# Find the sum of all the multiples of 3 or 5 below 1000.
def some_multiples():
    list1 = [0]
    #making list of all the multiples of 3
    i=0
    while i <= 997:
        list1.append(i+3)
        i = i+3
    i=0
    #adding in the multiples of 5 to the list
    while i <= 990:
        list1.append(i+5)
        i = i+5
    #this is using set() to get rid of multiple numbers in list e.g. 15 is a multiple of both 3 and 5 so it shows up in list twice
    list2=list(set(list1))
    return sum(list2)
print(some_multiples())
