# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/noise_patch_dialog.ui'
#
# Created: Tue Apr  9 17:37:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_noise_patch_dialog(object):
    def setupUi(self, noise_patch_dialog):
        noise_patch_dialog.setObjectName(_fromUtf8("noise_patch_dialog"))
        noise_patch_dialog.resize(476, 384)
        self.verticalLayout = QtGui.QVBoxLayout(noise_patch_dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_header_box = QtGui.QWidget(noise_patch_dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_header_box.sizePolicy().hasHeightForWidth())
        self.widget_header_box.setSizePolicy(sizePolicy)
        self.widget_header_box.setObjectName(_fromUtf8("widget_header_box"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_header_box)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_noise_patch = QtGui.QLabel(self.widget_header_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_noise_patch.sizePolicy().hasHeightForWidth())
        self.label_noise_patch.setSizePolicy(sizePolicy)
        self.label_noise_patch.setText(_fromUtf8(""))
        self.label_noise_patch.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/noise_patch.png")))
        self.label_noise_patch.setObjectName(_fromUtf8("label_noise_patch"))
        self.horizontalLayout.addWidget(self.label_noise_patch)
        self.label_2 = QtGui.QLabel(self.widget_header_box)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.widget_header_box)
        self.widget = QtGui.QWidget(noise_patch_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.widget.setFont(font)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.spin_size = QtGui.QSpinBox(self.widget)
        self.spin_size.setMinimum(1)
        self.spin_size.setMaximum(1000)
        self.spin_size.setProperty("value", 96)
        self.spin_size.setObjectName(_fromUtf8("spin_size"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spin_size)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.combobox_env = QtGui.QComboBox(self.widget)
        self.combobox_env.setObjectName(_fromUtf8("combobox_env"))
        self.combobox_env.addItem(_fromUtf8(""))
        self.combobox_env.addItem(_fromUtf8(""))
        self.combobox_env.addItem(_fromUtf8(""))
        self.combobox_env.addItem(_fromUtf8(""))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.combobox_env)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.spin_stdev = QtGui.QDoubleSpinBox(self.widget)
        self.spin_stdev.setMaximum(1000.0)
        self.spin_stdev.setProperty("value", 12.0)
        self.spin_stdev.setObjectName(_fromUtf8("spin_stdev"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spin_stdev)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_10)
        self.edit_color1 = QtGui.QLineEdit(self.widget)
        self.edit_color1.setText(_fromUtf8("white"))
        self.edit_color1.setObjectName(_fromUtf8("edit_color1"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.edit_color1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.edit_color2 = QtGui.QLineEdit(self.widget)
        self.edit_color2.setText(_fromUtf8("black"))
        self.edit_color2.setObjectName(_fromUtf8("edit_color2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.edit_color2)
        self.label_11 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_11)
        self.combobox_bgmode = QtGui.QComboBox(self.widget)
        self.combobox_bgmode.setObjectName(_fromUtf8("combobox_bgmode"))
        self.combobox_bgmode.addItem(_fromUtf8(""))
        self.combobox_bgmode.addItem(_fromUtf8(""))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.combobox_bgmode)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtGui.QWidget(noise_patch_dialog)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_12 = QtGui.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_2.addWidget(self.label_12)
        self.verticalLayout.addWidget(self.widget_3)
        self.buttonBox = QtGui.QDialogButtonBox(noise_patch_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(noise_patch_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), noise_patch_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), noise_patch_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(noise_patch_dialog)

    def retranslateUi(self, noise_patch_dialog):
        noise_patch_dialog.setWindowTitle(QtGui.QApplication.translate("noise_patch_dialog", "Insert noise patch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("noise_patch_dialog", "Insert noise patch", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_size.setSuffix(QtGui.QApplication.translate("noise_patch_dialog", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("noise_patch_dialog", "Envelope", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_env.setItemText(0, QtGui.QApplication.translate("noise_patch_dialog", "gaussian", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_env.setItemText(1, QtGui.QApplication.translate("noise_patch_dialog", "linear", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_env.setItemText(2, QtGui.QApplication.translate("noise_patch_dialog", "circular (sharp edge)", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_env.setItemText(3, QtGui.QApplication.translate("noise_patch_dialog", "rectangle (no envelope)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("noise_patch_dialog", "Standard deviation<br /><i>in pixels, only applies to Gaussian envelope</i>", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_stdev.setSuffix(QtGui.QApplication.translate("noise_patch_dialog", "px", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("noise_patch_dialog", "Color 1<br /><i>e.g., \'white\' or \'#FFFFFF\'</i>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("noise_patch_dialog", "Color 2<br /><i>e.g., \'black\' or \'#000000\'</i>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("noise_patch_dialog", "Background color *", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_bgmode.setItemText(0, QtGui.QApplication.translate("noise_patch_dialog", "Color average", None, QtGui.QApplication.UnicodeUTF8))
        self.combobox_bgmode.setItemText(1, QtGui.QApplication.translate("noise_patch_dialog", "Color 2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("noise_patch_dialog", "Size<br /><i>in pixels</i>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("noise_patch_dialog", "* Has no effect in psycho back-end", None, QtGui.QApplication.UnicodeUTF8))

