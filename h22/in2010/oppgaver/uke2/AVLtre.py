class AVLtre :
    right = None
    left = None
    element = 0
    height = 0
    

def left_rotation(z) :
    y = z.right
    z.right = y.left
    y.left = z

    y.height = 1 + max(height(y.right),height(y.left))
    z.height = 1 + max(height(z.right), height(z.left))

    return y

def right_rotation(x) :
    y = x.left
    x.left = y.right
    y.right = x

    y.height = 1 + max(height(y.right),height(y.left))
    x.height = 1 + max(height(x.right), height(x.left))

    return y

def height(v) :
    h = -1
    if (v == None) :
        return h
    for w in (v.left, v.right) :
        h = max(h, height(w))
    return 1+h

def balance_faktor(v) :
    if v == None :
        return 0
    return height(v.left) - height(v.right)

def balance(v) :
    if balance_faktor(v) < -1 :
        if balance_faktor(v.right) > 0 :
            v.right = right_rotation(v.right)
        return left_rotation(v)
    if balance_faktor(v) > 1 : #height(None) - height(None) = 0
        if balance_faktor(v.left) < 0 :
            v.left = left_rotation(v.left)
        return right_rotation(v)
    return v


def insert(v, x) :

    if v == None :
        v = AVLtre()
        v.element = x
    elif x < v.element :
        v.left = insert(v.left,x)
    elif x > v.element :
        v.right = insert(v.right, x)
    #nytt :
    v.height = 1 + max(height(v.left), height(v.right))
    return balance(v)

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
    #nytt :
    v.height = 1+ max(height(v.left), height(v.right))
    return balance(v)

def minimum(v) :
    if v.left == None :
        return v
    return minimum(v.left)

def search(v, x) :
    if v == None :
        return None
    if v.element == x :
        return v
    if x > v.element :
        return search(v.right, x)
    if x < v.element :
        return search(v.left, x)



tre = insert(None, 19) 
tre = insert(tre, 31) 
tre = insert(tre, 12)
tre = insert(tre, 41)
tre = insert(tre, 8)
tre = insert(tre, 31)

print(tre.element)
print(tre.left.element, tre.right.element)

#8, 12, 19, 31, 38, 41

"""
        19
       /  \
      12   31
     /     / \
    8     38  41
"""