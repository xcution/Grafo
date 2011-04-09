# -*- coding: UTF-8 -*-
'''
Created on 08/04/2011

@author: Rafael Pedretti
'''

import testes.gno
import unittest

if __name__ == "__main__":
    tests = []
    for module in testes.gno.__modules__:
        tests.append(module.suite())
    
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    unittest.TextTestRunner(verbosity=2).run(suite)