# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
from grafo import Vertice, GrafoNO
import sys
if sys.version_info[:2] < (2,7):
    try:
        import unittest2 as unittest
    except ImportError:
        print 'unittest2 não instalado'
        sys.exit(1)
else:
    import unittest
class TestOpGrafo(unittest.TestCase):


    def setUp(self):
        self.grafo = GrafoNO()
        self.vertices = [Vertice(i) for i in xrange(10)]
        self.v0 = self.vertices[0]
        self.v1 = self.vertices[1]
        self.v2 = self.vertices[2]
        self.v3 = self.vertices[3]
        self.v4 = self.vertices[4]
        self.v5 = self.vertices[5]

    def testAdicionarVertice(self):
        self.grafo.adicionarVertice(self.v1)
        self.assertIn(self.v1, self.grafo.obterVertices(), 'vertice não adicionado')
        self.assertEqual(len(self.grafo.obterVertices()), 1, 'numero de vertices incorreto')
        self.grafo.adicionarVertice(self.v0)
        self.assertEqual(len(self.grafo.obterVertices()), 2, 'numero de vertices incorreto')
        
    def testObterOrdem(self):
        self.assertEqual(self.grafo.obterOrdem(), 0, 'ordem do grafo incorreta')
        self.grafo.adicionarVertice(self.v1)
        self.assertEqual(self.grafo.obterOrdem(), 1, 'ordem do grafo incorreta')
        
    def testAdicionarAresta(self):
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarAresta(0, 1)
        self.assertEqual(len(self.grafo.adjacentes(0)), 1, 'era para ter apenas um adjacente')
        self.assertEqual(len(self.grafo.adjacentes(1)), 1, 'era para ter apenas um adjacente')
        self.assertIn(self.v0, self.grafo.adjacentes(1), 'v0 era para estar como adjacente de v1')
        self.assertIn(self.v1, self.grafo.adjacentes(0), 'v1 era para estar como sucessor de v0')
        
    def testRemoverAresta(self):
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarAresta(0, 1)
        self.grafo.removerAresta(0, 1)
        self.assertEqual(len(self.grafo.adjacentes(0)), 0, 'era para ter apenas um adjacente')
        self.assertEqual(len(self.grafo.adjacentes(1)), 0, 'era para ter apenas um adjacente')
        self.assertNotIn(self.v0, self.grafo.adjacentes(1), 'v0 era para estar como adjacente de v1')
        self.assertNotIn(self.v1, self.grafo.adjacentes(0), 'v1 era para estar como sucessor de v0')
        
    def testEhRegular(self):
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarVertice(self.v2)
        self.grafo.adicionarVertice(self.v3)
        self.assertTrue(self.grafo.ehRegular(), 'era pra ser regular')
        self.grafo.adicionarAresta(0, 1)
        self.assertFalse(self.grafo.ehRegular(), 'não era pra ser regular')
        self.grafo.adicionarAresta(1, 2)
        self.assertFalse(self.grafo.ehRegular(), 'não era pra ser regular')
        self.grafo.adicionarAresta(2, 3)
        self.assertFalse(self.grafo.ehRegular(), 'não era pra ser regular')
        self.grafo.adicionarAresta(3, 0)
        self.assertTrue(self.grafo.ehRegular(), 'era pra ser regular')
    
    def testEhCompleto(self):
        self.grafo.adicionarVertices(self.vertices)
        self.assertFalse(self.grafo.ehCompleto(), 'não era pra ser completo')
        for i in xrange(0,9):
            for j in xrange(i+1,10):
                self.grafo.adicionarAresta(i, j)
        self.assertTrue(self.grafo.ehCompleto(), 'era pra ser completo')
        
    def testObterVertices(self):
        self.grafo.adicionarVertices(self.vertices)
        self.assertSequenceEqual(self.vertices, self.grafo.obterVertices(), \
                                 'as listas deveriam ser iguais', seq_type = list)
        
    def testUmVertice(self):
        #TODO: teste fraco...
        self.grafo.adicionarVertices(self.vertices)
        vertice = self.grafo.umVertice()
        self.assertIsNotNone(vertice, 'retornado Null ao invés de um Vertice')
        self.assertIn(vertice, self.grafo.obterVertices(), \
                      'retornou um vertice não pertencente ao grafo')
        
    def testRemoverVertice(self):
        self.grafo.adicionarVertices(self.vertices)
        for i in xrange(0,9):
            for j in xrange(i+1,10):
                self.grafo.adicionarAresta(i, j)
        self.assertTrue(self.grafo.ehCompleto(), 'era pra ser completo')
        vertices = self.grafo.obterVertices()
        for vertice in vertices[:-2]:
            verticeRemovido = self.grafo.removerVertice(vertice.obterNome())
            self.assertNotIn(verticeRemovido, self.grafo.obterVertices(), 'vertice não removido efetivamente')
            self.assertEqual(vertice, verticeRemovido, 'era para serem o mesmo Vertice')
            self.assertTrue(self.grafo.ehCompleto(), 'era para ser completo')
        for vertice in vertices[-2:]:
            verticeRemovido = self.grafo.removerVertice(vertice.obterNome())
            self.assertNotIn(verticeRemovido, self.grafo.obterVertices(), 'vertice não removido efetivamente')
            self.assertEqual(vertice, verticeRemovido, 'era para serem o mesmo Vertice')
            self.assertFalse(self.grafo.ehCompleto(), 'era para ser completo')
        self.assertEqual(self.grafo.obterOrdem(), 0, 'era para estar vazio')

        
    def testBuscaProfundidade(self):
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v2)
        self.grafo.adicionarVertice(self.v3)
        self.grafo.adicionarVertice(self.v4)
        self.grafo.adicionarVertice(self.v5)
        self.grafo.adicionarAresta(0, 1)
        self.grafo.adicionarAresta(0, 2)
        self.grafo.adicionarAresta(0, 3)
        self.grafo.adicionarAresta(1, 4)
        self.grafo.adicionarAresta(2, 4)
        self.grafo.adicionarAresta(3, 5)
        caminhos = self.grafo.buscaProfundidade(0, 1)
        self.assertEqual(len(caminhos), 2)
        self.assertIn([self.v0, self.v1], caminhos)
        self.assertIn([self.v0, self.v2, self.v4, self.v1], caminhos)
        caminhos = self.grafo.buscaProfundidade(0, 3)
        self.assertEqual(len(caminhos), 1)
        self.assertIn([self.v0, self.v3], caminhos)
        caminhos = self.grafo.buscaProfundidade(0, 2)
        self.assertEqual(len(caminhos), 2)
        self.assertIn([self.v0, self.v2], caminhos)
        self.assertIn([self.v0, self.v1, self.v4, self.v2], caminhos)
        caminhos = self.grafo.buscaProfundidade(3, 5)
        self.assertEqual(len(caminhos), 1)
        self.assertIn([self.v3, self.v5], caminhos)
        caminhos = self.grafo.buscaProfundidade(3, 4)
        self.assertEqual(len(caminhos), 2)
        self.assertIn([self.v3, self.v0, self.v2, self.v4], caminhos)
        self.assertIn([self.v3, self.v0, self.v1, self.v4], caminhos)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOpGrafo))
    return suite