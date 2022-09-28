class Set :

    def __init__(self) :
        self._mengde = []

    def contains(self, x) : # O(n)
        for i in self._mengde :
            if (i == x) :
                return True
        return False

    def insert(self, x) : #O(n)
        if (not self.contains(x)) :
            self._mengde.append(x)

    def remove(self, x) : #O(n)
        self._mengde.remove(x) #remove tar allerede O(n) tid i python

    def size(self) : #O(n)
        teller = 0
        for i in self._mengde :
            teller+=1
        return teller
        

def skrivTilFil(set, filnavn) :
    fil_in = open(filnavn, "r")
    fil_out = open("output.txt","w")
    for i in fil_in :
        linje = i.split()
        if linje[0] == "insert" :
            set.insert(linje[1])
        elif linje[0] == "contains" :
            fil_out.write(str(set.contains(linje[1]))+"\n")
        elif linje[0] == "remove" :
            set.remove(linje[1])
        elif linje[0] == "size" :
            fil_out.write(str(set.size())+"\n")


skrivTilFil(Set(), "input/example")