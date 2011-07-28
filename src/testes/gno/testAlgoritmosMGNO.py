# -*- coding: UTF-8 -*-
'''
Created on 25/06/2011

@author: juarez
'''
''
import unittest
from nucleo.algoritmosGrafoNO import AlgoritmosGrafoNO

class TestAlgoritmosMGNO(unittest.TestCase):

    def setUp(self):
        self.grafo = AlgoritmosGrafoNO('Teste')
        
    def tearDown(self):
        del self.grafo

    def testBuscaProfundidade(self):
        self.grafo.adicionarVertice(0)
        self.grafo.adicionarVertice(1)
        self.grafo.adicionarVertice(2)
        self.grafo.adicionarVertice(3)
        self.grafo.adicionarVertice(4)
        self.grafo.adicionarVertice(5)
        self.grafo.adicionarAresta(0, 1)
        self.grafo.adicionarAresta(0, 2)
        self.grafo.adicionarAresta(0, 3)
        self.assertEqual(len(self.grafo.buscaProfundidade(0, 4)), 0)
        self.grafo.adicionarAresta(1, 4)
        self.grafo.adicionarAresta(2, 4)
        self.grafo.adicionarAresta(3, 5)
        
        v0 = self.grafo.obterVertice(0)
        v1 = self.grafo.obterVertice(1)
        v2 = self.grafo.obterVertice(2)
        v3 = self.grafo.obterVertice(3)
        v4 = self.grafo.obterVertice(4)
        v5 = self.grafo.obterVertice(5)
        
        caminhos = self.grafo.buscaProfundidade(0, 1)
        self.assertEqual(len(caminhos), 2)
        self.assertIn([v0, v1], caminhos)
        self.assertIn([v0, v2, v4, v1], caminhos)
        caminhos = self.grafo.buscaProfundidade(0, 3)
        self.assertEqual(len(caminhos), 1)
        self.assertIn([v0,v3], caminhos)
        caminhos = self.grafo.buscaProfundidade(0, 2)
        self.assertEqual(len(caminhos), 2)
        self.assertIn([v0, v2], caminhos)
        self.assertIn([v0, v1, v4, v2], caminhos)
        caminhos = self.grafo.buscaProfundidade(3, 5)
        self.assertEqual(len(caminhos), 1)
        self.assertIn([v3, v5], caminhos)
        caminhos = self.grafo.buscaProfundidade(3, 4)
        self.assertEqual(len(caminhos), 2)
        self.assertIn([v3, v0, v2, v4], caminhos)
        self.assertIn([v3, v0, v1, v4], caminhos)

    def testColorirGrafoNO(self):
#       inicializar grafo g1, não conexo, conexo.
        k = 200
              
        for x in xrange(k):
            self.grafo.adicionarVertice(x)

        for x in xrange(k):
            for y in xrange(x+1, k):
                self.grafo.adicionarAresta(x, y)
        
#        self.grafo.adicionarAresta(0, 1)
#        self.grafo.adicionarAresta(0, 4)
#        self.grafo.adicionarAresta(0, 5)
#        self.grafo.adicionarAresta(1, 2)
#        self.grafo.adicionarAresta(1, 6)
#        self.grafo.adicionarAresta(2, 3)
#        self.grafo.adicionarAresta(2, 7)
#        self.grafo.adicionarAresta(3, 8)
#        self.grafo.adicionarAresta(3, 4)
#        self.grafo.adicionarAresta(4, 9)
#        self.grafo.adicionarAresta(5, 7)
#        self.grafo.adicionarAresta(5, 8)
#        self.grafo.adicionarAresta(6, 8)
#        self.grafo.adicionarAresta(6, 9)
#        self.grafo.adicionarAresta(7, 9)
        
        num_cromatico,tempo = self.grafo.colorirVertices()
#        for vertice in self.grafo.obterVertices():
#            print vertice.obterNome(), '\t', vertice.obterDados()['cor']
        print num_cromatico, tempo
#        self.assertTrue(num_cromatico == k)
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAlgoritmosMGNO))
    return suite
