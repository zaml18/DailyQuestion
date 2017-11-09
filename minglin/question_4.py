def fibo(n):
    if n <=1:
        return n
    else:
        result = fibo(n-1) + fibo(n-2)
        return result

try:
    fibo_numbers = raw_input("please input the number:")
except IndentationError,e:
    print e

for i in range(int(fibo_numbers)):
    print fibo(i),