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
    
    def resetarInferencias(self):
        self.arvore = None
        self.conexo = None
        self.regular = None
        self.completo = None

    
    def adicionarVertice(self, vertice):
        self.resetarInferencias()
        assert type(vertice) == Vertice
        self.vertices[vertice.obterNome()] = vertice
        
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
                grau = self.umVertice().grauEmissao()
                for vertice in vertices:
                    if vertice.grauEmissao() != grau:
                        self.regular = False
                        break
                    grau = vertice.grauEmissao()
        return self.regular
    
    def ehCompleto(self):
        if self.completo is None:
            vertices = self.obterVertices()
            if len(vertices) > 1:
                self.completo = True
                ordem = self.obterOrdem()
                for vertice in vertices:
                    if vertice.grauEmissao() != ordem - 1:
                        self.completo = False
                        break
            else:
                self.completo = False
        return self.completo                
            
    def fechoTransitivo(self, vertice):
        pass
    
    def ehArvore(self):
        pass

    def buscaProfundidade(self, nomeInicial, nomeFinal):
        pilha = []
        caminhos = []
        return self._buscaProfundidade(nomeInicial, nomeFinal, pilha, caminhos)
    
    def _buscaProfundidade(self, nomeInicial, nomeFinal, pilha, caminhos):
        inicial = self.vertices[nomeInicial]
        final = self.vertices[nomeFinal]
        pilha.append(inicial)
        if inicial == final:
            pilhaC = list(pilha)
            caminhos.append(pilhaC)
            return caminhos
        else:
            for vertice in inicial.obterSucessores():
                if vertice not in pilha:
                    if vertice == final:
                        pilha.append(vertice)
                        pilhaC = list(pilha)
                        caminhos.append(pilhaC)
                        pilha.pop()
                    else:
                        caminhos = self._buscaProfundidade(vertice.obterNome(), nomeFinal, pilha, caminhos)
            
            pilha.pop()
            return caminhos
                        
class GrafoNO(Grafo):
    
    def __init__(self):
        super(GrafoNO, self).__init__()
        
    def ehConexo(self):
        arestas = 0
        vertices = self.obterVertices()
        for vertice in vertices:
            adjacentes = self.adjacentes(vertice.obterNome())
            if len(adjacentes) == 0:
                return False
            arestas += len(adjacentes)
        arestas = arestas/2
        return arestas == len(vertices) - 1
    
    def removerVertice(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        self.resetarInferencias()
        vertice = self.vertices[nomeVertice]
        for adjacente in self.adjacentes(nomeVertice):
            adjacente.removerSucessor(vertice)
        return self.vertices.pop(nomeVertice)
    
    def removerAresta(self, nomeVertice1, nomeVertice2):
        assert nomeVertice1 in self.vertices.keys()
        assert nomeVertice2 in self.vertices.keys()
        self.resetarInferencias()
        v1 = self.vertices[nomeVertice1]
        v2 = self.vertices[nomeVertice2]
        v1.removerSucessor(v2)
        v2.removerSucessor(v1)
    
    def adicionarAresta(self, nomeVertice1, nomeVertice2):#TODO: implementar aresta com dados
        assert nomeVertice1 in self.vertices.keys()
        assert nomeVertice2 in self.vertices.keys()
        self.resetarInferencias()
        v1 = self.vertices[nomeVertice1]
        v2 = self.vertices[nomeVertice2]
        v1.adicionarSucessor(v2)
        v2.adicionarSucessor(v1)
        
    def adjacentes(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        vertice = self.vertices[nomeVertice]
        adjacentes = vertice.obterSucessores()
        return adjacentes
    
    def grau(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        vertice = self.vertices[nomeVertice]
        return vertice.grauEmissao()
    
class GrafoO(Grafo):
    
    def __init__(self):
        super(GrafoO, self).__init__()
        
    def ehConexo(self):
        arestas = 0
        vertices = self.obterVertices()
        for vertice in vertices:
            sucessores = self.sucessores(vertice.obterNome())
            print vertice, sucessores
            if len(sucessores) == 0:
                return False
            arestas += len(sucessores)
        return arestas == len(vertices) - 1
    
    def removerVertice(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        self.resetarInferencias()
        vertice = self.vertices[nomeVertice]
        
        for sucessor in self.sucessores(nomeVertice):
            sucessor.removerAntecessor(vertice)
        
        for antecessor in self.antecessores(nomeVertice):
            antecessor.removerSucessor(vertice)
            
        return self.vertices.pop(nomeVertice)
    
    def removerAresta(self, nomeVertice1, nomeVertice2):
        assert nomeVertice1 in self.vertices.keys()
        assert nomeVertice2 in self.vertices.keys()
        self.resetarInferencias()
        vertice1 = self.vertices[nomeVertice1]
        vertice2 = self.vertices[nomeVertice2]
        vertice1.removerSucessor(vertice2)
        vertice2.removerAntecessor(vertice1)
    
    def adicionarAresta(self, nomeVertice1, nomeVertice2):#TODO: implementar aresta com dados
        assert nomeVertice1 in self.vertices.keys()
        assert nomeVertice2 in self.vertices.keys()
        self.resetarInferencias()
        vertice1 = self.vertices[nomeVertice1]
        vertice2 = self.vertices[nomeVertice2]
        vertice1.adicionarSucessor(vertice2)
        vertice2.adicionarAntecessor(vertice1)
    
    def sucessores(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        vertice = self.vertices[nomeVertice]
        return vertice.obterSucessores()
    
    def antecessores(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        vertice = self.vertices[nomeVertice]
        return vertice.obterAntecessores()
    
    def grauDeEmissao(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        vertice = self.vertices[nomeVertice]
        return vertice.grauEmissao()
    
    def grauDeRecepcao(self, nomeVertice):
        assert nomeVertice in self.vertices.keys()
        vertice = self.vertices[nomeVertice]
        return vertice.grauRecepcao()
    
class Vertice(object):
    
    def __init__(self, identificador, *dados):
        assert identificador != None
        self.nome = identificador
        self.dados = list(dados)
        self.sucessores = {}
        self.antecessores = {}
        
    def obterNome(self):
        return self.nome
    
    def adicionarSucessor(self, sucessor):
        assert type(sucessor) == Vertice
        self.sucessores[sucessor.obterNome()] = sucessor
                
    def removerSucessor(self, sucessor):
        assert type(sucessor) == Vertice
        return self.sucessores.pop(sucessor.obterNome())
        
    def adicionarAntecessor(self, antecessor):
        assert type(antecessor) == Vertice
        self.antecessores[antecessor.obterNome()] = antecessor
        
    def removerAntecessor(self, antecessor):
        assert type(antecessor) == Vertice
        return self.antecessores.pop(antecessor.obterNome())
        
    def obterSucessores(self):
        return self.sucessores.values()
    
    def obterAntecessores(self):
        return self.antecessores.values()
    
    def grauEmissao(self):
        return len(self.sucessores)
    
    def grauRecepcao(self):
        return len(self.antecessores)