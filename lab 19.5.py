graph=[[0,1],[0,2],[1,2],[1,3],[2,4],[2,6],[4,5],[4,8],[5,7]]
adancime=0
inainte=[]
dupa=[]
def parcurgGraf(graph,start,adancime):
       dupa.append(start)
       for el in graph:
         if el[0]==start:
            inainte.append(start)
            parcurgGraf(graph,el[1],adancime+1)

def parcgrafiterativ(graph,start):
    cale=[]
    nod=start
    cale.append(nod)
    for elem in graph:
        if elem[0]==nod:
            nod=elem[1]
            cale.append(nod)
    return cale

def toatecaile(graph):
    n=len(graph)
    i=0
    while i<n:
        primelem=graph[0][0]
        print(parcgrafiterativ(graph,primelem))
        graph.pop(0)
        i+=1

if __name__ == '__main__':
    #parcurgGraf(graph,0,1)
    #print(inainte)
    #print(dupa)
    #print(parcgrafiterativ(graph,0))
    toatecaile(graph)