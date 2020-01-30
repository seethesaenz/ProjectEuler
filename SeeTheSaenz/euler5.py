#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def smallestMultiple():
    list20 = list(range(1, 21))
    startValue = 2520
    while(startValue % 2 != 0 or startValue % 3 != 0 or startValue % 4 != 0 or startValue % 5 != 0 or startValue % 6 != 0 or startValue % 7 != 0 or
    startValue % 8 != 0 or startValue % 9 != 0 or startValue % 10 != 0 or startValue % 11 != 0 or startValue % 12 != 0 or startValue % 13 != 0 or
    startValue % 14 != 0 or startValue % 15 != 0 or startValue % 15 != 0 or startValue % 16 != 0 or startValue % 17 != 0 or startValue % 18 != 0 or
    startValue%19 != 0 or startValue%20 !=0):
        for i in list20[::-1]:
            if (startValue % i != 0):
                startValue = startValue+(startValue%i)


        print(startValue)



smallestMultiple()
