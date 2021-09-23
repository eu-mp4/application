class Vertice:
	def __init__ (self, key, payload):
	    self.key = int(key)
	    self.payload = payload
	    self.pai = None
	    self.left = None
	    self.right = None
					
	def __str__(self):
	    return str(self.key) + " " + str(self.payload)

class Tree:
    def __init__(self):
        self.raiz = None
        self.count = 0

    def TreeInsert(self, z):
        y = None
        x = self.raiz
        while (x != None):
            y = x
            if (z.key < x.key):
                x = x.left
            else:
                x = x.right
        z.pai = y
        if (y == None):
            self.raiz = z
        elif (z.key < y.key):
            y.left = z
        else:
            y.right = z
        
        self.count += 1

    def InteractiveTreeSearch(self, key):
        if (self.raiz == None):
            return None
        vertice = self.raiz
        while (vertice != None and int(key) != vertice.key):
            if (int(key) < vertice.key):
                vertice = vertice.left
            else:
                vertice = vertice.right
        return vertice

    def InOrderTreeWalk(self, vertice = None):
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        if (vertice.left != None):
            self.InOrderTreeWalk(vertice = vertice.left)
        print(vertice)
        if (vertice.right != None):
            self.InOrderTreeWalk(vertice = vertice.right)

    def PreOrderTreeWalk(self, vertice = None):                     #CORRIGIDO
        if (self.raiz == None):
            return
        if (vertice == None):
            vertice = self.raiz
        print(vertice)
        if (vertice.left != None):
            self.PreOrderTreeWalk(vertice = vertice.left)
        if (vertice.right != None):
            self.PreOrderTreeWalk(vertice = vertice.right)


    def PosOrderTreeWalk(self, vertice = None):                     #CORRIGIDO
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        if (vertice.left != None):
            self.PosOrderTreeWalk(vertice = vertice.left)
        if (vertice.right != None):
            self.PosOrderTreeWalk(vertice = vertice.right)
        print(vertice)

    def PrintDecrescente(self, vertice = None):                     #CORRIGIDO
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        if (vertice.right != None):
            self.PrintDecrescente(vertice = vertice.right)
        print(vertice)
        if (vertice.left != None):
            self.PrintDecrescente(vertice = vertice.left)

    def TreeMinimum(self, vertice = None):
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        while (vertice.left != None):
            vertice = vertice.left
        return vertice

    def TreeMinimumRecursive(self, vertice = None):                 #CORRIGIDO
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        if (vertice.left != None):
            vertice = self.TreeMinimumRecursive(vertice = vertice.left)
        return vertice

    def TreeMaximum(self, vertice = None):                          #CORRIGIDO
        if (self.raiz == None):
            return None
        if (vertice == None):
            vertice = self.raiz
        while (vertice.right != None):
            vertice = vertice.right
        return vertice
    
    def TreeSucessor(self, vertice = None):
        if (vertice.right != None):
            return self.TreeMinimum(vertice = vertice.right)
        y = vertice.pai
        while (y != None and vertice == y.right):
            vertice = y
            y = vertice.pai
        return y

    def TreePredecessor(self, vertice = None):                             #CORRIGIDO
        if (vertice.left != None):
            return self.TreeMaximum(vertice = vertice.left)
        y = vertice.pai
        while (y != None and vertice == y.left):
            vertice = y
            y = vertice.pai
        return y

    def TreeTransplant(self, u, v):
        if (u.pai == None):
            self.raiz = v
        elif (u.pai.left == u):
            u.pai.left = v
        else:
            u.pai.right = v
        
        if (v != None):
            v.pai = u.pai

    def TreeRemove(self, z):
        if (z.left == None):
            self.TreeTransplant(z, z.right)
        elif (z.right == None):
            self.TreeTransplant(z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            if (y.pai != z):
                self.TreeTransplant(y, y.right)
                y.right = z.right
                y.right.pai = y
            self.TreeTransplant(z, y)
            y.left = z.left
            y.left.pai = y

    def TreeRemoveMaximum(self, z):                                 #CORRIGIDO
        if (z.right == None):
            self.TreeTransplant(z, z.left)
        elif (z.left == None):
            self.TreeTransplant(z, z.right)
        else:
            y = self.TreeMaximum(z.left)
            if (y.pai != z):
                self.TreeTransplant(y, y.left)
                y.left = z.left
                y.left.pai = y
            self.TreeTransplant(z, y)
            y.right = z.right
            y.right.pai = y


def menu():
    print('''ESCOLHA OPÇÃO:
    0 -     SAIR DO PROGRAMA
    1 -     INSERIR
    2 -     BUSCAR
    3 -     PRINT IN-ORDER
    4 -     PRINT PRE-ORDER
    5 -     PRINT POS-ORDER
    6 -     PRINT DECRESCENTE
    7 -     TREE MINIMUM
    8 -     TREE MINIMUM RECURSIVO
    9 -     TREE MAXIMUM 
    10 -    TREE SUCESSOR
    11 -    TREE PREDECESSOR
    12 -    TREE TRANSPLANTE
    13 -    TREE REMOVE
    14 -    TREE REMOVE COM TREE MAXIMUM
    ''')
    return int(input())

def AddVertice(arvore):
    print('INFORME O PAR CHAVE-VALOR:', end='')
    texto = input()
    key, payload = texto.split()
    vertice = Vertice(key, payload)
    arvore.TreeInsert(vertice)

def BuscarChave(arvore):
    chave = int(input('INFORME A CHAVE: '))
    vertice = arvore.InteractiveTreeSearch(chave)
    if (vertice == None):
        print('CHAVE NÃO EXISTE')
    else:
        print('A CHAVE FOI ENCONTRADA: ', chave)

def Tree_Sucessor(arvore):
    chave = int(input('INFORME A CHAVE: '))
    vertice = arvore.InteractiveTreeSearch(chave)
    if (vertice == None):
        print('CHAVE', chave, 'NÃO ENCONTRADA')
    else:
        print('SUCESSOR DA CHAVE É: ', arvore.TreeSucessor(vertice))

def Tree_Predecessor(arvore):
    chave = int(input('INFORME A CHAVE: '))
    vertice = arvore.InteractiveTreeSearch(chave)
    if (vertice == None):
        print('CHAVE ', chave, 'NÃO ENCONTRADA')
    else:
        print('PREDECESSOR DA CHAVE É', arvore.TreePredecessor(vertice))

def RemoverVertice(arvore):
    chave = int(input('INFORME A CHAVE: '))
    vertice = arvore.InteractiveTreeSearch(chave)
    if (vertice == None):
        print('VERTICE DE CHAVE ', chave, 'NÃO EXISTE')
    else:
        arvore.TreeRemove(vertice)
        print('VERTICE REMOVIDO')

def RemoverVerticeMaximum(arvore):
    chave = int(input('INFORME A CHAVE: '))
    vertice = arvore.InteractiveTreeSearch(chave)
    if (vertice == None):
        print('CHAVE', chave, 'NÃO ENCONTRADA')
    else:
        print('VERTICE REMOVIDO. RESULTADO DA ÁRVORE: ', arvore.TreeRemoveMaximum(vertice))

def Transplantar(arvore):
    u = int(input('INFORME A CHAVE: '))
    vertice = arvore.InteractiveTreeSearch(u)
    arvore.TreeRemove(vertice)
    v = int(input('INFORME A CHAVE A SER TRANSPLANTADA: '))
    print('VERTICE TRANSPLANTADO. RESULTADO DA ÁRVORE: ', arvore.TreeTransplant(u, v))

def main():
    arvore = Tree()
    opcao = menu()
    while (opcao != 0):

        if (opcao == 1):
            AddVertice(arvore)
        elif (opcao == 2):
            BuscarChave(arvore)
        elif (opcao == 3):
            arvore.InOrderTreeWalk()
        elif (opcao == 4):
            arvore.PreOrderTreeWalk()
        elif (opcao == 5):
            arvore.PosOrderTreeWalk()
        elif (opcao == 6):
            arvore.PrintDecrescente()
        elif (opcao == 7):
            print('O menor elemento: ', arvore.TreeMinimum())
        elif (opcao == 8):
            print('O menor[recursivo] elemento: ', arvore.TreeMinimumRecursive())
        elif (opcao == 9):
            print('O maior elemento: ', arvore.TreeMaximum())
        elif (opcao == 10):
            Tree_Sucessor(arvore)
        elif (opcao == 11):
            Tree_Predecessor(arvore)
        elif (opcao == 12):
            Transplantar(arvore)
        elif (opcao == 13):
            RemoverVertice(arvore)
        elif (opcao) == 14:
            RemoverVerticeMaximum(arvore)
        else:
            print('OPÇÃO INVÁLIDA')
        opcao = menu()


if (__name__ == "__main__"):
    main()




