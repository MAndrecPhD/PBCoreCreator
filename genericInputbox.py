# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genericInputbox.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DescriptionDialog(object):
    def setupUi(self, DescriptionDialog):
        DescriptionDialog.setObjectName("DescriptionDialog")
        DescriptionDialog.resize(326, 438)
        self.layoutWidget = QtWidgets.QWidget(DescriptionDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.attribute = QtWidgets.QComboBox(self.layoutWidget)
        self.attribute.setObjectName("attribute")
        self.verticalLayout.addWidget(self.attribute)
        self.text = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.preset = QtWidgets.QComboBox(self.layoutWidget)
        self.preset.setObjectName("preset")
        self.verticalLayout.addWidget(self.preset)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DescriptionDialog)
        self.buttonBox.accepted.connect(DescriptionDialog.accept)
        self.buttonBox.rejected.connect(DescriptionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DescriptionDialog)

    def retranslateUi(self, DescriptionDialog):
        _translate = QtCore.QCoreApplication.translate
        DescriptionDialog.setWindowTitle(_translate("DescriptionDialog", "Description"))

