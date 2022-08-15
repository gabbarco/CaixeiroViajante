"""
Criação das Classes que vão representar o grafo
"""
class Node:
    vertex = 0
    weight = 0

class Edge:
    index = 0
    nodes = [] 
    
    def __init__(self, index):
        self.index = index
        
class Graph:
    edges = []
    

"""
Criação de um grafo - função que cria um grafo e inicializa os edges
"""
    
def createGraph(v):
    g = Graph()
    for i in range (0,v):
        g.edges.append(Edge(i))
    return g

"""
Cria um nó
"""
def createNode(v, weight):
    n = Node()
    n.vertex = v
    n.weight = weight
    return n

"""
Cria uma nova aresta
"""
def createEdge(g, vi, vf, w):
    if g is None:
        return False
    if vi < 0 or vi >= len(g.edges):
        return False
    if vf < 0 or vf >= len(g.edges):
        return False
    
    newNode = createNode(vf, w)
    if len(g.edges[vi].nodes) == 0 :
        g.edges[vi].nodes = [newNode]
    else:
        g.edges[vi].nodes.append(newNode)
    
"""
Mostra o grafo
"""
def printGraph(g):
    for i in range (0, len(g.edges)):
        print ("v" + str(i), end=" →  ")
        for nodes in g.edges[i].nodes:
            print ("v" + str(nodes.vertex) + "(" + str(nodes.weight) + ")" , end="|")
        print("\n")
        
"""
Valida uma rota
"""
def validarRota(g, rota):
    ## verifica se a rota repete algum valor
    a_set = set(rota)
    contains_duplicates = len(rota) != len(a_set)
    if contains_duplicates == True:

        return False
    
    ## verifica se a rota possui caminhos para percorrer as adjacencias
    for r in range (0,len(rota) -1):
        vi = rota[r]
        vf = rota[r + 1]
        checked = False
        for n in g.edges[vi].nodes:
            if n.vertex == vf:
                checked = True
        if checked == False:
            return False
    return True
                 
"""
Soma pesos
"""
def somaPesos(g, rota):
    ## Soma os pesos da rota
    soma = 0
    for r in range (0,len(rota) -1):
        vi = rota[r]
        vf = rota[r + 1]
        checked = False
        for n in g.edges[vi].nodes:
             if n.vertex == vf:
                soma += n.weight
                checked = True
        if checked == False:
            return False
    return soma

"""
Resolução de força bruta
"""
def resolverComForcaBruta():
    for a in range(0,1):
        for b in range(0,6):
            for c in range(0,6):
                for d in range(0,6):
                  for e in range(0,6):
                    for f in range(0,6):
                          rota = [a,b,c,d,e,f]
                          if(validarRota(g,rota) ==True):
                              print("------------")
                              print(rota)
                              print(validarRota(g, rota))                
                              print(somaPesos(g,rota))
                              print("------------")

"""
Resolução da menor rota possível
"""
def  MenorRota():
    i=0
    rotamin=0
    rotamin1=1000000
    shi = []
    sha = []
    numvet=0
    z=0
    for a in range(0,1):
        for b in range(0,6):
            for c in range(0,6):
                for d in range(0,6):
                  for e in range(0,6):
                    for f in range(0,6):
                          rota = [a,b,c,d,e,f]
                          if(validarRota(g,rota) ==True):  
                              for i in range(0,i+1):
                                shi.append(somaPesos(g,rota))
                                sha.append(rota)
    rotamin1=shi[z+1]                            
    for i in range(0,len(shi)-1):
      rotamin=shi[z]
      if rotamin<rotamin1:
        rotamin1=rotamin
        numvet=z
      z=z+1
    print("A menor rota possível é",sha[numvet])
    print("com uma distância de",rotamin1)
    print("\n")
                                
                                


g = createGraph(6)
createEdge(g, 0,1,60)
createEdge(g, 0,3,120)
createEdge(g, 0,4,50)
createEdge(g, 0,5,60)
createEdge(g, 1,0,60)
createEdge(g, 1,2,50)
createEdge(g, 1,4,100)
createEdge(g, 1,5,25)
createEdge(g, 2,1,50)
createEdge(g, 2,3,70)
createEdge(g, 2,4,100)
createEdge(g, 2,5,25)
createEdge(g, 3,0,120)
createEdge(g, 3,2,70)
createEdge(g, 3,5,75)
createEdge(g, 3,4,80)
createEdge(g, 4,1,100)
createEdge(g, 4,2,100)
createEdge(g, 4,3,80)
createEdge(g, 4,0,50)
createEdge(g, 4,5,75)
createEdge(g, 5,0,60)
createEdge(g, 5,1,25)
createEdge(g, 5,2,25)
createEdge(g, 5,3,75)
createEdge(g, 5,4,75)


MenorRota() #Inserir aqui a função desejada
printGraph(g)