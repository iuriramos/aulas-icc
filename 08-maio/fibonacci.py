'''
N = 1 >> 1
N = 2 >> 1
N = 3 >> 2 = 1 + 1
N = 4 >> 3 = 1 + 2
N = 5 >> 5 = 2 + 3

'''
def fibonacci(N):
    # caso base
    if N == 1 or N == 2:
        return 1
    # recursão
    return fibonacci(N-1) + fibonacci(N-2)
     
     
def fibo(N):
    if N == 0 or N == 1:
        return 1
    # N > 1 - 2, 3, 4, ...
    a = 1
    b = 1
    for _ in range(N-1): # N = 2
        a, b = b, a+b # a, b = 1, 1+1 >> b=2
    return b
        
        
     
N = int(input())
print(fibo(N))

        
        
        
        
