# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analogpremis.ui'
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
        Dialog.resize(342, 365)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 324, 340))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.analogevent_type = QtGui.QComboBox(self.widget)
        self.analogevent_type.setObjectName(_fromUtf8("analogevent_type"))
        self.analogevent_type.addItem(_fromUtf8(""))
        self.analogevent_type.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.analogevent_type)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.analogevent_date = QtGui.QLineEdit(self.widget)
        self.analogevent_date.setText(_fromUtf8(""))
        self.analogevent_date.setObjectName(_fromUtf8("analogevent_date"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.analogevent_date)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.analogevent_details = QtGui.QPlainTextEdit(self.widget)
        self.analogevent_details.setObjectName(_fromUtf8("analogevent_details"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.analogevent_details)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.analogevent_agent = QtGui.QComboBox(self.widget)
        self.analogevent_agent.setObjectName(_fromUtf8("analogevent_agent"))
        self.analogevent_agent.addItem(_fromUtf8(""))
        self.analogevent_agent.addItem(_fromUtf8(""))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.analogevent_agent)
        self.verticalLayout.addLayout(self.formLayout_5)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_4.setText(_translate("Dialog", "Event type:", None))
        self.analogevent_type.setItemText(0, _translate("Dialog", "Physical repair", None))
        self.analogevent_type.setItemText(1, _translate("Dialog", "Rehousing", None))
        self.label_2.setText(_translate("Dialog", "Date:", None))
        self.label_3.setText(_translate("Dialog", "Details:", None))
        self.label_5.setText(_translate("Dialog", "Agent:", None))
        self.analogevent_agent.setItemText(0, _translate("Dialog", "Andrec, Michael", None))
        self.analogevent_agent.setItemText(1, _translate("Dialog", "Doe, John", None))

