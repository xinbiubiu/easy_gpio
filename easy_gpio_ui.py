# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easy_gpio_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(289, 272)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 61, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_bank0 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.button_bank0.setObjectName("button_bank0")
        self.verticalLayout.addWidget(self.button_bank0)
        self.button_bank1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.button_bank1.setObjectName("button_bank1")
        self.verticalLayout.addWidget(self.button_bank1)
        self.button_bank2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.button_bank2.setObjectName("button_bank2")
        self.verticalLayout.addWidget(self.button_bank2)
        self.button_bank3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.button_bank3.setObjectName("button_bank3")
        self.verticalLayout.addWidget(self.button_bank3)
        self.button_bank4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.button_bank4.setObjectName("button_bank4")
        self.verticalLayout.addWidget(self.button_bank4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 60, 31, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_groupA = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.button_groupA.setObjectName("button_groupA")
        self.verticalLayout_2.addWidget(self.button_groupA)
        self.button_groupB = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.button_groupB.setObjectName("button_groupB")
        self.verticalLayout_2.addWidget(self.button_groupB)
        self.button_groupC = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.button_groupC.setObjectName("button_groupC")
        self.verticalLayout_2.addWidget(self.button_groupC)
        self.button_groupD = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.button_groupD.setObjectName("button_groupD")
        self.verticalLayout_2.addWidget(self.button_groupD)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(150, 60, 31, 172))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.button_pin0 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin0.setObjectName("button_pin0")
        self.verticalLayout_3.addWidget(self.button_pin0)
        self.button_pin1 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin1.setObjectName("button_pin1")
        self.verticalLayout_3.addWidget(self.button_pin1)
        self.button_pin2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin2.setObjectName("button_pin2")
        self.verticalLayout_3.addWidget(self.button_pin2)
        self.button_pin3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin3.setObjectName("button_pin3")
        self.verticalLayout_3.addWidget(self.button_pin3)
        self.button_pin4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin4.setObjectName("button_pin4")
        self.verticalLayout_3.addWidget(self.button_pin4)
        self.button_pin5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin5.setObjectName("button_pin5")
        self.verticalLayout_3.addWidget(self.button_pin5)
        self.button_pin6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin6.setObjectName("button_pin6")
        self.verticalLayout_3.addWidget(self.button_pin6)
        self.button_pin7 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.button_pin7.setObjectName("button_pin7")
        self.verticalLayout_3.addWidget(self.button_pin7)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 130, 71, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_value0 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.button_value0.setObjectName("button_value0")
        self.horizontalLayout.addWidget(self.button_value0)
        self.button_value1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.button_value1.setObjectName("button_value1")
        self.horizontalLayout.addWidget(self.button_value1)
        self.text_out = QtWidgets.QLineEdit(self.centralwidget)
        self.text_out.setGeometry(QtCore.QRect(40, 20, 200, 20))
        self.text_out.setObjectName("text_out")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy GPIO"))
        self.button_bank0.setText(_translate("MainWindow", "GPIO0"))
        self.button_bank1.setText(_translate("MainWindow", "GPIO1"))
        self.button_bank2.setText(_translate("MainWindow", "GPIO2"))
        self.button_bank3.setText(_translate("MainWindow", "GPIO3"))
        self.button_bank4.setText(_translate("MainWindow", "GPIO4"))
        self.button_groupA.setText(_translate("MainWindow", "A"))
        self.button_groupB.setText(_translate("MainWindow", "B"))
        self.button_groupC.setText(_translate("MainWindow", "C"))
        self.button_groupD.setText(_translate("MainWindow", "D"))
        self.button_pin0.setText(_translate("MainWindow", "0"))
        self.button_pin1.setText(_translate("MainWindow", "1"))
        self.button_pin2.setText(_translate("MainWindow", "2"))
        self.button_pin3.setText(_translate("MainWindow", "3"))
        self.button_pin4.setText(_translate("MainWindow", "4"))
        self.button_pin5.setText(_translate("MainWindow", "5"))
        self.button_pin6.setText(_translate("MainWindow", "6"))
        self.button_pin7.setText(_translate("MainWindow", "7"))
        self.button_value0.setText(_translate("MainWindow", "0"))
        self.button_value1.setText(_translate("MainWindow", "1"))
