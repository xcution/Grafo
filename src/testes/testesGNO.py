# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''
import os
import sys
caminho = os.path.abspath(os.path.join(os.path.dirname(__file__)))
caminho = os.path.abspath(os.path.split(caminho)[0])
sys.path.append(caminho)
if sys.version_info[:2] < (2,7):
    try:
        import unittest2 as unittest
    except ImportError:
        print 'unittest2 não instalado'
        sys.exit(1)
else:
    import unittest
import testes.gno


if __name__ == "__main__":
    tests = []
    for module in testes.gno.__modules__:
        tests.append(module.suite())
    
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    unittest.TextTestRunner(verbosity=2).run(suite)
