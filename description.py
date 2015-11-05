# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'description.ui'
#
# Created: Wed Nov  4 20:38:13 2015
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

class Ui_DescriptionDialog(object):
    def setupUi(self, DescriptionDialog):
        DescriptionDialog.setObjectName(_fromUtf8("DescriptionDialog"))
        DescriptionDialog.resize(290, 300)
        self.layoutWidget = QtGui.QWidget(DescriptionDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 268, 272))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.description_type = QtGui.QComboBox(self.layoutWidget)
        self.description_type.setObjectName(_fromUtf8("description_type"))
        self.description_type.addItem(_fromUtf8(""))
        self.description_type.addItem(_fromUtf8(""))
        self.description_type.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.description_type)
        self.description_text = QtGui.QPlainTextEdit(self.layoutWidget)
        self.description_text.setObjectName(_fromUtf8("description_text"))
        self.verticalLayout.addWidget(self.description_text)
        self.buttonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DescriptionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DescriptionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DescriptionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DescriptionDialog)

    def retranslateUi(self, DescriptionDialog):
        DescriptionDialog.setWindowTitle(_translate("DescriptionDialog", "Description", None))
        self.description_type.setItemText(0, _translate("DescriptionDialog", "Description", None))
        self.description_type.setItemText(1, _translate("DescriptionDialog", "Abstract", None))
        self.description_type.setItemText(2, _translate("DescriptionDialog", "Playlist", None))

