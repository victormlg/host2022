class Set :

    right = None
    left = None
    element = 0

count = 0

def insert(v, x, count) :

    if v == None :
        v = Set()
        v.element = x
        count +=1
    elif x < v.element :
        v.left, count = insert(v.left,x, count)
    elif x > v.element :
        v.right, count = insert(v.right, x, count)
    return v, count

def contains(v, x) :
    if v == None :
        return None
    if v.element == x :
        return v
    if x > v.element :
        return contains(v.right, x)
    if x < v.element :
        return contains(v.left, x)

def minimum(v) :
    if v.left == None :
        return v
    return minimum(v.left)

def remove(v, x, count) :
    if v == None :
        return None, count
    if x > v.element :
        v.right, count = remove(v.right, x, count)
        return v, count
    if x < v.element :
        v.left, count = remove(v.left, x, count)
        return v, count
    if v.left == None :
        count -=1
        return v.right, count
    if v.right == None :
        count -=1
        return v.left, count
    u = minimum(v.right)
    v.element = u.element
    v.right, count = remove(v.right, u.element)
    return v, count

set, count = insert(None, 10, count)

print(count)

count = insert(set, 13, count)[1]
count = insert(set, 3, count)[1]

count = remove(set, 13, count)[1]

print(count)