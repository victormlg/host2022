# Oppgave: Avgjør O-notasjonen på hver prosedyre
# Dere kan bruke amortized kjøretid, så for eksempel hashmap har konstant-tid operasjoner

# Deque er implementert som en dobbelt-lenket lenkeliste
from collections import deque

def fill_stack(n): #O(n)
    stack = []

    for _ in range(n):
        stack.append(n)

    for _ in range(n):
        print(stack.pop())


def fill_queue(n): #O(n(n+1)) = O(n^2)
    queue = []

    for _ in range(n):
        queue.append(n)

    for _ in range(n):
        queue.pop(0)


def fill_deque(n): #O(n)
    dq = deque()
    for i in range(n//2):
        dq.appendleft(i)

    while len(dq) > 0:
        dq.pop()

    for i in range(n//2):
        dq.append(i)

    while len(dq) > 0:
        dq.popleft()


def recursive_split(numbers): #O(n^2)
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]

    mid = (len(numbers) // 2)
    sum += recursive_split(numbers[0:mid])
    sum += recursive_split(numbers[mid+1:])

    return sum


def crazy_loop(n : int): #O(n)
    for i in range(n**2 - (n*n), 0, -1):
        print(i)


# Grafer, alle grafer inneholder V (noder) og E (edges)
# En edge inneholder (vekt, node1, node2)

def pairs(G): #O(n^2)
    V, E = G

    pairs = []
    for i in range(len(V)):
        for j in range(i+1, len(V)):
            pairs.append((V[i], V[j]))
    return pairs


def sum_weights_in_graph(G): #O(n)
    V, E = G

    weight_sum = 0
    for (weight, node1, node2) in E:
        weight_sum += weight

    return weight_sum