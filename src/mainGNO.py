# -*- coding: UTF-8 -*-
'''
Created on 07/04/2011

@author: Rafael Pedretti
'''
from grafo import Vertice, GrafoNO

if __name__ == '__main__':
    v = [Vertice(i) for i in xrange(10)]
    g1 = GrafoNO()
    g1.adicionarVertices(v)
    print 'ordem do grafo:', g1.obterOrdem()
    print 'Grau vertice 0:', g1.grau(0)
    print 'Grau vertice 1:', g1.grau(1)
    print 'É regular?:', g1.ehRegular()
    g1.adicionarAresta(0, 1)
    print 'Conectou vertice 0 com vertice 1'
    print 'É regular?:', g1.ehRegular()
    print 'Grau vertice 0:', g1.grau(0)
    print 'Grau vertice 1:', g1.grau(1)
    g1.removerVertice(0)
    print 'removeu vertice 0'
    print 'É regular?:', g1.ehRegular()
    print 'Grau vertice 1:', g1.grau(1)
    print 'ordem do grafo:', g1.obterOrdem()
    print 'É completo?:', g1.ehCompleto()
    print 'conectando todos os vertices'
    for i in xrange(1,9):
        for j in xrange(i+1,10):
            print 'Conectou vertice {0} com vertice {1}'.format(i, j)
            g1.adicionarAresta(i, j)
    print 'É completo?:', g1.ehCompleto()
    print 'removendo vertice 8', g1.removerVertice(8)
    print 'É completo?:', g1.ehCompleto()
    print 'Grau vertice 1:', g1.grau(1)
    print 'Grau vertice 7:', g1.grau(7)
    print 'remover aresta entre 1 e 7'
    g1.removerAresta(1, 7)
    print 'Grau vertice 1:', g1.grau(1)
    print 'Grau vertice 7:', g1.grau(7)
    print 'nodos adjacentes de 1: ', [i.obterNome() for i in g1.adjacentes(1)]
    print 'É completo?:', g1.ehCompleto()
    