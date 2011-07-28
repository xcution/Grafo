# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
from nucleo.grafo import GrafoNO
import unittest
    
class TestOpGrafo(unittest.TestCase):

    def setUp(self):
        self.grafo = GrafoNO('Teste')
        
    def tearDown(self):
        del self.grafo

    def testAdicionarVertice(self):
        self.grafo.adicionarVertice('v1')
        self.assertIn('v1', [x.obterNome() for x in self.grafo.obterVertices()])
        self.assertEqual(self.grafo.obterOrdem(), 1)
        self.grafo.adicionarVertice('v0')
        self.assertEqual(self.grafo.obterOrdem(), 2)
        
    def testObterOrdem(self):
        self.assertEqual(self.grafo.obterOrdem(), 0)
        self.grafo.adicionarVertice('v1')
        self.assertEqual(self.grafo.obterOrdem(), 1)
        
    def testAdicionarAresta(self):
        self.grafo.adicionarVertice('v1')
        self.grafo.adicionarVertice('v0')
        self.grafo.adicionarAresta('v0', 'v1')
        adjV0 = self.grafo.obterAdjacentes('v0') 
        adjV1 = self.grafo.obterAdjacentes('v1')
        self.assertEqual(len(adjV0), 1)
        self.assertEqual(len(adjV1), 1)
        self.assertIn('v0', [x.obterNome() for x in adjV1])
        self.assertIn('v1', [x.obterNome() for x in adjV0])
        
    def testRemoverAresta(self):
        self.grafo.adicionarVertice(1)
        self.grafo.adicionarVertice(0)
        self.grafo.adicionarAresta(0, 1)
        self.grafo.removerAresta(0, 1)
        self.assertEqual(len(self.grafo.obterAdjacentes(0)), 0)
        self.assertEqual(len(self.grafo.obterAdjacentes(1)), 0)
        self.assertNotIn(0, self.grafo.obterAdjacentes(1))
        self.assertNotIn(1, self.grafo.obterAdjacentes(0))
        
    def testObterAresta(self):
        self.grafo.adicionarVertice(1)
        self.grafo.adicionarVertice(0)
        self.grafo.adicionarVertice(2)
        self.grafo.adicionarVertice(3)
        self.grafo.adicionarAresta(0, 2, {'custo':2})
        self.grafo.adicionarAresta(0, 1, {'peso da aresta': 3, 'desc. aresta':'muito custosa'})
        dados = self.grafo.obterAresta(0, 1)
        self.assertEquals(dados.get('peso da aresta'), 3)
        self.assertEqual(dados.get('desc. aresta'), 'muito custosa')
        
        
    def testEhRegular(self):
        self.grafo.adicionarVertice('v1')
        self.grafo.adicionarVertice('v0')
        self.grafo.adicionarVertice('v2')
        self.grafo.adicionarVertice('v3')
        self.assertTrue(self.grafo.ehRegular())
        self.grafo.adicionarAresta('v0', 'v1')
        self.assertFalse(self.grafo.ehRegular())
        self.grafo.adicionarAresta('v1', 'v2')
        self.assertFalse(self.grafo.ehRegular())
        self.grafo.adicionarAresta('v2', 'v3')
        self.assertFalse(self.grafo.ehRegular())
        self.grafo.adicionarAresta('v3', 'v0')
        self.assertTrue(self.grafo.ehRegular(),)
    
    def testEhCompleto(self):
        self.grafo.adicionarVertices(['v'+str(x) for x in xrange(10)], [() for _ in xrange(10)] )
        self.assertFalse(self.grafo.ehCompleto())
        for i in xrange(0,9):
            for j in xrange(i+1,10):
                self.grafo.adicionarAresta('v'+str(i), 'v'+str(j))
        self.assertTrue(self.grafo.ehCompleto())
        
    def testUmVertice(self):
        #TODO: teste fraco...
        self.grafo.adicionarVertices([x for x in xrange(10)], [() for _ in xrange(10)] )
        vertice = self.grafo.umVertice()
        self.assertIsNotNone(vertice)
        self.assertIn(vertice, self.grafo.obterVertices())
        
    def testRemoverVertice(self):
        self.grafo.adicionarVertices([x for x in xrange(10)], [() for _ in xrange(10)] )
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

        
#    def testBuscaProfundidade(self):
#        self.grafo.adicionarVertice(0)
#        self.grafo.adicionarVertice(1)
#        self.grafo.adicionarVertice(2)
#        self.grafo.adicionarVertice(3)
#        self.grafo.adicionarVertice(4)
#        self.grafo.adicionarVertice(5)
#        self.grafo.adicionarAresta(0, 1)
#        self.grafo.adicionarAresta(0, 2)
#        self.grafo.adicionarAresta(0, 3)
#        self.assertEqual(len(self.grafo.buscaProfundidade(0, 4)), 0)
#        self.grafo.adicionarAresta(1, 4)
#        self.grafo.adicionarAresta(2, 4)
#        self.grafo.adicionarAresta(3, 5)
#        
#        v0 = self.grafo.obterVertice(0)
#        v1 = self.grafo.obterVertice(1)
#        v2 = self.grafo.obterVertice(2)
#        v3 = self.grafo.obterVertice(3)
#        v4 = self.grafo.obterVertice(4)
#        v5 = self.grafo.obterVertice(5)
#        
#        caminhos = self.grafo.buscaProfundidade(0, 1)
#        self.assertEqual(len(caminhos), 2)
#        self.assertIn([v0, v1], caminhos)
#        self.assertIn([v0, v2, v4, v1], caminhos)
#        caminhos = self.grafo.buscaProfundidade(0, 3)
#        self.assertEqual(len(caminhos), 1)
#        self.assertIn([v0,v3], caminhos)
#        caminhos = self.grafo.buscaProfundidade(0, 2)
#        self.assertEqual(len(caminhos), 2)
#        self.assertIn([v0, v2], caminhos)
#        self.assertIn([v0, v1, v4, v2], caminhos)
#        caminhos = self.grafo.buscaProfundidade(3, 5)
#        self.assertEqual(len(caminhos), 1)
#        self.assertIn([v3, v5], caminhos)
#        caminhos = self.grafo.buscaProfundidade(3, 4)
#        self.assertEqual(len(caminhos), 2)
#        self.assertIn([v3, v0, v2, v4], caminhos)
#        self.assertIn([v3, v0, v1, v4], caminhos)
        
    def testEhConexo(self):
        self.grafo.adicionarVertice(0)
        self.grafo.adicionarVertice(1)
        self.grafo.adicionarVertice(2)
        self.grafo.adicionarVertice(3)
        self.grafo.adicionarVertice(4)
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
        self.grafo.adicionarVertice(0)
        self.grafo.adicionarVertice(1)
        self.grafo.adicionarVertice(2)
        self.grafo.adicionarVertice(3)
        self.grafo.adicionarVertice(4)
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
        self.grafo.adicionarVertice(0)
        self.grafo.adicionarVertice(1)
        self.grafo.adicionarVertice(2)
        self.grafo.adicionarVertice(3)
        self.grafo.adicionarVertice(4)
        self.grafo.adicionarVertice(5)
        self.grafo.adicionarAresta(0, 1)
        self.grafo.adicionarAresta(0, 2)
        self.grafo.adicionarAresta(2, 3)
        self.grafo.adicionarAresta(4, 5)
        fecho0 = self.grafo.fechoTransitivo(0, set())
        fecho1 = self.grafo.fechoTransitivo(1, set())
        fecho2 = self.grafo.fechoTransitivo(2, set())
        fecho4 = self.grafo.fechoTransitivo(4, set())
        fecho5 = self.grafo.fechoTransitivo(5, set())
        
#        print 0,fecho0
#        print 1,fecho1
#        print 2,fecho2
#        print 4,fecho4
#        print 5,fecho5
#        
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