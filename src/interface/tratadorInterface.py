#-*- coding: utf-8 -*-
'''
Created on 17/06/2011

@author: pepe
'''
from PyQt4.QtCore import pyqtSlot, pyqtSignal, SIGNAL, QSignalMapper, SLOT, QString
from PyQt4.QtGui import QMainWindow, QComboBox, QMessageBox, QTableWidgetItem, \
    QListWidgetItem, QInputDialog, QLineEdit, QSizePolicy
from interface.interfaceQt import Ui_InterfaceQt
from nucleo.grafo import GrafoNO
from recursos.Observable import Observer

class TratadorInterface(QMainWindow, Ui_InterfaceQt, Observer):
    
    erro_vertice_existe = pyqtSignal()
    erro_vertice_nao_existe = pyqtSignal(str)
    
    def __init__(self):
        Observer.__init__(self)
        QMainWindow.__init__(self)
        super(TratadorInterface, self).__init__(self)
        self.setupUi(self)
        self.erro_vertice_existe.connect(self.verticeExiste)
        self.erro_vertice_nao_existe.connect(self.verticeNaoExiste)
        self.eh_funcao.setEnabled(False)
        self.funcao_edit.setEnabled(False)
        self.grafo = None
        self.signalMapper = QSignalMapper(self)
        
    
    @pyqtSlot()
    def on_adicionar_vertice_button_clicked(self):
        if not self.grafo:
            nome = str(self.nome_edit.text())
            if nome == '':
                QMessageBox(self).critical(self, 'ERRO', 'O Gravo deve ter um nome!', buttons=QMessageBox.Ok)
                return
            self.grafo = GrafoNO(nome)
            self.observe(self.grafo)
        self.limparInferencias()
        vertices = str(self.vertices_edit.text())
        vertices = vertices.split(',')
        if len(vertices) > 0:
            self.signalMapper = QSignalMapper(self)
            for vertice in vertices:
                vertice = vertice.strip()
                if vertice != '':
                    cont = self.tabela_adjacencia.rowCount()
                    item = QTableWidgetItem(vertice)
                    self.tabela_adjacencia.insertColumn(cont)
                    self.tabela_adjacencia.insertRow(cont)
                    self.tabela_adjacencia.setHorizontalHeaderItem(cont,item)
                    self.tabela_adjacencia.setVerticalHeaderItem(cont,item)
                    self.grafo.adicionarVertice(vertice)

                for x in xrange(self.tabela_adjacencia.rowCount()):
                    comboV = QComboBox(self)
                    comboH = QComboBox(self)
                    
                    comboV.addItems(['0','1'])
                    comboH.addItems(['0','1'])
                    comboV.setSizePolicy(QSizePolicy().Minimum, QSizePolicy().Minimum)
                    comboH.setSizePolicy(QSizePolicy().Minimum, QSizePolicy().Minimum)
                    self.tabela_adjacencia.setCellWidget(cont,x,comboH)
                    self.tabela_adjacencia.setCellWidget(x,cont,comboV)
                        
            for x in xrange(self.tabela_adjacencia.rowCount()):
                for y in xrange(self.tabela_adjacencia.rowCount()):
                    item = self.tabela_adjacencia.cellWidget(x, y)
                    self.connect(item, SIGNAL('currentIndexChanged(int)'),self.signalMapper, SLOT('map()'))
                    self.signalMapper.setMapping(item, '{0};{1}'.format(x,y))
                    self.connect(self.signalMapper, SIGNAL('mapped(QString)'), self.valorAlterado)
                    
            self.tabela_adjacencia.resizeColumnsToContents()
            self.tabela_adjacencia.resizeRowsToContents()
            self.fecho_origem.addItems(vertices)
            self.informacoes_vertice.addItems(vertices)
            self.busca_destino.addItems(vertices)
            self.busca_origem.addItems(vertices)
            self.remover_vertice_combo.addItems(vertices)
            self.ordem_resultado.setText(str(self.grafo.obterOrdem()))
            self.gerar_arestas_button.setEnabled(True)
            self.vertices_edit.clear()
    
    @pyqtSlot()            
    def on_remover_vertice_button_clicked(self):
        '''TODO: Verificar o segfault
        '''
        pass
