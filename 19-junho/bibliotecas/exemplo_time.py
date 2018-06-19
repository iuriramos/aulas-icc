import time
import math

def funcao():
    math.sin(math.pi/2)
    time.sleep(5)
    
start = time.time()
funcao()
end = time.time()
secs = end-start
print(secs, 'segundos')
