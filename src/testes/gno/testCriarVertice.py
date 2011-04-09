# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
from grafo import Vertice
import sys
if sys.version_info[:2] <(2,7):
    try:
        import unittest2 as unittest
    except ImportError:
        print "unittest2 não encontrado! Você precisa do unittest2 instalado."
else:
    import unittest


class TestCriarVertice(unittest.TestCase):

    def testCriarVertice(self):
        nome = 'V1'
        v1 = Vertice(nome)
        self.assertEqual(nome, v1.obterNome(), 'Vertice criado com nome diferente')
        self.assertEqual(v1.obterSucessores(), [], 'vertice criado com sucessores')
        self.assertEqual(v1.obterAntecessores(), [], 'vertice criado com antessores')
        self.assertEqual(v1.grauEmissao(), 0, 'Vertice criado com uma aresta de saida')
        self.assertEqual(v1.grauRecepcao(), 0, 'Vertice criado com uma aresta de entrada')
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCriarVertice))
    return suite