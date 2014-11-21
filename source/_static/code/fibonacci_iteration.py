
def fibonacci(n):
    fib_suite = []
    i = 0
    while i <= n:
        if i == 0:
            fib_suite.append(0)
        elif i == 1:
            fib_suite.append(1)
        else: 
            res = fib_suite[i-1] + fib_suite[i-2] 
            fib_suite.append(res)
        i += 1
    return fib_suite

print ', '.join([str(i) for i in fibonacci(10)])


