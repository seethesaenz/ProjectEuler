#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sumSquare():
    list1 = []
    x = 1
    for i in range(100):
        list1.append(x)
        x += 1
    squares = []
    for number in list1:
        squares.append(pow(number, 2))
    sumOfSquares = sum(squares)
    squareOfSum = pow(sum(list1), 2)
    print(squareOfSum-sumOfSquares)


sumSquare()
