# -*- coding: UTF-8 -*-

'''
Created on 07/04/2011

@author: Rafael Pedretti
'''
import random
from recursos.Observable import Observable

class Grafo(Observable):

    def __init__(self, nome):
        Observable.__init__(self)
        assert nome != None
        self.nome = nome
        self.lista_vertices = []
        self.lista_arestas = []
        self.vertices = {}
        self.arvore = None
        self.conexo = None
        self.regular = None
        self.completo = None
        self.numero_cromatico = None
        
    def obterNome(self):
        '''Retorna o nome do grafo
           Complexidade )(1)
        '''
        return self.nome
    
    def redefinirInferencias(self):
        self.arvore = None
        self.conexo = None
        self.regular = None
        self.completo = None
        self.numero_cromatico = None
        
    def adicionarVertices(self, nomes, dados):
        for i in xrange(len(nomes)):
            self.adicionarVertice(nomes[i], dados[i])
    
    def obterOrdem(self):
        '''Retorna a ordem (inteiro) do grafo
        Complexidade: O(1)
        '''
        return len(self.vertices)
    
    def obterVertices(self):
        '''Retorna os vértices (objetos) do grafo
        Complexidade: O(1)
        '''
        return self.lista_vertices
    
    def obterVertice(self, nomeVertice):
        '''Retorna o vértice (objeto) com nome 'nomeVertice'
        Complexidade: O(1)
        '''
        try:
            return self.vertices[nomeVertice]
        except KeyError as e:
            self._erroChaveNaoExiste(e)
    
    def umVertice(self):
        '''Retorna um vértice (objeto) aleatório do grafo
        Complexidade: O(1)
        '''
        return random.choice(self.lista_vertices)
    
    def ehRegular(self):
        '''Verifica se o grafo é regular
        Complexidade: obterNome() -> O(1)
                      umVertice() -> O(1)
                      Total -> O(n) | n é o número de vértices
        '''
        if self.regular is None:
            vertices = self.obterVertices()
            self.regular = True
            if len(vertices) != 0:
                grau = self.obterGrau(self.umVertice().obterNome())
                for vertice in vertices:
                    if self.obterGrau(vertice.obterNome()) != grau:
                        self.regular = False
                        break
        return self.regular              
        
    def _erroChaveNaoExiste(self, e):
        self.broadcastEvent('VerticeNaoExiste', 'Vertice ' + unicode(e) + " não pertence ao grafo")
        
    def _erroChaveExiste(self, e):
        self.broadcastEvent('VerticeJahExiste'," vertice " + unicode(e) + " já pertence ao grafo")

