

#pt fiecare litera se atribuie o valoare a-100, b-1 .... z-2000
#doresc sa calculez sumavalorilor generate de literele unui cuvant adica daca cuvantul e az- 2100

def hash1(x):
    h1={'a':100,'b':1,'c':200,'d':3,'e':4,'f':5,'g':300,
        'h':23,'i':25,'j':7,'k':45,'l':50,'m':120,'n':45,'o':56,'p':45,
        'q':10,'r':34,'s':56,'t':28,'u':16,'v':19,'w':21,'x':22,'y':23,'z':2000}

    s=0
    for i in x:
        s+=h1[i]
    return s

#de preluat de a tastatura sau de creeat o lista manuala cu nume de persoane [ion,maria,bogdan]
# si de gasit numele cu cea mai mare valoare


def nume(lista):
    s=0
    smax=' '
    for i in lista:
        val_curenta=hash1(i)
        if val_curenta>s:
            s=val_curenta
            smax=i
    print(smax)



def generare_ht(tip=0):
    ht={}
    litere=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    listanoua=[]
    start=7
    for i in range (start,len(litere)):
        listanoua.append(litere[i])
    for i in range(0,start):
        listanoua.append(litere[i])
    for i in range(len(litere)):
        if tip == 0:
            ht[litere[i]]=listanoua[i]
        else:
            ht[listanoua[i]]=litere[i]
    return ht

def crypt_text(propozitie,tip=0):
    rezultat=''
    dict_crypt=generare_ht(tip)
    for i in propozitie:
        if i in (' ','-','8','9',':'):
            rezultat+=i
        else:
            rezultat+=dict_crypt[i]
    return rezultat


if __name__ == '__main__':
    #print(hash1())
    nume(['ion','maria','simona','aurel'])
    print(generare_ht())
    #prop=input()
    #c=crypt_text(prop)
    #print(c)
    #d=crypt_text(c,444)
    #print(d)