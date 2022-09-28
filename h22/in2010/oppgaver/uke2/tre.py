class Tre :

    class Node :
        barn = []

        def __init__(self, element) :
            self.element = element

        def sett_neste(self, node) :
            self.barn.append(node)

        def slett(self, element) :
            for i in self.barn :
                if i.element == element :
                    self.barn.remove(i)
                    return
        
    
    def insert(self) :
        #insert på en viss posisjon dybde;høyde
        pass

    def remove(self) :
        pass

    def dybde(self) :
        pass

    def hoeyde(self) :
        pass
    

