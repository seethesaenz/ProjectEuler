#Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome():
    biggestPalin = [0]
    x = 1000
    y = 1000
    while(y > 100):

        while (x > 100):

            maybePalin = x * y
            maybe1Palin = [int(i) for i in str(maybePalin)]
            maybe2Palin = maybe1Palin[::-1]
            if(maybe1Palin == maybe2Palin):
                if(len(maybe1Palin)>len(biggestPalin) or maybe1Palin[0]>biggestPalin[0]):
                    biggestPalin = maybe1Palin
            x -= 1
        x = 1000
        y -= 1
        print(biggestPalin)
palindrome()


