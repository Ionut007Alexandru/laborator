
def interclasare():
    f = open("sirul.in", "r" )
    n = int(f.readline())
    sir1=[]
    sir2=[]
    sir3=[]
    while n:
        sir1.append(f.readline().split())
        n-=1

    m= int(f.readline())

    while m:
        sir2.append(f.readline().split())
        m-=1

    f.close()

    x=len(sir1)+len(sir2)

    a=min(sir1,default=0)
    b=min(sir2,default=0)
    print(a, " ", b)
    a=int()
    b=int()

    if a >= b:
        print("da")
    print(a," ",b)
    """""""""
    while x:
          sir3.append(min(sir1+sir2))
          a=
          
          a=int()
          b=int()
          
              sir1.remove(min(sir1,default=0))
          else:
              sir2.remove(min(sir2,default=0))
          
          x -= 1
    """""

def bbs(l,cnt=0):
    flag=True
    i=0
    while flag:
        flag=False
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                flag=True
                l[i],l[i+1]=l[i+1],l[i]
                cnt+=1
    print(l," ",cnt)


if __name__ == '__main__':
   #interclasare()
    bbs([45,7,90,11,1,100])