from aula01 import Arvore

arvore = Arvore()
arvore.adicionar_raiz('A')
arvore.adicionar_filho('A','B')
arvore.adicionar_filho('A','C')
arvore.adicionar_filho('A','D')
arvore.adicionar_filho('C','E')
arvore.adicionar_filho('C','F')
arvore.adicionar_filho('F','G')
arvore.imprimir()
arvore.percorrer()