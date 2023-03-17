def masini(l):
    l=sorted(l)
    x=[]
    t_lucru=int(input())
    i=0
    while t_lucru>0 and t_lucru>=l[i]:
        if l[i]<t_lucru:
            t_lucru-=l[i]
            x.append(l[i])
        i+=1
    print(x)

def srec(n):
    if n== 0:
        return 0
    else:
        return srec(n-1)+n

def prob3(l):
        if len(l)==1:
            return l[0]
        else:
            mij=len(l)//2
            return prob3(l[:mij])+prob3(l[mij:])


if __name__ == '__main__':
    #masini([1,5,20,3,300])
    #print(srec(21))
    print(prob3([23,23,1]))
