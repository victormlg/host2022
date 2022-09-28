import math
kø = []

def insert(A, x) :
    A.append(x)
    i = A.index(x)

    while 0 < i and A[i] < A[parent_of(i)] :
        A[i], A[parent_of(i)] = A[parent_of(i)], A[i]
        i = parent_of(i)

def parent_of(i) :
    return math.floor((i-1)/2)

def left_of(i) :
    return 2*i +1

def right_of(i) :
    return 2*i +2

def remove_min(A) :
    i=0
    x = A[i]
    n = len(A)
    A[i] = A.pop()
    while right_of(i) < n-1 :
        if A[left_of(i)] <= A[right_of(i)] :
            j = left_of(i)
        else :
            j = right_of(i)

        if A[j] <= A[i] :
            A[i], A[j] = A[j], A[i]
            i = j
        else :
            break
    if left_of(i) < n-1 and A[left_of(i)] <= A[i] :
        A[i], A[left_of(i)] = A[left_of(i)], A[i]
    return x



class prioritetskoe :

    kø = []

    def insert(self, x) :
        A = self.kø
        A.append(x)
        i = A.index(x)

        while 0 < i and A[i] < A[parent_of(i)] :
            A[i], A[parent_of(i)] = A[parent_of(i)], A[i]
            i = parent_of(i)

    def parent_of(self, i) :
        return math.floor((i-1)/2)

    def left_of(self, i) :
        return 2*i +1

    def right_of(self, i) :
        return 2*i +2
    
    def remove_min(self) :
        A = self.kø
        i=0
        x = A[i]
        n = len(A)
        A[i] = A[:-1]
        while right_of(i) < n-1 :
            if A[left_of(i)] <= A[right_of(i)] :
                j = left_of(i)
            else :
                j = right_of(i)

            if A[j] <= A[i] :
                A[i], A[j] = A[j], A[i]
                i = j
            else :
                break
        if left_of(i) < n-1 and A[left_of(i)] <= A[i] :
            A[i], A[left_of(i)] = A[left_of(i)], A[i]
        return x
    
    def print(self) :
        print(self.kø)


class Huffman :

    class Node :
        def __init__(self, s, f, h, v) :
            self._element = s
            self._freq = f 
            self._hoeyre = h 
            self._venstre = v

        def __lt__(self, other) :
            return self._freq < other._freq

        def __le__(self, other) :
            return self._freq <= other._freq

        def __gt__(self, other) :
            return self._freq > other._freq

        def __ge__(self, other) :
            return self._freq >= other._freq

    def __init__(self, C) :
        Q = prioritetskoe()
        for s in C :
            f = C[s]
            Q.insert(self.Node(s, f, None, None))
        while len(Q.kø) > 1 :
            v_1 = Q.remove_min()
            v_2 = Q.remove_min()
            f = v_1._freq + v_2._freq
            Q.insert(self.Node(None, f, v_1, v_2))
        return Q.remove_min()

ordbok = {" ": 9, "a": 5, "b":1, "d":3, "e":7, "f":3, "h":1, "i":1, "k":1, "n":4, "o":1, "r":5, "s":1, "t":2, "u":1, "v":1}
h = Huffman(ordbok)