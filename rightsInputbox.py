# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rightsInputbox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RightsInputbox(object):
    def setupUi(self, RightsInputbox):
        RightsInputbox.setObjectName("RightsInputbox")
        RightsInputbox.resize(616, 438)
        self.gridLayout = QtWidgets.QGridLayout(RightsInputbox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preset = QtWidgets.QComboBox(RightsInputbox)
        self.preset.setObjectName("preset")
        self.horizontalLayout.addWidget(self.preset)
        self.pushButton = QtWidgets.QPushButton(RightsInputbox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.text = QtWidgets.QPlainTextEdit(RightsInputbox)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.buttonBox = QtWidgets.QDialogButtonBox(RightsInputbox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(RightsInputbox)
        self.buttonBox.accepted.connect(RightsInputbox.accept)
        self.buttonBox.rejected.connect(RightsInputbox.reject)
        QtCore.QMetaObject.connectSlotsByName(RightsInputbox)

    def retranslateUi(self, RightsInputbox):
        _translate = QtCore.QCoreApplication.translate
        RightsInputbox.setWindowTitle(_translate("RightsInputbox", "Rights"))
        self.pushButton.setText(_translate("RightsInputbox", "Replace text with preset"))

