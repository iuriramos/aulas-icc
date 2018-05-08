def mdc(N, M):
    # iterativa - N > M
    # N >= M
    if N < M:
        N, M = M, N
        
    while M != 0:
        N, M = M, N % M
    return N

def mdc2(N, M):
    if N < M:
        return mdc2(M, N)
    # caso base
    if M == 0:
        return N
    # recursão
    else:
        return mdc2(M, N%M)
    
N = int(input())
M = int(input())
print(mdc2(N, M))
