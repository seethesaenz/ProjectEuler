#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
fibonacci = [1, 2]
evenFibonacci = []
x=0
def fibbonacci(x):
    while fibonacci[-1] <= 4000000:
        fibonacci.append(fibonacci[x]+fibonacci[x+1])
        x = x+1
fibbonacci(x)
fibonacci.pop(-1)
print(fibonacci)
def evenodd():
    for i in fibonacci:
        if i % 2 == 0:
            evenFibonacci.append(i)
evenodd()
print(evenFibonacci)
print(sum(evenFibonacci))
