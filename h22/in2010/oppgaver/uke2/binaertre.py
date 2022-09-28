class Binaersoeketre :

    right = None
    left = None
    element = 0

def insert(v, x) :

    if v == None :
        v = Binaersoeketre()
        v.element = x
    elif x < v.element :
        v.left = insert(v.left,x)
    elif x > v.element :
        v.right = insert(v.right, x)
    return v

def search(v, x) :
    if v == None :
        return None
    if v.element == x :
        return v
    if x > v.element :
        return search(v.right, x)
    if x < v.element :
        return search(v.left, x)

def height(v) :
    h = -1

    if v == None :
        return h
    for w in (v.left, v.right) :
        h = max(h, height(w))
    return 1+ h

def minimum(v) :
    if v.left == None :
        return v
    return minimum(v.left)

def remove(v, x) :
    if v == None :
        return None
    if x > v.element :
        v.right = remove(v.right, x)
        return v
    if x < v.element :
        v.left = remove(v.left, x)
        return v
    if v.left == None :
        return v.right
    if v.right == None :
        return v.left
    u = minimum(v.right)
    v.element = u.element
    v.right = remove(v.right, u.element)
    return v

node = insert(None, 20)
insert(node, 10)
insert(node, 5)
#insert(node, 35)
insert(node, 2)


print(search(node, 10).element)
print(remove(node, 10).element)
print(search(node, 10))
print(search(node, 5).element)

#print(height(node))

#print(minimum(node).element)


