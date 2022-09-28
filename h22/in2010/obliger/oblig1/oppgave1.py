import sys

class Set :

    class Node :
        left = None
        right = None
        element = None

    root = None
    _size = 0

    def _insert(self, v, x) :
        if v == None :
            v = self.Node()
            v.size = 1
            v.element = x
            self._size +=1
        if x < v.element :
            v.left = self._insert(v.left,x)
        elif x > v.element :
            v.right = self._insert(v.right, x)
        return v
    
    def insert(self, x) :
        self.root = self._insert(self.root, x)
        return self.root
        
    def _remove(self, v, x) :
        if v == None :
            return None
        if x > v.element :
            v.right = self._remove(v.right, x)
            return v
        if x < v.element :
            v.left = self._remove(v.left, x)
            return v
        if v.left == None :
            self._size -=1
            return v.right
        if v.right == None :
            self._size -=1
            return v.left
        u = self._minimum(v.right)
        v.element = u.element
        v.right = self._remove(v.right, u.element)
        return v

    def remove(self, x) :
        self.root =  self._remove(self.root, x)
        return self.root

    def _minimum(self, v) :
        if v.left == None :
            return v
        return self._minimum(v.left)

    def _contains(self, v, x) :
        if v == None :
            return None 
        if v.element == x :
            return v
        if x > v.element :
            return self._contains(v.right, x)
        if x < v.element :
            return self._contains(v.left, x)
        
    def contains(self, x) :
        return not self._contains(self.root, x) == None

    def size(self) :
        return self._size

set = Set()
for i in sys.stdin :
    linje = i.split()
    if linje[0] == "insert" :
        set.insert(int(linje[1]))
    elif linje[0] == "contains" :
        print(str(set.contains(int(linje[1]))).lower())
    elif linje[0] == "remove" :
        set.remove(int(linje[1]))
    elif linje[0] == "size" :
        print(str(set.size()))