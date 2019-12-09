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
        MainWindow.resize(897, 618)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPath = QtWidgets.QPushButton(self.centralwidget)
        self.btnPath.setGeometry(QtCore.QRect(30, 50, 121, 31))
        self.btnPath.setObjectName("btnPath")
        self.txEtatFinal = QtWidgets.QTextEdit(self.centralwidget)
        self.txEtatFinal.setGeometry(QtCore.QRect(420, 80, 171, 31))
        self.txEtatFinal.setObjectName("txEtatFinal")
        self.lbEtatFn = QtWidgets.QLabel(self.centralwidget)
        self.lbEtatFn.setGeometry(QtCore.QRect(420, 60, 47, 13))
        self.lbEtatFn.setObjectName("lbEtatFn")
        self.btnpli = QtWidgets.QPushButton(self.centralwidget)
        self.btnpli.setGeometry(QtCore.QRect(620, 40, 161, 31))
        self.btnpli.setObjectName("btnpli")
        self.btnastar = QtWidgets.QPushButton(self.centralwidget)
        self.btnastar.setGeometry(QtCore.QRect(620, 80, 161, 31))
        self.btnastar.setObjectName("btnastar")
        self.lbAlgorithm = QtWidgets.QLabel(self.centralwidget)
        self.lbAlgorithm.setGeometry(QtCore.QRect(580, 20, 71, 16))
        self.lbAlgorithm.setObjectName("lbAlgorithm")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(620, 170, 251, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.tbEtape = QtWidgets.QLabel(self.centralwidget)
        self.tbEtape.setGeometry(QtCore.QRect(620, 140, 111, 16))
        self.tbEtape.setObjectName("tbEtape")
        self.tbResolution = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbResolution.setGeometry(QtCore.QRect(370, 170, 231, 401))
        self.tbResolution.setObjectName("tbResolution")
        self.lbResolution = QtWidgets.QLabel(self.centralwidget)
        self.lbResolution.setGeometry(QtCore.QRect(370, 150, 111, 16))
        self.lbResolution.setObjectName("lbResolution")
        self.tbFaits = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbFaits.setGeometry(QtCore.QRect(30, 140, 221, 81))
        self.tbFaits.setObjectName("tbFaits")
        self.lbFaits = QtWidgets.QLabel(self.centralwidget)
        self.lbFaits.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.lbFaits.setObjectName("lbFaits")
        self.tbRegle = QtWidgets.QTextBrowser(self.centralwidget)
        self.tbRegle.setGeometry(QtCore.QRect(30, 250, 221, 321))
        self.tbRegle.setObjectName("tbRegle")
        self.lbregles = QtWidgets.QLabel(self.centralwidget)
        self.lbregles.setGeometry(QtCore.QRect(30, 230, 111, 16))
        self.lbregles.setObjectName("lbregles")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 21))
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
        self.lbEtatFn.setText(_translate("MainWindow", "Etat final"))
        self.btnpli.setText(_translate("MainWindow", "profondeur limitée itérative"))
        self.btnastar.setText(_translate("MainWindow", "l\'algorithme A*"))
        self.lbAlgorithm.setText(_translate("MainWindow", "Algorithme"))
        self.tbEtape.setText(_translate("MainWindow", "Etape de la resolution"))
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
        # test = Predicat("cruchesAetB", ['4', '2'])
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
