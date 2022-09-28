import sys

class Node : 

    def __init__(self, e) :
        self.element = e
        self.children = []
        self.parent = None

    def set_children(self, l) :
        for i in l :
            n = Node(int(i))
            n.parent = self
            self.children.append(n)

def find(v, x) :
    if v.element == x :
        return parent_list(v, [])
    for i in v.children :
        n = find(i, x)
        if n != None :
            return n

def parent_list(v, l) :
    l.append(v.element)
    if v.parent == None :
        return l
    return parent_list(v.parent, l)

def combine(l, rot) :
    if not rot.children :
        return 
    for i in l :
        for c in rot.children :
            if i.element == c.element :
                rot.children.remove(c)
                rot.children.append(i)
                i.parent = rot
    for k in rot.children :
        combine(l, k)   
    return l[0]


rot_liste = []
t = 0
for i in sys.stdin :
    if t == 0 :
        kattunge = int(i.strip())
    elif i.strip() != "-1" :
        linje = i.split()
        rot = Node(int(linje[0]))
        rot.set_children(linje[1:])
        rot_liste.append(rot)
    t+=1


rotnode = combine(rot_liste, rot_liste[0])
for i in find(rotnode, kattunge) :
    print(i, end=" ")
print()