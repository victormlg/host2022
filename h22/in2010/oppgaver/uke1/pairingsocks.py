pile = []
aux_pile = []

n = int(input("n: "))
for i in range(2*n) :
    pile.append(int(input("sock :")))


def Recursive_Pairing_Socks(pile, aux_pile, teller) :
    
    if (not aux_pile and not pile) : #base case
        return print(teller)
    elif (not pile) :
        return print("impossible")

    if (pile[-1:] == aux_pile[-1:]) :
        pile.pop()
        aux_pile.pop()
    else :
        aux_pile.append(pile.pop())
    return Recursive_Pairing_Socks(pile, aux_pile, teller+1)

def Pairing_Socks(pile, aux_pile) :
    teller=0
    while (pile) :
        if (pile[-1:] == aux_pile[-1:]) :
            pile.pop()
            aux_pile.pop()
        else :
            aux_pile.append(pile.pop())
        teller+=1
    if (aux_pile) :
        print("impossible")
    else :
        print(teller)

Pairing_Socks(pile, aux_pile)
Recursive_Pairing_Socks(pile, aux_pile, 0)
