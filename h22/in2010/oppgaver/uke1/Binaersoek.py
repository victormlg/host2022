import math

def Søk(array, x) : #O(1)
    for i in array :
        if (i == x) :
            return True
    return False

def BinærSøk(A, x) : #O(log2(n))
    high = len(A)-1 
    low = 0
    while (low <= high) :
        indeks = math.ceil((low+high)/2) 
        if (A[indeks] == x) :
            return True
        elif (A[indeks] < x) :
            low = indeks +1
        elif (A[indeks] > x) :
            high = indeks -1
    return False


def RekursivtSøk(high, low, A, x) : #O(log2(n))

    if (low > high) :
        return False
    inx = math.ceil((low+high)/2)
    if (A[inx]==x) :
        return True

    if (A[inx] < x) :
        return RekursivtSøk(high, inx+1, A, x)
    if (A[inx] > x) :
        return RekursivtSøk(inx-1, low, A, x)

array = [1,2,3,5,6,7,567,789]

print(BinærSøk(array, 8))
print(RekursivtSøk(len(array)-1, 0, array, 567))