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
        self.assertIn(self.v1, self.grafo.obterVertices())
        self.assertEqual(len(self.grafo.obterVertices()), 1)
        self.grafo.adicionarVertice(self.v0)
        self.assertEqual(len(self.grafo.obterVertices()), 2)
        
    def testObterOrdem(self):
        self.assertEqual(self.grafo.obterOrdem(), 0)
        self.grafo.adicionarVertice(self.v1)
        self.assertEqual(self.grafo.obterOrdem(), 1)
        
    def testAdicionarAresta(self):
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarAresta(0, 1)
        adjV0 = self.grafo.obterAdjacentes(0) 
        adjV1 = self.grafo.obterAdjacentes(1)
        self.assertEqual(len(adjV0), 1)
        self.assertEqual(len(adjV1), 1)
        self.assertIn(self.v0, adjV1)
        self.assertIn(self.v1, adjV0)
        
    def testRemoverAresta(self):
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarAresta(0, 1)
        self.grafo.removerAresta(0, 1)
        self.assertEqual(len(self.grafo.obterAdjacentes(0)), 0)
        self.assertEqual(len(self.grafo.obterAdjacentes(1)), 0)
        self.assertNotIn(self.v0, self.grafo.obterAdjacentes(1))
        self.assertNotIn(self.v1, self.grafo.obterAdjacentes(0))
        
    def testObterAresta(self):
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarVertice(self.v2)
        self.grafo.adicionarVertice(self.v3)
        self.grafo.adicionarAresta(0, 2, 'aresta 0 e 2')
        self.grafo.adicionarAresta(0, 1, 'peso da aresta', 'desc. aresta', 'arg3', 'etc...')
        self.assertEquals(self.grafo.obterAresta(0, 1),['peso da aresta', 'desc. aresta', 'arg3', 'etc...'])
        
        
    def testEhRegular(self):
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarVertice(self.v2)
        self.grafo.adicionarVertice(self.v3)
        self.assertTrue(self.grafo.ehRegular())
        self.grafo.adicionarAresta(0, 1)
        self.assertFalse(self.grafo.ehRegular())
        self.grafo.adicionarAresta(1, 2)
        self.assertFalse(self.grafo.ehRegular())
        self.grafo.adicionarAresta(2, 3)
        self.assertFalse(self.grafo.ehRegular())
        self.grafo.adicionarAresta(3, 0)
        self.assertTrue(self.grafo.ehRegular(),)
    
    def testEhCompleto(self):
        self.grafo.adicionarVertices(self.vertices)
        self.assertFalse(self.grafo.ehCompleto())
        for i in xrange(0,9):
            for j in xrange(i+1,10):
                self.grafo.adicionarAresta(i, j)
        self.assertTrue(self.grafo.ehCompleto())
        
    def testObterVertices(self):
        self.grafo.adicionarVertices(self.vertices)
        self.assertSequenceEqual(self.vertices, self.grafo.obterVertices(), seq_type = list)
        
    def testUmVertice(self):
        #TODO: teste fraco...
        self.grafo.adicionarVertices(self.vertices)
        vertice = self.grafo.umVertice()
        self.assertIsNotNone(vertice)
        self.assertIn(vertice, self.grafo.obterVertices())
        
    def testRemoverVertice(self):
        self.grafo.adicionarVertices(self.vertices)
        for i in xrange(0,9):
            for j in xrange(i+1,10):
                self.grafo.adicionarAresta(i, j)
        self.assertTrue(self.grafo.ehCompleto())
        vertices = self.grafo.obterVertices()
        for vertice in vertices[:-2]:
            verticeRemovido = self.grafo.removerVertice(vertice.obterNome())
            self.assertNotIn(verticeRemovido, self.grafo.obterVertices())
            self.assertEqual(vertice, verticeRemovido)
            self.assertTrue(self.grafo.ehCompleto())
        for vertice in vertices[-2:]:
            verticeRemovido = self.grafo.removerVertice(vertice.obterNome())
            self.assertNotIn(verticeRemovido, self.grafo.obterVertices())
            self.assertEqual(vertice, verticeRemovido)
            self.assertFalse(self.grafo.ehCompleto())
        self.assertEqual(self.grafo.obterOrdem(), 0)

        
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
        self.assertEqual(len(self.grafo.buscaProfundidade(0, 4)), 0)
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
        
    def testEhConexo(self):
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v2)
        self.grafo.adicionarVertice(self.v3)
        self.grafo.adicionarVertice(self.v4)
        self.assertFalse(self.grafo.ehConexo())
        self.grafo.adicionarAresta(0, 1)
        self.grafo.adicionarAresta(0, 2)
        self.grafo.adicionarAresta(0, 3)
        self.assertFalse(self.grafo.ehConexo())
        self.grafo.adicionarAresta(1, 4)
        self.assertTrue(self.grafo.ehConexo())
        self.grafo.adicionarAresta(2, 4)
        self.assertTrue(self.grafo.ehConexo())
        
    def testEhArvore(self):
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v2)
        self.grafo.adicionarVertice(self.v3)
        self.grafo.adicionarVertice(self.v4)
        self.assertFalse(self.grafo.ehArvore())
        self.grafo.adicionarAresta(0, 1)
        self.grafo.adicionarAresta(0, 2)
        self.grafo.adicionarAresta(0, 3)
        self.assertFalse(self.grafo.ehArvore())
        self.grafo.adicionarAresta(1, 4)
        self.assertTrue(self.grafo.ehArvore())
        self.grafo.adicionarAresta(2, 4)
        self.assertFalse(self.grafo.ehArvore())
        
    def testFechoTransitivo(self):
        self.grafo.adicionarVertice(self.v0)
        self.grafo.adicionarVertice(self.v1)
        self.grafo.adicionarVertice(self.v2)
        self.grafo.adicionarVertice(self.v3)
        self.grafo.adicionarVertice(self.v4)
        self.grafo.adicionarVertice(self.v5)
        self.grafo.adicionarAresta(0, 1)
        self.grafo.adicionarAresta(0, 2)
        self.grafo.adicionarAresta(2, 3)
        self.grafo.adicionarAresta(4, 5)
        fecho0 = self.grafo.fechoTransitivo(self.v0, set())
        fecho1 = self.grafo.fechoTransitivo(self.v1, set())
        fecho2 = self.grafo.fechoTransitivo(self.v2, set())
        fecho4 = self.grafo.fechoTransitivo(self.v4, set())
        fecho5 = self.grafo.fechoTransitivo(self.v5, set())
        
        print 0,fecho0
        print 1,fecho1
        print 2,fecho2
        print 4,fecho4
        print 5,fecho5
        
        self.assertEqual(fecho0, fecho1)
        self.assertEqual(fecho0, fecho2)
        self.assertEqual(fecho1, fecho0)
        self.assertEqual(fecho4, fecho5)
        self.assertEqual(fecho5, fecho4)
        self.assertTrue(len(fecho0.intersection(fecho4)) == 0)
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOpGrafo))
    return suite