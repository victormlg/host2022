import math
import sys
class Teque :

    def __init__(self) :
        self.A = []

    def push_back(self, x) :
        self.A.append(x)

    def push_front(self, x) :
        k = len(self.A)
        i = 0
        self.A.append(self.A[-1])
        while i < k :
            self.A[k-i] = self.A[k-i-1]
            i+=1
        self.A[0] = x

    def push_middle(self, x) :
        k = len(self.A)
        mid = math.floor((k+1)/2)
        i = 0
        self.A.append(self.A[-1])
        while i < mid :
            self.A[k-i] = self.A[k-i-1] 
            i+=1
        self.A[mid] = x 

    def get(self, i) :
        return self.A[i]
    
teque = Teque()

for i in sys.stdin :
    linje = i.split()
    if linje[0] == "push_back" :
        teque.push_back(int(linje[1]))
    elif linje[0] == "push_front" :
        teque.push_front(int(linje[1]))
    elif linje[0] == "push_middle" :
        teque.push_middle(int(linje[1]))
    elif linje[0] == "get" :
        print(str(teque.get(int(linje[1]))))
