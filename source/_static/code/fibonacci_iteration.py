
fib_suite = []
n = 0
while n < 10:
    if n == 0:
        fib_suite.append(0)
    elif n == 1:
        fib_suite.append(1)
    else: 
        res = fib_suite[n-1] + fib_suite[n-2] 
        fib_suite.append(res)
    n += 1
print ', '.join([str(i) for i in fib_suite])