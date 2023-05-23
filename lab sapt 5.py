def minMax(l):
    min=99999
    max=-1
    for i in range(len(l)):
     if l[i]>=max:
         max=l[i]
     if l[i]<=min:
         min=l[i]
    print(min," ",max)

def minsort(l):
    l.sort()
    print(l[0]," ",l[1]," ",l[len(l)-2]," ",l[len(l)-1])

def parcurgere_matrice(matrice):
    n=len(matrice)
    sir='abcd'
    for i in range(n):
        for j in range(n):
            if matrice[i][j]==1:
                print(sir[i],sir[j],end='')
        print("")

def nrap0(n):
    if n==0:
        return 0
    if n%10==0:
        return 1+nrap0(n//10)
    else:
        return nrap0(n//10)


if __name__== '__main__' :
    #minMax([20,40,8,1])
    #minsort([20,40,8,1])
    #parcurgere_matrice([[1,0,1,0],[1,0,1,1],[0,0,1,0],[1,0,0,0]])
    print(nrap0(1301208))
