import math
from multiprocessing import heap
#bubble sort
def bubble_sort(A) :
    n = len(A)
    for i in range(n-2) :
        for j in range(n-i-2) :
            if A[j] > A[j+1] :
                A[j], A[j+1] = A[j+1], A[j]

#selection sort
def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        k = i
        for j in range(i+1, n-1) :
            if A[j] < A[k] :
                k = j 
        if i != k :
            A[i], A[k] = A[k], A[i]

#insertion sort
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n-1) :
        j = i 
        while j < 0 and A[j-1] > A[j] :
            A[j-1], A[j] = A[j], A[j-1] 
            j -= 1


#heap sort
def bubble_down(A, i, n) :
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and A[largest] < A[left] :
        largest, left = left, largest 
    
    if right < n and A[largest] < A[right] :
        largest, right = right, largest 
    
    if i != largest :
        A[i], A[largest] = A[largest], A[i]
        bubble_down(A, largest, n)

def build_max_heap(A, n) :
    for i in range(int(math.floor(n/2)), -1, -1) :
        bubble_down(A, i, n)

def heap_sort(A) :
    n = len(A)
    build_max_heap(A, n)
    for i in range(n-1, -1, -1) :
        A[0], A[i] = A[i], A[0]
        bubble_down(A, 0, i)

