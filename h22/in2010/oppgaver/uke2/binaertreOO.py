class binaertre :

    root = None

    class node :
        left = None
        right = None 
        element = 0
    
    def insert(self, v, x) :

        if v == None :
           v = self.node()
           v.element = x
        elif x < v.element :
            v.left = self.insert(v.left,x)
        elif x > v.element :
            v.right = self.insert(v.right, x)
        return v

    def node_insert(self, x) :
        if (self.root == None ) :
            self.root = self.insert(None, x)
        else :
            self.insert(self.root, x)

    def search(self, v, x) :
        if v == None :
            return None
        if v.element == x :
            return v
        if x > v.element :
            return self.search(v.right, x)
        if x < v.element :
            return self.search(v.left, x)

    def er_med(self, x) :
        return not self.search(self.root, x) == None

    def remove(self) :
        pass

tre = binaertre()

tre.node_insert(10)
tre.node_insert(11)
tre.node_insert(10)

print(tre.er_med(11))