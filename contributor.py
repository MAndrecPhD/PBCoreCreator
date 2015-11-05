# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contributor.ui'
#
# Created: Wed Nov  4 20:38:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(356, 141)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 100, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 331, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.contributor_name = QtGui.QLineEdit(self.layoutWidget)
        self.contributor_name.setObjectName(_fromUtf8("contributor_name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.contributor_name)
        self.verticalLayout.addLayout(self.formLayout)
        self.contributor_role = QtGui.QComboBox(self.layoutWidget)
        self.contributor_role.setObjectName(_fromUtf8("contributor_role"))
        self.contributor_role.addItem(_fromUtf8(""))
        self.contributor_role.addItem(_fromUtf8(""))
        self.contributor_role.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.contributor_role)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Contributor:", None))
        self.contributor_role.setItemText(0, _translate("Dialog", "Producer", None))
        self.contributor_role.setItemText(1, _translate("Dialog", "Speaker", None))
        self.contributor_role.setItemText(2, _translate("Dialog", "Author", None))

