# -*- coding: UTF-8 -*-

'''
Created on 24/06/2011

@author: Juarez Sacenti
'''
from nucleo.grafo import GrafoNO

class AlgoritmosGrafoNO(GrafoNO):
    
    def __init__(self, nome):
        super(AlgoritmosGrafoNO, self).__init__(nome)
    
    def buscaProfundidade(self, nomeInicial, nomeFinal):
        '''Delegação para o método _buscaProfundidade()
        '''
        pilha = []
        caminhos = []
        arvore = self.ehArvore()
        return self._buscaProfundidade(nomeInicial, nomeFinal, pilha, caminhos, arvore)
    
    def _buscaProfundidade(self, nomeInicial, nomeFinal, pilha, caminhos,arvore):
        '''Executa uma busca em profundidade e retorna Todos os caminhos
           que levam do vértice 'nomeInicial' ao vértice 'nomeFinal'
           Complexidade: obterAdjacentes() -> O(1)
                         Total -> O(n)
                         
        '''
        try:
            inicial = self.vertices[nomeInicial]
            final = self.vertices[nomeFinal]
            pilha.append(inicial)
            if inicial == final:
                pilhaC = list(pilha)
                caminhos.append(pilhaC)
                return caminhos
            else:
                for vertice in self.obterAdjacentes(nomeInicial):
                    if vertice not in pilha:
                        if vertice == final:
                            pilha.append(vertice)
                            pilhaC = list(pilha)
                            caminhos.append(pilhaC)
                            pilha.pop()
                            if arvore:
                                return caminhos
                        else:
                            caminhos = self._buscaProfundidade(vertice.obterNome(), nomeFinal, pilha, caminhos,arvore)
                
                pilha.pop()
                return caminhos
        except KeyError as e:
            self._erroChaveNaoExiste(e)
    
    # TODO precisa lançar exceção se tem laços no grafo?
    def colorirVertices(self):
        ''' Algoritmo de coloração de Vertice
            Testar se há laços
            função Maior_primeiro(G: grafo): Grafo colorido 
                Ordenar os vértices de G em ordem não crescente de grau
                i := 1 
                Enquanto G contém vértices não coloridos 
                    Para Cada vértice v de G não colorido: 
                        Se Nenhum vértice adjacente a v possui a cor i:
                            Atribuir cor i ao vértice v
                    i := i + 1 
                Retornar número cromático
                
            Complexidade: self._ordenarGrauNaoCrescente(): O(nlogn)
                          self._temLacos() : O(n)
                          while(self._temVerticeNaoColorido()): n * ...
                              for vertice in lista_ordenada: ... * n * ...
                                  for adjacente in adjacentes: ... * n * ...
                          vertice.obterDados().has_key('cor'): O(1) 
                          self.obterAdjacentes(vertice.obterNome(): O(1)
                          vertice.obterDados().has_key('cor'): O(1)
                          Total: O(n³)
                          
        '''
        if self.numero_cromatico == None and not self._temLacos():
            lista_ordenada = self._ordenarGrauNaoCrescente(self.lista_vertices)
            cores = ['vermelho', 'verde', 'amarelo', 'azul', 'laranja', 'roxo',
                     'cinza', 'preto', 'branco', 'lilas', 'marrom', 'rosa', 'turquesa']
            i = 0
            while(self._temVerticeNaoColorido()):
                for vertice in lista_ordenada:
                    if(not vertice.obterDados().has_key('cor')):
                        possuiAdjacenteComEstaCor = False
                        for adjacente in self.obterAdjacentes(vertice.obterNome()):
                            if(adjacente.obterDados().has_key('cor')):
                                if(i < 13):
                                    if(adjacente.obterDados()['cor'] == cores[i]):
                                        possuiAdjacenteComEstaCor = True
                                        break
                                else:
                                    if(adjacente.obterDados()['cor'] == i):
                                        possuiAdjacenteComEstaCor = True
                                        break        
                        if(not possuiAdjacenteComEstaCor):
                            if(i < 13):
                                vertice.adicionarDado({'cor': cores[i]})
                            else:
                                vertice.adicionarDado({'cor': i})
                i = i + 1
            self.numero_cromatico = i
        return self.numero_cromatico
    
    def _temLacos(self):
        '''Verifica se o Grafo contém laços
           Complexidade: Percorrer os vértices: O(n) | n é o número de vértices
        '''
        vertices = self.obterVertices()
        for vertice in vertices:
            adjacentes = self.obterAdjacentes(vertice.obterNome())  
            if(vertice in adjacentes):
                return True
        return False
    
    # TODO fazer o reordenamento.
    def _ordenarGrauNaoCrescente(self, lista_vertices):
        '''Ordena por grau em ordem não crescente a lista de vértices
           Complexidade: gerar lista_graus: O(n) | n é o número de vértices
                         ordenar a lista: O(nlogn)
                         retornar a lista ordenada: O(n)
                         Total: O(nlogn)
        '''
        lista_ordenada = []
        lista_graus = [(self.obterGrau(x.obterNome()),x) for x in lista_vertices]
        lista_graus.sort(reverse=True)
        for tupla in lista_graus:
            lista_ordenada.append(tupla[1])
        return lista_ordenada
    
    def _temVerticeNaoColorido(self):
        '''Verifica se o grafo possui vértices não coloridos
           Complexidade: O(n) | n é o número de vértices
        '''
        vertices = self.obterVertices()
        for vertice in vertices:
            if(not vertice.obterDados().has_key('cor')):
                return True
        return False