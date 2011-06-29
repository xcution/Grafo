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
        return self._buscaProfundidade(nomeInicial, nomeFinal, pilha, caminhos)
    
    def _buscaProfundidade(self, nomeInicial, nomeFinal, pilha, caminhos):
        '''Executa uma busca em profundidade e retorna Todos os caminhos
           que levam do vértice 'nomeInicial' ao vértice 'nomeFinal'
           Complexidade: ehArvore -> O(n)
                         obterAdjacentes() -> O(1)
                         Total -> O(n)
                         
        '''
        try:
            arvore = self.ehArvore()
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
                            caminhos = self._buscaProfundidade(vertice.obterNome(), nomeFinal, pilha, caminhos)
                
                pilha.pop()
                return caminhos
        except KeyError as e:
            self._erroChaveNaoExiste(e)
            
# Ainda em produção - Juarez
    def colorirVertices(self):
        ''' Algoritmo de coloração de Vertice
            TODO Testar se há laços
            TODO algoritmo
        '''
#        cor = 0;
#       if not self._temLacos(self):
#          lista_ordenada = self._ordenarGrauNaoCrescente(self.lista_vertices);
#         for vertice in lista_ordenada:
#            while()
        for vertice in self.obterVertices():
            vertice.definirDados('azul', 2)