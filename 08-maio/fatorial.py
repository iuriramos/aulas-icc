def fatorial(N):
    # caso base
    if N == 0:
        return 1
    else: # recursão
        return N*fatorial(N-1)

def fatorial2(N):
    fat = 1
    for i in range(1, N+1):
        fat *= i
    return fat

print('fatorial(1)=', fatorial(1))
print('fatorial(2)=', fatorial(2))        
print('fatorial(5)=', fatorial(5))

N = int(input())
print(fatorial2(N))
