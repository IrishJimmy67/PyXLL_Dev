# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HTC_Proposal1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 357)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 320, 91, 23))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 80, 361, 231))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.proposalNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.proposalNameLabel.setObjectName("proposalNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.proposalNameLabel)
        self.proposalNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.proposalNameLineEdit.setObjectName("proposalNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.proposalNameLineEdit)
        self.totalInvestmentLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.totalInvestmentLabel.setObjectName("totalInvestmentLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.totalInvestmentLabel)
        self.totalInvestmentLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.totalInvestmentLineEdit.setObjectName("totalInvestmentLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.totalInvestmentLineEdit)
        self.cashLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cashLabel.setObjectName("cashLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.cashLabel)
        self.cashLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cashLineEdit.setObjectName("cashLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cashLineEdit)
        self.equityPercentageLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.equityPercentageLabel.setObjectName("equityPercentageLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.equityPercentageLabel)
        self.equityPercentageLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.equityPercentageLineEdit.setObjectName("equityPercentageLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.equityPercentageLineEdit)
        self.fixedIncomePercentageLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.fixedIncomePercentageLabel.setObjectName("fixedIncomePercentageLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fixedIncomePercentageLabel)
        self.fixedIncomePercentageLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fixedIncomePercentageLineEdit.setObjectName("fixedIncomePercentageLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fixedIncomePercentageLineEdit)
        self.cashOverrideLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.cashOverrideLabel.setObjectName("cashOverrideLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.cashOverrideLabel)
        self.cashOverrideLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.cashOverrideLineEdit.setObjectName("cashOverrideLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cashOverrideLineEdit)
        self.equityModelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.equityModelLabel.setObjectName("equityModelLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.equityModelLabel)
        self.equityModelComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.equityModelComboBox.setObjectName("equityModelComboBox")
        self.equityModelComboBox.addItem("")
        self.equityModelComboBox.addItem("")
        self.equityModelComboBox.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.equityModelComboBox)
        self.fixedModelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.fixedModelLabel.setObjectName("fixedModelLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.fixedModelLabel)
        self.fixedModelComboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.fixedModelComboBox.setObjectName("fixedModelComboBox")
        self.fixedModelComboBox.addItem("")
        self.fixedModelComboBox.addItem("")
        self.fixedModelComboBox.addItem("")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.fixedModelComboBox)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(26, 20, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Portfolio Proposal"))
        self.pushButton.setText(_translate("Form", "Create Proposal"))
        self.proposalNameLabel.setText(_translate("Form", "Proposal Name"))
        self.totalInvestmentLabel.setText(_translate("Form", "Total Investment"))
        self.cashLabel.setText(_translate("Form", "Cash Percentage"))
        self.equityPercentageLabel.setText(_translate("Form", "Equity Percentage"))
        self.fixedIncomePercentageLabel.setText(_translate("Form", "Fixed Income Percentage"))
        self.cashOverrideLabel.setText(_translate("Form", "Cash Override"))
        # geek list
        geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
        self.equityModelLabel.setText(_translate("Form", "Equity Model"))
        self.equityModelComboBox.setItemText(0, _translate("Form", "EQT Model 1"))
        self.equityModelComboBox.setItemText(1, _translate("Form", "EQT Model 2"))
        self.equityModelComboBox.setItemText(2, _translate("Form", "EQT Model 3"))
        self.equityModelComboBox.addItems(geek_list)
        self.fixedModelLabel.setText(_translate("Form", "Fixed Model"))
        self.fixedModelComboBox.setItemText(0, _translate("Form", "FIX Model 1"))
        self.fixedModelComboBox.setItemText(1, _translate("Form", "FIX Model 2"))
        self.fixedModelComboBox.setItemText(2, _translate("Form", "FIX Model 3"))

        self.label.setText(_translate("Form", "Haverford Proposal System"))

    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()

        else:
            self.w.close()  # Close window.
            self.w = None  # Discard reference.


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
