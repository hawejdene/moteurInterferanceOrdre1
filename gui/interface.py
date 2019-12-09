# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tp2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget, QTableWidgetItem
from model.BaseDeConnaissance import BaseDeConnaissance
from model.Graph import Graph
from model.Predicat import Predicat
from service import algorithmService
from service.algorithmService import *
from model.BaseDeConnaissance import BaseDeConnaissance


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPath = QtWidgets.QPushButton(self.centralwidget)
        self.btnPath.setGeometry(QtCore.QRect(30, 30, 121, 31))
        self.btnPath.setObjectName("btnPath")
        self.txEtatIni = QtWidgets.QTextEdit(self.centralwidget)
        self.txEtatIni.setGeometry(QtCore.QRect(190, 40, 171, 31))
        self.txEtatIni.setObjectName("txEtatIni")
        self.lbEtatinitial = QtWidgets.QLabel(self.centralwidget)
        self.lbEtatinitial.setGeometry(QtCore.QRect(190, 20, 47, 13))
        self.lbEtatinitial.setObjectName("lbEtatinitial")
        self.txEtatFinal = QtWidgets.QTextEdit(self.centralwidget)
        self.txEtatFinal.setGeometry(QtCore.QRect(190, 110, 171, 31))
        self.txEtatFinal.setObjectName("txEtatFinal")
        self.lbEtatFn = QtWidgets.QLabel(self.centralwidget)
        self.lbEtatFn.setGeometry(QtCore.QRect(200, 90, 47, 13))
        self.lbEtatFn.setObjectName("lbEtatFn")
        self.btnpli = QtWidgets.QPushButton(self.centralwidget)
        self.btnpli.setGeometry(QtCore.QRect(430, 60, 161, 31))
        self.btnpli.setObjectName("btnpli")
        self.btnastar = QtWidgets.QPushButton(self.centralwidget)
        self.btnastar.setGeometry(QtCore.QRect(430, 100, 161, 31))
        self.btnastar.setObjectName("btnastar")
        self.lbAlgorithm = QtWidgets.QLabel(self.centralwidget)
        self.lbAlgorithm.setGeometry(QtCore.QRect(430, 40, 71, 16))
        self.lbAlgorithm.setObjectName("lbAlgorithm")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(480, 210, 291, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.lbEtape = QtWidgets.QLabel(self.centralwidget)
        self.lbEtape.setGeometry(QtCore.QRect(480, 180, 111, 16))
        self.lbEtape.setObjectName("lbEtape")
        self.tbResolution = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbResolution.setGeometry(QtCore.QRect(230, 210, 231, 341))
        self.tbResolution.setObjectName("tbResolution")
        self.lbResolution = QtWidgets.QLabel(self.centralwidget)
        self.lbResolution.setGeometry(QtCore.QRect(240, 190, 111, 16))
        self.lbResolution.setObjectName("lbResolution")
        self.tbFaits = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbFaits.setGeometry(QtCore.QRect(0, 210, 221, 121))
        self.tbFaits.setObjectName("tbFaits")
        self.lbFaits = QtWidgets.QLabel(self.centralwidget)
        self.lbFaits.setGeometry(QtCore.QRect(20, 190, 111, 16))
        self.lbFaits.setObjectName("lbFaits")
        self.tbRegle = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbRegle.setGeometry(QtCore.QRect(0, 370, 221, 181))
        self.tbRegle.setObjectName("tbRegle")
        self.lbregles = QtWidgets.QLabel(self.centralwidget)
        self.lbregles.setGeometry(QtCore.QRect(20, 350, 111, 16))
        self.lbregles.setObjectName("lbregles")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnPath.setText(_translate("MainWindow", "Charger la base"))
        self.lbEtatinitial.setText(_translate("MainWindow", "Etat initial"))
        self.lbEtatFn.setText(_translate("MainWindow", "Etat final"))
        self.btnpli.setText(_translate("MainWindow", "profondeur limitée itérative"))
        self.btnastar.setText(_translate("MainWindow", "l\'algorithme A*"))
        self.lbAlgorithm.setText(_translate("MainWindow", "Algorithme"))
        self.lbEtape.setText(_translate("MainWindow", "Etape de la resolution"))
        self.lbResolution.setText(_translate("MainWindow", "Resolution"))
        self.lbFaits.setText(_translate("MainWindow", "Base des faits"))
        self.lbregles.setText(_translate("MainWindow", "Base des regles"))
        self.btnPath.clicked.connect(self.openImportBasesDialog)
        self.btnpli.clicked.connect(self.profondeurLimit)
        self.btnastar.clicked.connect(self.onStar)
        MainWindow.show()

    def openImportBasesDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'open File')
        if filename[0]:
            self.base = BaseDeConnaissance(filename[0])
            self.path = filename[0]
            string = ''
            for fait in self.base.faits:
                string += str(fait)
                string += '\n'
            self.tbFaits.setText(string)
            string = ''
            for regle in self.base.regles:
                string += str(regle)
                string += '\n'
            self.tbRegle.setText(string)
            self.isImport = True

    def profondeurLimit(self):
        self.base = BaseDeConnaissance(self.path)
        self.tbResolution.setText("")
        etatFinal = self.txEtatFinal.toPlainText()
        EtatInit = self.base.faits[0].predicat
        graphe = Graph(EtatInit)
        nouedFermées = []
        nouedOuverts = [EtatInit]
        i = 0

        # Graph construction
        while nouedOuverts:

            nouedCourant = nouedOuverts.pop(0)
            nouedFermées.append(nouedCourant)
            self.base.faits = nouedCourant
            possibleConclusions = genererConclusionUnifies(self.base.regles, nouedCourant)

            for conclusion in possibleConclusions:
                graphe.addEdge(nouedCourant, conclusion)
                if not exist(conclusion, nouedFermées) and not exist(conclusion, nouedOuverts):
                    nouedOuverts.append(conclusion)
            i += 1
        test = Predicat.extractPredicat(etatFinal)
        #test = Predicat("cruchesAetB", ['4', '2'])
        chemin = []
        solution = 'chemin:'
        print(graphe.rechercheProfendeurLimiteIteratif(graphe.V, test, 10, chemin))
        solution += '\n'
        chemin = algorithmService.prepareChemin(chemin, graphe.V)
        for chem in chemin:
            solution += str(chem) + '\n'
        self.tbResolution.setText("")
        self.tbResolution.setText(solution)
        self.textBrowser.setText("")
        self.textBrowser.setText(str(graphe.trace))

    def onStar(self):
        self.base = BaseDeConnaissance(self.path)
        self.tbResolution.setText("")
        EtatInit = self.base.faits[0].predicat
        graphe = Graph(EtatInit)
        nouedFermées = []
        nouedOuverts = [EtatInit]
        i = 0

        # Graph construction
        while nouedOuverts:

            nouedCourant = nouedOuverts.pop(0)
            nouedFermées.append(nouedCourant)
            self.base.faits = nouedCourant
            possibleConclusions = genererConclusionUnifies(self.base.regles, nouedCourant)

            for conclusion in possibleConclusions:
                graphe.addEdge(nouedCourant, conclusion)
                if not exist(conclusion, nouedFermées) and not exist(conclusion, nouedOuverts):
                    nouedOuverts.append(conclusion)
            i += 1

        etatFinal = self.txEtatFinal.toPlainText()
        test = Predicat.extractPredicat(etatFinal)
        solution = 'chemin\n'

        result, parcours = graphe.a_star_search(graphe.V, test)
        for chem in parcours:
            print(chem)
            solution += str(chem) + '\n'
        self.tbResolution.setText("")
        self.tbResolution.setText(solution)
        self.textBrowser.setText("")
        self.textBrowser.setText(graphe.trace)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
