import random



def max(l):
    max=0
    for elem in l:
        for el2 in elem:
            if el2>max:
                max=el2
    return max+1

#------
def verif(l):
    n=max(l)
    matr=[]
    for el in range(n):
            r=[]
    for el2 in range(n):
            r.append(0)
            matr.append(r)

    for elem in list:
         x=elem[0]
         y=elem[1]
         matr[x][y]=1
         matr[y][x]=1

def genlist(m):
    l=[]
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j]==1 and i>j:
                l.append([i,j])
    print(l)

def rolldice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    if dice1==dice2:
        return 1
    else:
        return 0

if __name__== '__main__' :
     v=0
     for i in range(100):
         v+=rolldice()
     print(v/100)
