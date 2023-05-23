
def monede(l1):
    l2=[0]*len(l1)
    change= int(input())
    l1.sort(reverse=True)
    for i in range (len(l1)):
        while change >=l1[i]:
                change=change-l1[i]
                l2[i]=l2[i]+1

    l2.reverse()
    print(l2)

def fibonacci(n):
    l=[0]*n
    l[1]=1
    for i in range(2,n):
        l[i]=l[i-1]+l[i-2]
    print(l)

def fibo(n):
    l=[]
    l.append(0)
    l.append(1)
    i=2
    while(i<=n):
        l.append(l[i-1]+l[i-2])
        i+=1
    print(l)

def f():
    sir=input()
    for i in range(3,len(sir)):
         sir.lower()
    print(sir)

if __name__== '__main__' :
    #print(fibonacci(5))
    #monede([1,2,5,10,20,50,100])
    #fibonacci(5)
    #fibo(5)
    f()