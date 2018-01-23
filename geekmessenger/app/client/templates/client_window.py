# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'geekmessenger\app\client\templates\client_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_client_window(object):
    def setupUi(self, client_window):
        client_window.setObjectName("client_window")
        client_window.resize(648, 600)
        self.messanger_window = QtWidgets.QWidget(client_window)
        self.messanger_window.setMinimumSize(QtCore.QSize(648, 600))
        self.messanger_window.setObjectName("messanger_window")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.messanger_window)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dialogs_list = QtWidgets.QListWidget(self.messanger_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialogs_list.sizePolicy().hasHeightForWidth())
        self.dialogs_list.setSizePolicy(sizePolicy)
        self.dialogs_list.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dialogs_list.setLineWidth(1)
        self.dialogs_list.setObjectName("dialogs_list")
        self.horizontalLayout_2.addWidget(self.dialogs_list)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.messanges_list = QtWidgets.QListWidget(self.messanger_window)
        self.messanges_list.setLineWidth(2)
        self.messanges_list.setObjectName("messanges_list")
        self.verticalLayout.addWidget(self.messanges_list)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messanger_edit = QtWidgets.QTextEdit(self.messanger_window)
        self.messanger_edit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.messanger_edit.setObjectName("messanger_edit")
        self.horizontalLayout.addWidget(self.messanger_edit)
        self.send_button = QtWidgets.QPushButton(self.messanger_window)
        self.send_button.setMinimumSize(QtCore.QSize(50, 0))
        self.send_button.setMaximumSize(QtCore.QSize(16777215, 50))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_button.setIcon(icon)
        self.send_button.setObjectName("send_button")
        self.horizontalLayout.addWidget(self.send_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        client_window.setCentralWidget(self.messanger_window)
        self.actionsend = QtWidgets.QAction(client_window)
        self.actionsend.setIcon(icon)
        self.actionsend.setObjectName("actionsend")

        self.retranslateUi(client_window)
        QtCore.QMetaObject.connectSlotsByName(client_window)

    def retranslateUi(self, client_window):
        _translate = QtCore.QCoreApplication.translate
        client_window.setWindowTitle(_translate("client_window", "Messanger Client"))
        self.send_button.setText(_translate("client_window", "Отправить"))
        self.actionsend.setText(_translate("client_window", "send"))