class GrafoNO(Grafo):
    
    def __init__(self, nome):
        super(GrafoNO, self).__init__(nome)
        self.adjacentes = {}
        
    def ehConexo(self):
        '''Verifica se o grafo é conexo
        Complexidade: obterAdjacentes() -> O(1)
                      obterNome -> O(1)
                      obterVertices() -> O(1)
                      Total -> O(n) | n é o número de vértices
        '''
        if self.conexo is None:
            self.conexo = True
            pilha = []
            marcados = set()
            vertice = self.umVertice()
            marcados.add(vertice)
            pilha.append(vertice)
            while pilha:
                vertice = pilha[-1]
                adjacentes = self.obterAdjacentes(vertice.obterNome())
                for adjacente in adjacentes:
                    if adjacente not in marcados:
                        pilha.append(adjacente)
                        marcados.add(adjacente)

                if set(adjacentes).issubset(marcados):

                    pilha.remove(vertice)
            
            for vertice in self.obterVertices():
                if vertice not in marcados:
                    self.conexo = False

        return self.conexo
    
    def ehCompleto(self):
        '''Verifica se o grafo é copleto
           Complexidade: O(n) | n é o número de vértices
        '''
        if self.completo is None:
            vertices = self.obterVertices()
            if len(vertices) > 1:
                self.completo = True
                ordem = self.obterOrdem()
                for vertice in vertices:
                    if self.obterGrau(vertice.obterNome()) != ordem - 1:
                        self.completo = False
                        break
            else:
                self.completo = False
        return self.completo
    
    def obterGrau(self, nomeVertice):
        '''Retorna o grau do vértice de nome nomeVertice
           Complexidade: O(1)
        '''
        
        return len(self.obterAdjacentes(nomeVertice))
    
    def ehArvore(self):
        '''Verifica se o grafo é uma árvore
        Complexidade: ehConexo() -> O(n) | n é o número de vértices
                      obterVertices() -> O(1)
                      obterAdjacentes() -> O(1)
                      obterNome() -> O(1)
                      Total -> O(n)
        '''     
        if self.arvore is None:
            self.arvore = False
            if self.ehConexo():
                arestas = 0
                vertices = self.obterVertices()
                for vertice in vertices:
                    adjacentes = self.obterAdjacentes(vertice.obterNome())
                    arestas += len(adjacentes)
                arestas = arestas/2
                self.arvore = arestas == len(vertices) - 1
        return self.arvore
    
    def fechoTransitivo(self, vertice, visitados = set()):
        '''Retorna o conjunto do nome dos vértices que pertencem ao fecho 
           transitivo do vértice alvo
           Complexidade: O(m) | m é o número de arestas do grafo (pior caso m = n-1
                              | n é o número de vértices no grafo )
        '''
        fecho = set()
        fecho.add(vertice)
        visitados.add(vertice)
        for adjacente in self.obterAdjacentes(vertice):
            if adjacente.obterNome() not in visitados:
                fecho = fecho.union(self.fechoTransitivo(adjacente.obterNome(),visitados))
        return fecho
      
    def adicionarVertice(self, nome, dados = {}):
        '''Adiciona um vértice no grafo
           Coplexidade: O(1)
        '''
        try:
            self.redefinirInferencias()
            if nome in self.vertices:
                raise KeyError
            vertice = Vertice(nome, dados)
            self.vertices[nome] = vertice
            self.adjacentes[nome] = {}
            self.lista_vertices.append(vertice)
        except KeyError as e:
            self._erroChaveExiste(e)
            
    def removerVertice(self, nomeVertice):
        '''Remove o vértice de nome nomeVertice do grafo e suas arestas
           Complexidade: O(a) | a é o número de adjacentes do vértice alvo (pior caso a = n-1)
                              | n é o número de vértices no grafo 
        '''
        try:
            self.redefinirInferencias()
            for adjacente in self.obterAdjacentes(nomeVertice):
                self.removerAresta(nomeVertice, adjacente.obterNome())
            vertice = self.vertices.pop(nomeVertice)
            self.lista_vertices.remove(vertice)
            return vertice
        except KeyError as e:
            self._erroChaveNaoExiste(e)
         
    def adicionarAresta(self, nomeVertice1, nomeVertice2, dados = {}):
        '''Adiciona uma aresta ligando os vértices de nome: nomeVertice1 e nomeVertice2
           Complexidade: O(1)
        '''
        try:
            self.redefinirInferencias()
            v1 = self.vertices[nomeVertice1]
            v2 = self.vertices[nomeVertice2]
            self.adjacentes[nomeVertice1][v2] = dados
            self.adjacentes[nomeVertice2][v1] = dados
            self.lista_arestas.append((dados,v1,v2))
        except KeyError as e:
            self._erroChaveNaoExiste(e)
        
    def removerAresta(self, nomeVertice1, nomeVertice2):
        '''Remove a aresta que conecta os vertices de nomeVertice1 e nomeVertice2
           Complexidade: O(1)
        '''
        try:
            self.redefinirInferencias()
            v1 = self.vertices[nomeVertice1]
            v2 = self.vertices[nomeVertice2]
            self.adjacentes[nomeVertice1].pop(v2)
            self.adjacentes[nomeVertice2].pop(v1)
        except KeyError as e:
            self._erroChaveNaoExiste(e)
        
    def obterAresta(self, nomeVertice1, nomeVertice2):
        '''Retorna a aresta que conecta os vertices de nomeVertice1 e nomeVertice2
           Complexidade: O(1)
        '''
        vertice2 = self.vertices[nomeVertice2]
        return self.adjacentes[nomeVertice1][vertice2]

    def obterAdjacentes(self, nomeVertice):
        '''Retorna os vértices (objetos) adjacentes ao vértice de nome
           'nomeVertice'
           Complexidade: O(1)
        '''
        try:
            return self.adjacentes[nomeVertice].keys()
        except KeyError as e:
            self._erroChaveNaoExiste(e)
            
    def limpar(self):
        '''remove todas as arestas do grafo
           Complexidade O(n) | n é o número de vértices
        '''
        for vertice in self.lista_vertices:
            self.adjacentes[vertice.obterNome()] = {}
        self.redefinirInferencias()

class Vertice(object):
    
    def __init__(self, identificador, dados = {}):
        assert identificador != None
        self.nome = identificador
        self.dados = dados
        
    def obterNome(self):
        return self.nome
    
    def obterDados(self):
        return self.dados
    
    def obterDado(self, chave):
        return self.dados[chave]
    
    def adicionarDado(self, dados):
        self.dados = dict(self.dados.items() + dados.items())
    
    def removerDado(self, chaveDado):
        return self.dados.pop(chaveDado)