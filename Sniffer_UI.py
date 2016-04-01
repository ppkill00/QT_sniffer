# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sniffer.ui'
#
# Created: Wed Nov 25 16:13:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Sniffer(object):
    def setupUi(self, Sniffer):
        Sniffer.setObjectName("Sniffer")
        Sniffer.resize(899, 481)
        self.Sniff_Text_1 = QtGui.QPlainTextEdit(Sniffer)
        self.Sniff_Text_1.setGeometry(QtCore.QRect(10, 10, 281, 411))
        self.Sniff_Text_1.setObjectName("Sniff_Text_1")
        self.Sniff_But_1 = QtGui.QPushButton(Sniffer)
        self.Sniff_But_1.setGeometry(QtCore.QRect(10, 426, 841, 41))
        self.Sniff_But_1.setObjectName("Sniff_But_1")
        self.TableSrc = QtGui.QTableView(Sniffer)
        self.TableSrc.setGeometry(QtCore.QRect(460, 10, 211, 411))
        self.TableSrc.setObjectName("TableSrc")
        self.TableDst = QtGui.QTableView(Sniffer)
        self.TableDst.setGeometry(QtCore.QRect(680, 10, 211, 411))
        self.TableDst.setObjectName("TableDst")
        self.TableProto = QtGui.QTableView(Sniffer)
        self.TableProto.setGeometry(QtCore.QRect(300, 10, 151, 411))
        self.TableProto.setObjectName("TableProto")

        self.retranslateUi(Sniffer)
        QtCore.QMetaObject.connectSlotsByName(Sniffer)

    def retranslateUi(self, Sniffer):
        Sniffer.setWindowTitle(QtGui.QApplication.translate("Sniffer", "Sniffer", None, QtGui.QApplication.UnicodeUTF8))
        self.Sniff_But_1.setText(QtGui.QApplication.translate("Sniffer", "Start", None, QtGui.QApplication.UnicodeUTF8))