#        vertice = self.remover_vertice_combo.currentText()
#        colunas = self.tabela_adjacencia.columnCount()
#        for x in xrange(colunas):
#            if vertice == str(self.tabela_adjacencia.horizontalHeaderItem(x).text()):
#                for y in xrange(self.tabela_adjacencia.columnCount()):
#                    self.tabela_adjacencia.removeCellWidget(y,x)
#                self.tabela_adjacencia.removeColumn(x)
#                self.fecho_origem.removeItem(self.fecho_origem.findText(vertice))
#                self.informacoes_vertice.removeItem(self.informacoes_vertice.findText(vertice))
#                self.busca_destino.removeItem(self.busca_destino.findText(vertice))
#                self.busca_origem.removeItem(self.busca_origem.findText(vertice))
#                self.remover_vertice_combo.removeItem(self.remover_vertice_combo.findText(vertice))
#                self.ordem_resultado.setText(str(self.grafo.obterOrdem()))
#                break
           
    @pyqtSlot()
    def on_gerar_arestas_button_clicked(self):
        self.limparInferencias()
        self.grafo.limpar()
        n_linhas = self.tabela_adjacencia.rowCount()
        n_colunas = self.tabela_adjacencia.columnCount()
        for x in xrange(n_linhas):
            for y in xrange(x,n_colunas):
                item = self.tabela_adjacencia.cellWidget(x, y)
                if item.currentText() == '1':
                    v1 = str(self.tabela_adjacencia.horizontalHeaderItem(x).text())
                    v2 = str(self.tabela_adjacencia.verticalHeaderItem(y).text())
                    valor = None
                    if self.valorar_aresta.isChecked():
                        ok = False
                        while not ok:
                            valor,ok = QInputDialog().getText(self, 'Dados para a aresta {0}-{1} (separados por ",")'.format(v1,v2), 
                                                           'Dados:', mode=QLineEdit.Normal, 
                                                           text=QString())
                            valor = str(valor)
                            if not ok:
                                sair = QMessageBox.question(self, 'Cancelar?', u'deseja cancelar a criação do grafo?',
                                                            buttons=QMessageBox.Yes | QMessageBox.No, defaultButton=QMessageBox.NoButton)
                                
                                if sair == QMessageBox.Yes:
                                    self.grafo.limpar()
                                    return
                            elif valor == '':
                                atribuir_zero = QMessageBox.question(self, 'Valor em branco!', u'Atribuit valor "0" à aresta?', 
                                                                     buttons=QMessageBox.Yes | QMessageBox.No, defaultButton=QMessageBox.NoButton)
                                if atribuir_zero:
                                    valor = '0'
                                else:
                                    valor = None
                            valor = valor.split(',')
                            valor = [string.strip() for string in valor]
                            for dado in valor:
                                if dado.isdigit():
                                    valor[valor.index(dado)] = int(dado)
                                else:
                                    try:
                                        valor[valor.index(dado)] = float(dado)
                                    except ValueError:
                                        pass
                    if valor:
                        self.grafo.adicionarAresta(v1, v2, tuple(valor))
                    else:
                        self.grafo.adicionarAresta(v1, v2, valor)
        self.eh_conexo.setChecked(self.grafo.ehConexo())
        self.eh_arvore.setChecked(self.grafo.ehArvore())
        self.eh_regular.setChecked(self.grafo.ehRegular())
        self.eh_completo.setChecked(self.grafo.ehCompleto())
    
    @pyqtSlot()
    def on_busca_profundidade_button_clicked(self):
        self.busca_resultado.clear()
        verticeInicial = str(self.busca_origem.currentText())
        verticeFinal = str(self.busca_destino.currentText())
        resultados = self.grafo.buscaProfundidade(verticeInicial, verticeFinal)
        for resultado in resultados:
            caminho = str([vertice.obterNome() for vertice in resultado]) + '\n'
            item = QListWidgetItem(caminho)
            self.busca_resultado.addItem(item)
    @pyqtSlot()
    def on_informacoes_button_clicked(self):
        self.busca_resultado.clear()
        vertice = str(self.informacoes_vertice.currentText())
        '''Mostrar grau'''
        grau = self.grafo.obterGrau(vertice)
        self.busca_resultado.addItem(QListWidgetItem('Grau: ' + str(grau)))
        
        '''Mostrar adjacentes e info das arestas'''
        adjacentes = self.grafo.obterAdjacentes(vertice)
        self.busca_resultado.addItem(QListWidgetItem('Adjacentes:'))
        for adjacente in adjacentes:
            texto_valor = ''
            valor = self.grafo.obterAresta(vertice, adjacente.obterNome())
            texto = '\t'+adjacente.obterNome()
            if valor:
                for x in xrange(len(valor)):
                    texto_valor += str(valor[x]) + ', '
                texto += ': ' + texto_valor[:-2]
            self.busca_resultado.addItem(QListWidgetItem(texto))
    
    @pyqtSlot('QString')
    def on_fecho_origem_activated(self, vertice):
        fecho = self.grafo.fechoTransitivo(str(vertice), set())
        resultado = ''
        while fecho:
            resultado += fecho.pop() + ', '
        self.fecho_resultado.setText(resultado[:-2])
        
    @pyqtSlot('bool')
    def on_valorar_aresta_toggled(self,marcado):
        if not marcado:
            self.eh_funcao.setChecked(marcado)
            self.funcao_edit.setEnabled(marcado)
        self.eh_funcao.setEnabled(marcado)
        
    @pyqtSlot('bool')
    def on_eh_funcao_toggled(self,marcado):
        self.funcao_edit.setEnabled(marcado)
    
    @pyqtSlot('QString')
    def on_nome_edit_textChanged(self, texto):
        if texto == '':
            self.adicionar_vertice_button.setEnabled(False)
        elif len(self.vertices_edit.text()) > 0:
            self.adicionar_vertice_button.setEnabled(True)

    @pyqtSlot('QString')
    def on_vertices_edit_textChanged(self, texto):
        if texto == '':
            self.adicionar_vertice_button.setEnabled(False)
        elif len(self.nome_edit.text()) > 0:
            self.adicionar_vertice_button.setEnabled(True)
                
    def processEvent(self, notificador, evento, *args):
        if notificador == self.grafo:
            if evento == 'VerticeNaoExiste':
                self.erro_vertice_nao_existe.emit(args[0])
            elif evento == 'VerticeJahExiste':
                self.erro_vertice_existe.emit()
    
    def limparItens(self):
        self.fecho_origem.clear()
        self.informacoes_vertice.clear()
        self.busca_destino.clear()
        self.busca_origem.clear()
        self.ordem_resultado.setText('')
        
    def limparInferencias(self):
        self.eh_conexo.setChecked(False)
        self.eh_arvore.setChecked(False)
        self.eh_regular.setChecked(False)
        self.eh_completo.setChecked(False)
        
    def verticeExiste(self):
        QMessageBox(self).critical(self, 'ERRO!', u'Existe mais de um vértice com o mesmo nome!', buttons=QMessageBox.Ok)
        self.limparInferencias()
        self.limparItens()
        self.tabela_adjacencia.setRowCount(0)
        self.tabela_adjacencia.setColumnCount(0)
    
    def verticeNaoExiste(self,e):
        QMessageBox(self).critical(self, 'ERRO', e, buttons=QMessageBox.Ok)
    
    @pyqtSlot('QString')
    def valorAlterado(self,string):
        string = str(string)
        pos = string.split(';')
        item2 = self.tabela_adjacencia.cellWidget(int(pos[1]), int(pos[0]))
        item1 = self.tabela_adjacencia.cellWidget(int(pos[0]), int(pos[1]))
        item2.setCurrentIndex(item1.currentIndex())
