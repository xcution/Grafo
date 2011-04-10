# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
import sys
if sys.version_info[:2] < (2,7):
    try:
        import unittest2 as unittest
    except ImportError:
        print 'unittest2 não instalado'
        sys.exit(1)
else:
    import unittest
from grafo import GrafoNO

class TestCriarGrafo(unittest.TestCase):


    def testCriarGrafoNO(self):
        g1 = GrafoNO()
        self.assertIsNotNone(g1, 'grafo não criado')
        self.assertEqual(g1.obterVertices(), [], 'Grafo criado não vazio')
        self.assertEqual(g1.obterOrdem(), 0, 'ordem do grafo não é 0')
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCriarGrafo))
    return suite
