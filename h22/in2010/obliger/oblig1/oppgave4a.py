import math
import sys

def balansert_input(l1, l2) :
    n = len(l1)

    if n == 1 : 
        l2.append(l1[0])
        return l2

    mid = int(math.floor(n/2))

    l2.append(l1[mid])
    if n > 2 :
        balansert_input(l1[mid+1:], l2)
    balansert_input(l1[:mid], l2)

    return l2


input = []
output = []

for i in sys.stdin:
    line = i.split()
    input.append(int(line[0]))

kul_liste = balansert_input(input, output)
for i in kul_liste:
    print(f"{i}")