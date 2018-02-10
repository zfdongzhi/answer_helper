# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demo.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 321)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 301, 131))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 50, 71, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(170, 50, 141, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 140, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 120, 151, 41))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 20, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 110, 111, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "答题小程序"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">说明：</span></p><p><span style=\" font-size:10pt;\">1、运行手机模拟器，将答题直播放在识别范围中</span></p><p><span style=\" font-size:10pt;\">或者连接Android手机，打开USB调试</span></p><p><span style=\" font-size:10pt;\">2、选择对应的答题平台</span></p><p><span style=\" font-size:10pt;\">3、题目出现时点击搜索</span></p></body></html>"))
        self.checkBox.setText(_translate("MainWindow", "高级搜索"))
        self.checkBox_2.setText(_translate("MainWindow", "记录题目"))
        self.checkBox_3.setText(_translate("MainWindow", "自动打开浏览器"))
        self.commandLinkButton.setText(_translate("MainWindow", "搜索"))
        self.comboBox.setItemText(0, _translate("MainWindow", "百万英雄"))
        self.comboBox.setItemText(1, _translate("MainWindow", "冲顶大会"))
        self.comboBox.setItemText(2, _translate("MainWindow", "芝士超人"))
        self.comboBox.setItemText(3, _translate("MainWindow", "淘宝"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">参考答案：</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffaa00;\">准备查询...</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "查看识别范围"))
        self.checkBox_4.setText(_translate("MainWindow", "连接手机"))

