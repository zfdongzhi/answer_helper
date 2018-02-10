#!/usr/bin/python
# -*- coding: utf-8 -*-
# author:Zhai-Fan
# mail: zfneutrino@gmail.com


from __future__ import division
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtGui import QIcon
import sys
import Size
import Demo
from ocr import baidu_ocr
from search import baidu_search
from im_cap import im_cap_adb, im_cap_pc


def show_size_window():
    global size_window_flag
    if size_window_flag:
        size_window.close()
    else:
        size_window.show()
    size_window_flag = ~size_window_flag


def find_answer():
    global debug, index, browser_flag, app_name, more_search
    global cb_more_search, cb_debug, cb_browser, app_box, ans_box
    more_search = cb_more_search.checkState()
    debug = cb_debug.checkState()
    phone_flag = cb_phone.checkState()
    if app_box.currentIndex() == 0:
        app_name = 'Toutiao'
    elif app_box.currentIndex() == 1:
        app_name = 'Chongding'
    elif app_box.currentIndex() == 2:
        app_name = 'Zhishi'
    elif app_box.currentIndex() == 3:
        app_name = 'Taobao'
    else:
        app_name = 'default'
    if phone_flag:
        im_cap_adb(app_name)
    else:
        im_cap_pc(app_name)
    question, options = baidu_ocr(debug)
    if app_name != 'Zhishi' and app_name != 'default':
        head = 0
        tail = len(question)
        while question[head] > '0' < '9' and head < tail:
            head = head + 1
        if question[head] == '.':
            head = head + 1
        question = question[head:]
    answer = baidu_search(question, options, browser_flag, more_search)
    ans_box.setPlainText(answer)


if __name__ == '__main__':
    debug = 1
    index = 1
    browser_flag = 1
    more_search = 0
    app_name = 'default'
    size_window_flag = 0
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui_demo = Demo.Ui_MainWindow()
    ui_demo.setupUi(main_window)
    main_window.setWindowIcon(QIcon('ui\icon.png'))
    main_window.setFixedSize(main_window.width(), main_window.height())
    main_window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    main_window.show()
    size_button = ui_demo.pushButton
    size_button.clicked.connect(show_size_window)
    answer_button = ui_demo.commandLinkButton
    answer_button.clicked.connect(find_answer)
    cb_more_search = ui_demo.checkBox
    cb_debug = ui_demo.checkBox_2
    cb_browser = ui_demo.checkBox_3
    cb_phone = ui_demo.checkBox_4
    app_box = ui_demo.comboBox
    ans_box = ui_demo.textEdit
    size_window = QDialog()
    ui_size = Size.Ui_Form()
    ui_size.setupUi(size_window)
    size_window.setFixedSize(size_window.width(), size_window.height())
    size_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    size_window.setWindowIcon(QIcon('ui\icon.png'))
    size_window.setGeometry(0, 35, 355, 625)
    sys.exit(app.exec_())
