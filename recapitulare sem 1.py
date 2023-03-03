#1)   sa se def o functie care primeste ca param un nr nat si o
#     lista de nr nat si reintaorce true daca nr nat primit ca
#     param este gasit in lista si false in caz contrar
n=open("fisierr",'r')
l=int(n.readline())

def f1(l,n):
    for i in l:
        l.append(n.readline())
    read()
    for i in l:
        if l[i]==n:
            return True
    return False

#2) def o functie care primeste ca param o matrice de
# nr nat si fct sa intoarca true daca gaseste nr nat
# intre elem matricei si false in caz contrar

def f2(matr,n):
    l=len(matr)
    c=len(matr[0])
    for i in l:
        for j in c:
            if matr[i][j]==n:
                return True
    return False

#3) sa se scrie o functie recursiva care calculeaza factorialul unui nr nat n
 #   sa se scrie o functie recursiva casre primeste ca param un nr nat si calc
 # de cate ori apare cifra 0 in nr respectiv

def f3(n):
    if n==0:
        return 1
    else: return n*f3(n-1)


def f4(n,c=0):
    if n==0:
        return c
    if n%10==0:
        return f4(n//10,c+1)

    else:
        return f4(n//10,c)

def f5(n,s=0):
    if n==0:
        return s
    return f5(n//10,s+n%10)

#4) sa se scrie o functie care implementeaza algoritmul bubble sort pe o lista

def f6(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                aux=l[j]
                l[j]=l[j+1]
                l[j+1]=aux
    print(l)




if __name__ == '__main__':
    #print(f1([1,2,3,4],10))
    #matr=[[1,2,3],[4,5,6],[7,8,9]]
    #print(f2(matr,8))
    #print(f3(5))
    #print(f4(320001))
    #print(f5(1234))
    f6([1,4545,6,787,8])

