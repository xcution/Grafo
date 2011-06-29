# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
from nucleo.grafo import Vertice
import unittest
    
class TestCriarVertice(unittest.TestCase):

    def testCriarVertice(self):
        nome = 'V1'
        dado1 = 'azul'
        dado2 =  2
        dados = {'cor':dado1,'custo':dado2}
        v1 = Vertice(nome, dados)
        self.assertEqual(nome, v1.obterNome())
        self.assertEqual(dados['cor'], v1.obterDado('cor'))
        self.assertEqual(dados['custo'], v1.obterDado('custo'))
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCriarVertice))
    return suite