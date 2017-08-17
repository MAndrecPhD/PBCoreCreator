# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analogpremis.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnalogpremisInputbox(object):
    def setupUi(self, AnalogpremisInputbox):
        AnalogpremisInputbox.setObjectName("AnalogpremisInputbox")
        AnalogpremisInputbox.resize(342, 365)
        self.layoutWidget = QtWidgets.QWidget(AnalogpremisInputbox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 324, 340))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.analogevent_type = QtWidgets.QComboBox(self.layoutWidget)
        self.analogevent_type.setEditable(True)
        self.analogevent_type.setObjectName("analogevent_type")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.analogevent_type)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.analogevent_date = QtWidgets.QLineEdit(self.layoutWidget)
        self.analogevent_date.setText("")
        self.analogevent_date.setObjectName("analogevent_date")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.analogevent_date)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.analogevent_details = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.analogevent_details.setObjectName("analogevent_details")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.analogevent_details)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.analogevent_agent = QtWidgets.QComboBox(self.layoutWidget)
        self.analogevent_agent.setObjectName("analogevent_agent")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.analogevent_agent)
        self.verticalLayout.addLayout(self.formLayout_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AnalogpremisInputbox)
        self.buttonBox.accepted.connect(AnalogpremisInputbox.accept)
        self.buttonBox.rejected.connect(AnalogpremisInputbox.reject)
        QtCore.QMetaObject.connectSlotsByName(AnalogpremisInputbox)

    def retranslateUi(self, AnalogpremisInputbox):
        _translate = QtCore.QCoreApplication.translate
        AnalogpremisInputbox.setWindowTitle(_translate("AnalogpremisInputbox", "Dialog"))
        self.label_4.setText(_translate("AnalogpremisInputbox", "Event type:"))
        self.label_2.setText(_translate("AnalogpremisInputbox", "Date:"))
        self.label_3.setText(_translate("AnalogpremisInputbox", "Details:"))
        self.label_5.setText(_translate("AnalogpremisInputbox", "Agent:"))

