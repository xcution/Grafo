#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
Created on 03/03/2011

@author: Rafael Pedretti
'''

from PyQt4.QtGui import QApplication
from multiprocessing import freeze_support
import sys
import os
caminho = os.path.abspath(os.path.join(os.path.dirname(__file__)))
caminho = os.path.abspath(os.path.split(caminho)[0])
sys.path.append(caminho)
from interface.tratadorInterface import TratadorInterface


if __name__ == '__main__':
    freeze_support()
    app = QApplication(sys.argv)
    janela = TratadorInterface()
    janela.show()
    app.exec_()
