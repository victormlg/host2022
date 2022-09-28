import math 
import heapq
import sys

def print_heapbalansert_input(h) :
    n = len(h)

    if n == 1 :
        print(heapq.heappop(h))
        return

    mid = int(math.floor(n/2))
    pop = -1
    newh = []
    while pop < mid-1 :
        pop = heapq.heappop(h) 
        heapq.heappush(newh, pop)
    print(heapq.heappop(h))

    print_heapbalansert_input(newh)
    if h :
        print_heapbalansert_input(h)

A=[]
for line in sys.stdin :
    A.append(int(line.split()[0]))

print_heapbalansert_input(A)