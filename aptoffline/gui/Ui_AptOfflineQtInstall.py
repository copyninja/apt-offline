# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AptOfflineQtInstall.ui'
#
# Created: Sat Sep 13 15:37:48 2014
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_AptOfflineQtInstall(object):
    def setupUi(self, AptOfflineQtInstall):
        AptOfflineQtInstall.setObjectName(_fromUtf8("AptOfflineQtInstall"))
        AptOfflineQtInstall.setWindowModality(QtCore.Qt.ApplicationModal)
        AptOfflineQtInstall.resize(466, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AptOfflineQtInstall.sizePolicy().hasHeightForWidth())
        AptOfflineQtInstall.setSizePolicy(sizePolicy)
        AptOfflineQtInstall.setMinimumSize(QtCore.QSize(466, 400))
        AptOfflineQtInstall.setMaximumSize(QtCore.QSize(466, 400))
        self.zipFilePath = QtGui.QLineEdit(AptOfflineQtInstall)
        self.zipFilePath.setGeometry(QtCore.QRect(30, 32, 270, 30))
        self.zipFilePath.setObjectName(_fromUtf8("zipFilePath"))
        self.browseFilePathButton = QtGui.QPushButton(AptOfflineQtInstall)
        self.browseFilePathButton.setGeometry(QtCore.QRect(320, 32, 110, 30))
        self.browseFilePathButton.setObjectName(_fromUtf8("browseFilePathButton"))
        self.startInstallButton = QtGui.QPushButton(AptOfflineQtInstall)
        self.startInstallButton.setEnabled(False)
        self.startInstallButton.setGeometry(QtCore.QRect(31, 75, 130, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/dialog-ok-apply.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startInstallButton.setIcon(icon)
        self.startInstallButton.setObjectName(_fromUtf8("startInstallButton"))
        self.cancelButton = QtGui.QPushButton(AptOfflineQtInstall)
        self.cancelButton.setGeometry(QtCore.QRect(320, 75, 110, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelButton.setIcon(icon1)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.statusProgressBar = QtGui.QProgressBar(AptOfflineQtInstall)
        self.statusProgressBar.setGeometry(QtCore.QRect(30, 146, 410, 20))
        self.statusProgressBar.setProperty("value", 0)
        self.statusProgressBar.setObjectName(_fromUtf8("statusProgressBar"))
        self.label = QtGui.QLabel(AptOfflineQtInstall)
        self.label.setGeometry(QtCore.QRect(30, 2, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(AptOfflineQtInstall)
        self.label_2.setGeometry(QtCore.QRect(34, 120, 70, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.progressStatusDescription = QtGui.QLabel(AptOfflineQtInstall)
        self.progressStatusDescription.setGeometry(QtCore.QRect(90, 120, 53, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressStatusDescription.setFont(font)
        self.progressStatusDescription.setObjectName(_fromUtf8("progressStatusDescription"))
        self.rawLogHolder = QtGui.QTextEdit(AptOfflineQtInstall)
        self.rawLogHolder.setGeometry(QtCore.QRect(30, 180, 411, 191))
        self.rawLogHolder.setTabChangesFocus(True)
        self.rawLogHolder.setUndoRedoEnabled(False)
        self.rawLogHolder.setReadOnly(True)
        self.rawLogHolder.setAcceptRichText(False)
        self.rawLogHolder.setObjectName(_fromUtf8("rawLogHolder"))
        self.bugReportsButton = QtGui.QPushButton(AptOfflineQtInstall)
        self.bugReportsButton.setEnabled(False)
        self.bugReportsButton.setGeometry(QtCore.QRect(172, 75, 130, 30))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/help-about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bugReportsButton.setIcon(icon2)
        self.bugReportsButton.setObjectName(_fromUtf8("bugReportsButton"))
        self.browseFileFoldercheckBox = QtGui.QCheckBox(AptOfflineQtInstall)
        self.browseFileFoldercheckBox.setGeometry(QtCore.QRect(322, 10, 101, 18))
        self.browseFileFoldercheckBox.setObjectName(_fromUtf8("browseFileFoldercheckBox"))

        self.retranslateUi(AptOfflineQtInstall)
        QtCore.QMetaObject.connectSlotsByName(AptOfflineQtInstall)

    def retranslateUi(self, AptOfflineQtInstall):
        AptOfflineQtInstall.setWindowTitle(_translate("AptOfflineQtInstall", "Install Packages", None))
        self.browseFilePathButton.setText(_translate("AptOfflineQtInstall", "Browse", None))
        self.startInstallButton.setText(_translate("AptOfflineQtInstall", "Install", None))
        self.cancelButton.setText(_translate("AptOfflineQtInstall", "Close", None))
        self.label.setText(_translate("AptOfflineQtInstall", "Specify file or folder path", None))
        self.label_2.setText(_translate("AptOfflineQtInstall", "Status:", None))
        self.progressStatusDescription.setText(_translate("AptOfflineQtInstall", "Ready", None))
        self.bugReportsButton.setText(_translate("AptOfflineQtInstall", "Bug Reports", None))
        self.browseFileFoldercheckBox.setText(_translate("AptOfflineQtInstall", "Is Directory", None))

import resources_rc
