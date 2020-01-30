# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
fibonacci = [1, 2]
evenFibonacci = []
x = 0


# making list of fibbonacci including both even and odd
def fibbonacci(x):
    # setting the limits of the sequence to not exceed 4M
    while fibonacci[-1] <= 4000000:
        # adding on the next sequence and counting up after
        fibonacci.append(fibonacci[x] + fibonacci[x + 1])
        x = x + 1
    # added this because the limit we set was exceeded so correct our list. there's probably a more elegent way but this works
    fibonacci.pop(-1)
    evenodd()


# decide to just take the values that are even and appending to new list. Don't know if its more efficient to just
# fibonacci.remove() the odd values instead
def evenodd():
    for i in fibonacci:
        if i % 2 == 0:
            evenFibonacci.append(i)


fibbonacci(x)
print(sum(evenFibonacci))
