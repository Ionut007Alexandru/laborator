
def cautare(l,x):
    for i in range(len(l)):
        if l[i]==x:
            return i+1
    return -1

def cnp(gen,an,luna,zi,judet,nnn):
    cnp=""
    if gen=="M" or gen =="m" or gen=="masculin":
        if an<2000:
            cnp+="1"
        else:
            cnp+="5"
    else:
        if an<2000:
            cnp+="2"
        else:
            cnp+="6"
    if an<2000:
        an-=1900
    else:
        an-=2000
    if an<10:
        cnp+="0"
    if judet<10:
        cnp+="0"
    cnp+=str(judet)

    cnp+=str(an)
    cnp+=str(luna)
    cnp+=str(zi)
    cnp+=str(judet)
    if nnn<10:
        cnp+="00"
    elif nnn<100:
        cnp+="0"
    else:
        cnp+=""
    cnp+=str(nnn)
    cnp+=str(generareC(cnp))
    return cnp

def generareC(sir):
    sirControl="279146358279"
    suma="0"
    for i in range(len(sir)):
        suma+=int(sir[i])+int(sirControl[i])
    if suma%11==10:
        return 1
    else:
        return suma %11





if __name__== '__main__' :
    #print(cautare([3,5,6,9,10],9))
    cnp("m",1980,1,1,24,1)