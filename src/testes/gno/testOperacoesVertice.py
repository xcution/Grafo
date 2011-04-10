# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
from grafo import Vertice
import sys
if sys.version_info[:2] < (2,7):
    try:
        import unittest2 as unittest
    except ImportError:
        print 'unittest2 não instalado'
        sys.exit(1)
else:
    import unittest

class TestOpVertice(unittest.TestCase):


    def setUp(self):
        self.v1 = Vertice(1)
        self.v2 = Vertice(2)

    def testAdicionarSucessor(self):
        self.v1.adicionarSucessor(self.v2)
        self.assertIn(self.v2, self.v1.obterSucessores(), 'vertice não adicionado')
        self.assertEqual(len(self.v1.obterSucessores()), 1, \
                         'adicionado mais de um sucessor')    
        self.assertEqual(len(self.v1.obterAntecessores()), 0, \
                         'adicionado um antecessor')
        self.assertEqual(self.v1.grauEmissao(), 1, 'grau emissão errado')
        self.assertEqual(self.v1.grauRecepcao(), 0, 'grau recepção errado')
        
    def testRemoverSucessor(self):
        self.v1.adicionarSucessor(self.v2)
        removido = self.v1.removerSucessor(self.v2)
        self.assertIsNotNone(removido, 'não foi retornado nenhum sucessor')
        self.assertEqual(self.v2, removido, 'Sucessor removido não é o pedido')
        self.assertNotIn(self.v2, self.v1.obterSucessores(), 'não foi removido sucessor')
        self.assertEqual(self.v1.grauEmissao(), 0, 'grau emissão errado')
        self.assertEqual(self.v1.grauRecepcao(), 0, 'grau recepção errado')
        
    def testAdicionarAntecessor(self):
        self.v2.adicionarAntecessor(self.v1)
        self.assertIn(self.v1, self.v2.obterAntecessores(), 'vertice não adicionado')
        self.assertEqual(len(self.v2.obterAntecessores()), 1, \
                         'adicionado mais de um sucessor')    
        self.assertEqual(len(self.v1.obterSucessores()), 0, \
                         'adicionado um antecessor')
        self.assertEqual(self.v2.grauEmissao(), 0, 'grau emissão errado')
        self.assertEqual(self.v2.grauRecepcao(), 1, 'grau recepção errado')
        
    def testRemoverAntecessor(self):
        self.v2.adicionarAntecessor(self.v1)
        removido = self.v2.removerAntecessor(self.v1)
        self.assertIsNotNone(removido, 'não foi retornado nenhum sucessor')
        self.assertEqual(self.v1, removido, 'Sucessor removido não é o pedido')
        self.assertNotIn(self.v1, self.v2.obterAntecessores(), 'não foi removido sucessor')
        self.assertEqual(self.v1.grauEmissao(), 0, 'grau emissão errado')
        self.assertEqual(self.v1.grauRecepcao(), 0, 'grau recepção errado')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestOpVertice))
    return suite