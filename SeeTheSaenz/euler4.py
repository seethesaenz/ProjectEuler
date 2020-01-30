# Find the largest palindrome made from the product of two 3-digit numbers.
def palindrome():
    biggestPalin = [0]
    # setting the upper limit
    x = 1000
    y = 1000
    # setting the lower limits
    while y > 100:

        while x > 100:
            # brute forcing my way through every product starting at 999*999 and working down to 100*100
            maybePalin = x * y
            # converting the product into a list
            maybe1Palin = [int(i) for i in str(maybePalin)]
            # making new list the save as first list but reversed
            maybe2Palin = maybe1Palin[::-1]
            # comparing both lists if they are the same aka palindromic(is that a word lol)
            if (maybe1Palin == maybe2Palin):
                # setting the biggest palindrome if the product is longer or starts with a bigger number could be
                # broken if I had for example a palindrome 960069 and 980089. currently would not register that the
                # latter is in fact bigger
                if len(maybe1Palin) > len(biggestPalin) or maybe1Palin[0] > biggestPalin[0]:
                    biggestPalin = maybe1Palin
            x -= 1
        x = 1000
        y -= 1
        print(biggestPalin)

palindrome()
