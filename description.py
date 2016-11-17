# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'description.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DescriptionDialog(object):
    def setupUi(self, DescriptionDialog):
        DescriptionDialog.setObjectName("DescriptionDialog")
        DescriptionDialog.resize(290, 300)
        self.layoutWidget = QtWidgets.QWidget(DescriptionDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 268, 272))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.description_type = QtWidgets.QComboBox(self.layoutWidget)
        self.description_type.setObjectName("description_type")
        self.description_type.addItem("")
        self.description_type.addItem("")
        self.description_type.addItem("")
        self.verticalLayout.addWidget(self.description_type)
        self.description_text = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.description_text.setObjectName("description_text")
        self.verticalLayout.addWidget(self.description_text)
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
        self.description_type.setItemText(0, _translate("DescriptionDialog", "Description"))
        self.description_type.setItemText(1, _translate("DescriptionDialog", "Abstract"))
        self.description_type.setItemText(2, _translate("DescriptionDialog", "Playlist"))

