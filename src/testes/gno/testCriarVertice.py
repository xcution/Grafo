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
    
class TestCriarVertice(unittest.TestCase):

    def testCriarVertice(self):
        nome = 'V1'
        dado1 = 'azul'
        dado2 =  2
        v1 = Vertice(nome, dado1, dado2)
        self.assertEqual(nome, v1.obterNome())
        self.assertEqual((dado1,dado2), v1.obterDados())
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCriarVertice))
    return suite