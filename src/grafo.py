# -*- coding: UTF-8 -*-

'''
Created on 07/04/2011

@author: Rafael Pedretti
'''
import random

class Grafo(object):
    '''
    classdocs
    '''
    def __init__(self):
        self.vertices = {}
        self.arvore = None
        self.conexo = None
        self.regular = None
        self.completo = None
    
    def redefinirInferencias(self):
        self.arvore = None
        self.conexo = None
        self.regular = None
        self.completo = None
        
    def adicionarVertices(self, vertices):
        for vertice in vertices:
            self.adicionarVertice(vertice)
    
    def obterOrdem(self):
        return len(self.vertices)
    
    def obterVertices(self):
        return self.vertices.values()
    
    def umVertice(self):
        return random.choice(self.vertices.values())
    
    def ehRegular(self):
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
            
    def fechoTransitivo(self, vertice):
        pass

        
    def _erroChaveNaoExiste(self, e):
        print ' reimplementar: vertice ' + str(e) + " não pertence ao grafo"
        
    def _erroChaveExiste(self, e):
        print ' reimplementar: vertice ' + str(e) + " já pertence ao grafo"
    
    def _erroTipoVertice(self, e):
        print ' reimplementar: ' + str(e) + ' não é do tipo Vertice'
                        
class GrafoNO(Grafo):
    
    def __init__(self):
        super(GrafoNO, self).__init__()
        self.adjacentes = {}
        
    def ehConexo(self):
        if self.conexo is None:
            arestas = 0
            vertices = self.obterVertices()
            self.conexo = True
            for vertice in vertices:
                adjacentes = self.obterAdjacentes(vertice.obterNome())
                if len(adjacentes) == 0:
                    self.conexo = False
                arestas += len(adjacentes)
            self.conexo = arestas/2 >= len(self.obterVertices()) -1 
        return self.conexo
    
    def buscaProfundidade(self, nomeInicial, nomeFinal):
        pilha = []
        caminhos = []
        return self._buscaProfundidade(nomeInicial, nomeFinal, pilha, caminhos)
    
    def _buscaProfundidade(self, nomeInicial, nomeFinal, pilha, caminhos):
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
        
    def ehCompleto(self):
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
        return len(self.obterAdjacentes(nomeVertice))
    
    def ehArvore(self):
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
      
    def adicionarVertice(self, vertice):
        try:
            self.redefinirInferencias()
            if type(vertice) != Vertice:
                raise TypeError
            if vertice.obterNome() in self.vertices:
                raise KeyError
            self.vertices[vertice.obterNome()] = vertice
            self.adjacentes[vertice.obterNome()] = {}
        except TypeError as e:
            self._erroTipoVertice(e)
        except KeyError as e:
            self._erroChaveExiste(e)
            
    def removerVertice(self, nomeVertice):
        try:
            self.redefinirInferencias()
            for adjacente in self.obterAdjacentes(nomeVertice):
                self.removerAresta(nomeVertice, adjacente.obterNome())
            return self.vertices.pop(nomeVertice)
        except KeyError as e:
            return self._erroChaveNaoExiste(e)
         
    def adicionarAresta(self, nomeVertice1, nomeVertice2, *dados):#TODO: implementar aresta com dados
        try:
            self.redefinirInferencias()
            v1 = self.vertices[nomeVertice1]
            v2 = self.vertices[nomeVertice2]
            self.adjacentes[nomeVertice1][v2] = list(dados)
            self.adjacentes[nomeVertice2][v1] = list(dados)
        except KeyError as e:
            return self._erroChaveNaoExiste(e)
        
    def removerAresta(self, nomeVertice1, nomeVertice2):
        try:
            self.redefinirInferencias()
            v1 = self.vertices[nomeVertice1]
            v2 = self.vertices[nomeVertice2]
            self.adjacentes[nomeVertice1].pop(v2)
            self.adjacentes[nomeVertice2].pop(v1)
        except KeyError as e:
            return self._erroChaveNaoExiste(e)
        
    def obterAresta(self, nomeVertice1, nomeVertice2):
        vertice2 = self.vertices[nomeVertice2]
        return self.adjacentes[nomeVertice1][vertice2]

    def obterAdjacentes(self, nomeVertice):
        adjacentes = []
        try:
            for vertice in self.adjacentes[nomeVertice]:
                adjacentes.append(vertice)
            return adjacentes
        except KeyError as e:
            return self._erroChaveNaoExiste(e)
    
    def grau(self, nomeVertice):
        try:
            vertice = self.vertices[nomeVertice]
            return vertice.grauEmissao()
        except KeyError as e:
            return self._erroChaveNaoExiste(e)

    
class Vertice(object):
    
    def __init__(self, identificador, *dados):
        assert identificador != None
        self.nome = identificador
        self.dados = dados
        self.sucessores = {}
        self.antecessores = {}
        
    def obterNome(self):
        return self.nome
    
    def obterDados(self):
        return self.dados