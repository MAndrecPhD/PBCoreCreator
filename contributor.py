# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contributor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 141)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 100, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 331, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.contributor_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.contributor_name.setObjectName("contributor_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.contributor_name)
        self.verticalLayout.addLayout(self.formLayout)
        self.contributor_role = QtWidgets.QComboBox(self.layoutWidget)
        self.contributor_role.setObjectName("contributor_role")
        self.contributor_role.addItem("")
        self.contributor_role.addItem("")
        self.contributor_role.addItem("")
        self.verticalLayout.addWidget(self.contributor_role)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Contributor:"))
        self.contributor_role.setItemText(0, _translate("Dialog", "Producer"))
        self.contributor_role.setItemText(1, _translate("Dialog", "Speaker"))
        self.contributor_role.setItemText(2, _translate("Dialog", "Author"))

