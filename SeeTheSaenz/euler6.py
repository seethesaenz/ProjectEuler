# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the 
# sum of the first 100 numbers. 
def sumSquare():
    list1 = []
    x = 1
    # made list of 1-100
    for i in range(100):
        list1.append(x)
        x += 1
    # made list with 1-100 squared
    squares = []
    for number in list1:
        squares.append(pow(number, 2))
    sumOfSquares = sum(squares)
    # squaring the sum of the list of 1-100
    squareOfSum = pow(sum(list1), 2)
    print(squareOfSum - sumOfSquares)
sumSquare()
