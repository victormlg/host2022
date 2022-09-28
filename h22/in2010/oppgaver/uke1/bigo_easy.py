def sum_three_elements(array): # O(1)
    return array[0] + array[1] + array[2]


def string_contains_space(input_string): #O(n)
    for char in input_string:
        if char == ' ':
            return True
    return False


def print_number_many_times(n): # O(n)
    for _ in range(20):
        print(n)


def contains_duplicate(array): #O(n^2)
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return True
    return False


def contains_duplicate_smarter(array): #O(n^2)
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True
    return False


def multiply_by_two(n): #O(log(n))
    current = 1
    while current <= n:
        print(current)
        current = current * 2


def sums_multiplied(array1, array2): #O(n)
    sum1, sum2 = 0, 0

    for element in array1:
        sum1 += element

    for element in array2:
        sum2 += element

    return sum1*sum2


def sums_multiplied_k_times(array1, array2, k): #O(n)
    sum = 0
    for _ in range(k):
        sum += sums_multiplied(array1, array2)


# Se her: https://wiki.python.org/moin/TimeComplexity
def get_array_sorted(array): #O(nlog(n))
    return sorted(array)