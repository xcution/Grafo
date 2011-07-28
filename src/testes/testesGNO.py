# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
import os
import sys
caminho = os.path.abspath(os.path.join(os.path.dirname(__file__)))
while not caminho.endswith('src'):
	caminho = os.path.abspath(os.path.split(caminho)[0])
sys.path.append(caminho)
import unittest
import testes.gno


if __name__ == "__main__":
    tests = []
    for module in testes.gno.__modules__:
        tests.append(module.suite())
    
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    unittest.TextTestRunner(verbosity=2).run(suite)
