#sa se det val minima si max dintr-o matrice de dim m*n
def prob1():
    m=int(input())
    n=int(input())
    matr=[[0]*m for i in range(n)]
    max=int(-1)
    for i in range(n):
        for j in range(m):
            matr[i][j]=int(input())
            if matr[i][j]>=max:
                max=matr[i][j]

    print(max)
#sa se gen valorile unei matrice patratice dupa urmat reguli
#elementele pt care produsul indicilor este un nr par vor avea
#val 1 iar pt elem cu prod indicilor impar iar elem de pe diag principala vor avea valoarea 2

def prob2():
    n=int(input())
    matr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                matr[i][j]=2
            elif (i*j)%2==0:
                matr[i][j]=1
    for i in range(n):
        for j in range(n):
            print(matr[i][j],end='\t')
        print('\n')

def unire():
    rezultat=[]
    i=0
    j=0
    while i<len(lista) and j<len(lista):
        if lista[i]<lista[j]:
            rezultat.append(lista[i])
            i+=1
        else:
            rezultat.append(lista[j])
            j+=1
    return rezultat


def sort():
    if len(lista)<1:
        return lista
    else:
        m=(st+dr)//2
        st=sort(lista[:mij])
        dr=sort(lista[mij:])
        if st!=None and dr!=None:
            return unire(st,dr)


def max_digit_frequency(s):
    digit_freq = {}
    for c in s:
        if c.isdigit():
            if c in digit_freq:
                digit_freq[c] += 1
            else:
                digit_freq[c] = 1
    if digit_freq:
        max_freq = max(digit_freq.values())
        return max_freq
    else:
        return 0

if __name__ == '__main__':
    #prob1()
    #prob2()
    #unire([25,1,60,3,14,9,26,5])
    print(max_digit_frequency("1 apare de 9 dar 9 apare de 111 apare de 9 ori"))
