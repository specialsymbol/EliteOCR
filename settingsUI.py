# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsUI.ui'
#
<<<<<<< HEAD
# Created: Fri Jan 16 17:36:24 2015
=======
# Created: Wed Dec 31 06:50:50 2014
>>>>>>> origin/dev
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

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.setEnabled(True)
        Settings.resize(592, 262)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/ico/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Settings.setWindowIcon(icon)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Settings)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(Settings)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ui_language = QtGui.QComboBox(self.tab)
        self.ui_language.setObjectName(_fromUtf8("ui_language"))
        self.horizontalLayout_4.addWidget(self.ui_language)
<<<<<<< HEAD
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.ocr_language = QtGui.QComboBox(self.tab)
        self.ocr_language.setEnabled(True)
=======
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.ocr_language = QtGui.QComboBox(self.tab)
>>>>>>> origin/dev
        self.ocr_language.setObjectName(_fromUtf8("ocr_language"))
        self.horizontalLayout_4.addWidget(self.ocr_language)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
<<<<<<< HEAD
        self.translate_results = QtGui.QCheckBox(self.tab)
        self.translate_results.setObjectName(_fromUtf8("translate_results"))
        self.verticalLayout_2.addWidget(self.translate_results)
=======
>>>>>>> origin/dev
        self.auto_fill = QtGui.QCheckBox(self.tab)
        self.auto_fill.setObjectName(_fromUtf8("auto_fill"))
        self.verticalLayout_2.addWidget(self.auto_fill)
        self.remove_dupli = QtGui.QCheckBox(self.tab)
        self.remove_dupli.setObjectName(_fromUtf8("remove_dupli"))
        self.verticalLayout_2.addWidget(self.remove_dupli)
        self.pause_at_end = QtGui.QCheckBox(self.tab)
        self.pause_at_end.setChecked(False)
        self.pause_at_end.setObjectName(_fromUtf8("pause_at_end"))
        self.verticalLayout_2.addWidget(self.pause_at_end)
        self.delete_files = QtGui.QCheckBox(self.tab)
        self.delete_files.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.delete_files.setObjectName(_fromUtf8("delete_files"))
        self.verticalLayout_2.addWidget(self.delete_files)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scr_dir = QtGui.QLineEdit(self.tab_2)
        self.scr_dir.setObjectName(_fromUtf8("scr_dir"))
        self.horizontalLayout.addWidget(self.scr_dir)
        self.browse = QtGui.QPushButton(self.tab_2)
        self.browse.setObjectName(_fromUtf8("browse"))
        self.horizontalLayout.addWidget(self.browse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_2 = QtGui.QFrame(self.tab_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lg_dir = QtGui.QLineEdit(self.tab_2)
        self.lg_dir.setObjectName(_fromUtf8("lg_dir"))
        self.horizontalLayout_3.addWidget(self.lg_dir)
        self.lg_browse = QtGui.QPushButton(self.tab_2)
        self.lg_browse.setObjectName(_fromUtf8("lg_browse"))
        self.horizontalLayout_3.addWidget(self.lg_browse)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_3 = QtGui.QFrame(self.tab_2)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.exp_dir = QtGui.QLineEdit(self.tab_2)
        self.exp_dir.setObjectName(_fromUtf8("exp_dir"))
        self.horizontalLayout_2.addWidget(self.exp_dir)
        self.exp_browse = QtGui.QPushButton(self.tab_2)
        self.exp_browse.setObjectName(_fromUtf8("exp_browse"))
        self.horizontalLayout_2.addWidget(self.exp_browse)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
<<<<<<< HEAD
        self.native_dialog = QtGui.QCheckBox(self.tab_3)
        self.native_dialog.setObjectName(_fromUtf8("native_dialog"))
        self.verticalLayout_6.addWidget(self.native_dialog)
        self.horizontal_exp = QtGui.QCheckBox(self.tab_3)
        self.horizontal_exp.setObjectName(_fromUtf8("horizontal_exp"))
        self.verticalLayout_6.addWidget(self.horizontal_exp)
        self.updates_check = QtGui.QCheckBox(self.tab_3)
        self.updates_check.setObjectName(_fromUtf8("updates_check"))
        self.verticalLayout_6.addWidget(self.updates_check)
=======
        self.horizontal_exp = QtGui.QCheckBox(self.tab_3)
        self.horizontal_exp.setObjectName(_fromUtf8("horizontal_exp"))
        self.verticalLayout_6.addWidget(self.horizontal_exp)
>>>>>>> origin/dev
        self.create_nn_images = QtGui.QCheckBox(self.tab_3)
        self.create_nn_images.setChecked(False)
        self.create_nn_images.setObjectName(_fromUtf8("create_nn_images"))
        self.verticalLayout_6.addWidget(self.create_nn_images)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Settings)
        self.buttonBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Settings.reject)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(_translate("Settings", "Settings", None))
        self.label_4.setText(_translate("Settings", "Interface Language:", None))
<<<<<<< HEAD
        self.label_6.setText(_translate("Settings", "(restart required)", None))
        self.label_5.setText(_translate("Settings", "OCR Language:", None))
        self.translate_results.setText(_translate("Settings", "Translate results to english on export", None))
=======
        self.label_5.setText(_translate("Settings", "OCR Language:", None))
>>>>>>> origin/dev
        self.auto_fill.setText(_translate("Settings", "Automatically add results with high confidence to the table", None))
        self.remove_dupli.setText(_translate("Settings", "Remove duplicates in table", None))
        self.pause_at_end.setText(_translate("Settings", "Pause \"OCR All\" at the end of a file (recommended with Delete processed images)", None))
        self.delete_files.setText(_translate("Settings", "Delete processed images", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Settings", "General", None))
        self.label.setText(_translate("Settings", "Screenshot Directory:", None))
        self.browse.setText(_translate("Settings", "Browse", None))
        self.label_3.setText(_translate("Settings", "Log Directory (for system names):", None))
        self.lg_browse.setText(_translate("Settings", "Browse", None))
        self.label_2.setText(_translate("Settings", "Export Directory:", None))
        self.exp_browse.setText(_translate("Settings", "Browse", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Settings", "Paths", None))
<<<<<<< HEAD
        self.native_dialog.setText(_translate("Settings", "Use native file dialog (might ignore default paths)", None))
        self.horizontal_exp.setText(_translate("Settings", "Horizontal export", None))
        self.updates_check.setText(_translate("Settings", "Check for updates on startup", None))
=======
        self.horizontal_exp.setText(_translate("Settings", "Horizontal export", None))
>>>>>>> origin/dev
        self.create_nn_images.setText(_translate("Settings", "Save images for machine learning (not used currently)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Settings", "Misc", None))

import res_rc
