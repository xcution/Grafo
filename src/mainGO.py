# -*- coding: UTF-8 -*-
'''
Created on 07/04/2011

@author: Rafael Pedretti
'''
from grafo import Vertice, GrafoO

if __name__ == '__main__':
    v = [Vertice(i) for i in xrange(10)]
    g1 = GrafoO()
    g1.adicionarVertices(v)
    print 'ordem do grafo:', g1.obterOrdem()
    print 'Grau (E/R) vertice 0:', g1.grauDeEmissao(0), g1.grauDeRecepcao(0)
    print 'Grau (E/R) vertice 1:', g1.grauDeEmissao(1), g1.grauDeRecepcao(1)
    print 'É regular?:', g1.ehRegular()
    g1.adicionarAresta(0, 1)
    print 'Conectou vertice 0 com vertice 1'
    print 'É regular?:', g1.ehRegular()
    print 'Grau (E/R) vertice 0:', g1.grauDeEmissao(0), g1.grauDeRecepcao(0)
    print 'Grau (E/R) vertice 1:', g1.grauDeEmissao(1), g1.grauDeRecepcao(1)
    g1.removerVertice(0)
    print 'removeu vertice 0'
    print 'É regular?:', g1.ehRegular()
    print 'Grau (E/R) vertice 1:', g1.grauDeEmissao(1), g1.grauDeRecepcao(1)
    print 'ordem do grafo:', g1.obterOrdem()
    print 'É completo?:', g1.ehCompleto()
    print 'conectando todos os vertices'
    for i in xrange(1,9):
        for j in xrange(i+1,10):
            g1.adicionarAresta(i, j)
            g1.adicionarAresta(j, i)
    print 'É completo?:', g1.ehCompleto()
    print 'removendo vertice 8', g1.removerVertice(8)
    print 'É completo?:', g1.ehCompleto()
    print 'Grau (E/R) vertice 1:', g1.grauDeEmissao(1), g1.grauDeRecepcao(1)
    print 'Grau (E/R) vertice 7:', g1.grauDeEmissao(7), g1.grauDeRecepcao(7)
    print 'remover aresta entre 1 e 7'
    g1.removerAresta(1, 7)
    print 'Grau (E/R) vertice 1:', g1.grauDeEmissao(1), g1.grauDeRecepcao(1)
    print 'Grau (E/R) vertice 7:', g1.grauDeEmissao(7), g1.grauDeRecepcao(7)
    print 'nodos sucessores de 1: ', [i.obterNome() for i in g1.sucessores(1)]
    print 'É completo?:', g1.ehCompleto()