# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flying_tracker_dialog_base.ui'
#
# Created: Mon Nov 23 14:32:51 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(939, 969)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        DockWidget.setFont(font)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButtonConnect = QtGui.QPushButton(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonConnect.setFont(font)
        self.pushButtonConnect.setObjectName(_fromUtf8("pushButtonConnect"))
        self.horizontalLayout.addWidget(self.pushButtonConnect)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.course_comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.course_comboBox.setObjectName(_fromUtf8("course_comboBox"))
        self.horizontalLayout_5.addWidget(self.course_comboBox)
        self.LoadtoolButton = QtGui.QToolButton(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.LoadtoolButton.setFont(font)
        self.LoadtoolButton.setStyleSheet(_fromUtf8(""))
        self.LoadtoolButton.setObjectName(_fromUtf8("LoadtoolButton"))
        self.horizontalLayout_5.addWidget(self.LoadtoolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.fixedHeightspinBox = QtGui.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fixedHeightspinBox.setFont(font)
        self.fixedHeightspinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.fixedHeightspinBox.setMaximum(10000)
        self.fixedHeightspinBox.setSingleStep(1)
        self.fixedHeightspinBox.setObjectName(_fromUtf8("fixedHeightspinBox"))
        self.horizontalLayout_6.addWidget(self.fixedHeightspinBox)
        self.label_9 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_6.addWidget(self.label_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_10.addWidget(self.label_12)
        self.DWpt_spinBox = QtGui.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DWpt_spinBox.setFont(font)
        self.DWpt_spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.DWpt_spinBox.setMaximum(10000)
        self.DWpt_spinBox.setSingleStep(1)
        self.DWpt_spinBox.setProperty("value", 35)
        self.DWpt_spinBox.setObjectName(_fromUtf8("DWpt_spinBox"))
        self.horizontalLayout_10.addWidget(self.DWpt_spinBox)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_10)
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_15.addWidget(self.label_17)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_13.addWidget(self.label_14)
        self.DCompass_spinBox = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DCompass_spinBox.setFont(font)
        self.DCompass_spinBox.setProperty("value", 2.0)
        self.DCompass_spinBox.setObjectName(_fromUtf8("DCompass_spinBox"))
        self.horizontalLayout_13.addWidget(self.DCompass_spinBox)
        self.label_18 = QtGui.QLabel(self.groupBox)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_13.addWidget(self.label_18)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_12.addWidget(self.label_15)
        self.DTrack_spinBox = QtGui.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DTrack_spinBox.setFont(font)
        self.DTrack_spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.DTrack_spinBox.setMaximum(10000)
        self.DTrack_spinBox.setSingleStep(1)
        self.DTrack_spinBox.setProperty("value", 10)
        self.DTrack_spinBox.setObjectName(_fromUtf8("DTrack_spinBox"))
        self.horizontalLayout_12.addWidget(self.DTrack_spinBox)
        self.label_20 = QtGui.QLabel(self.groupBox)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_12.addWidget(self.label_20)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_12)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_14.addWidget(self.label_16)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.DHeightspinBox = QtGui.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DHeightspinBox.setFont(font)
        self.DHeightspinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.DHeightspinBox.setMaximum(10000)
        self.DHeightspinBox.setSingleStep(1)
        self.DHeightspinBox.setProperty("value", 5)
        self.DHeightspinBox.setObjectName(_fromUtf8("DHeightspinBox"))
        self.horizontalLayout_14.addWidget(self.DHeightspinBox)
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_14.addWidget(self.label_19)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_2.addWidget(self.checkBox)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_10 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_9.addWidget(self.label_10)
        self.GpsFixlcdNumber = QtGui.QLCDNumber(self.dockWidgetContents)
        self.GpsFixlcdNumber.setObjectName(_fromUtf8("GpsFixlcdNumber"))
        self.horizontalLayout_9.addWidget(self.GpsFixlcdNumber)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.label_11 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_9.addWidget(self.label_11)
        self.SatelliteslcdNumber = QtGui.QLCDNumber(self.dockWidgetContents)
        self.SatelliteslcdNumber.setStyleSheet(_fromUtf8(""))
        self.SatelliteslcdNumber.setObjectName(_fromUtf8("SatelliteslcdNumber"))
        self.horizontalLayout_9.addWidget(self.SatelliteslcdNumber)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.label_13 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_11.addWidget(self.label_13)
        self.ZoomOuttoolButton = QtGui.QToolButton(self.dockWidgetContents)
        self.ZoomOuttoolButton.setObjectName(_fromUtf8("ZoomOuttoolButton"))
        self.horizontalLayout_11.addWidget(self.ZoomOuttoolButton)
        self.ZoomIntoolButton = QtGui.QToolButton(self.dockWidgetContents)
        self.ZoomIntoolButton.setObjectName(_fromUtf8("ZoomIntoolButton"))
        self.horizontalLayout_11.addWidget(self.ZoomIntoolButton)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_8 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lcdNumberWpt = QtGui.QLCDNumber(self.dockWidgetContents)
        self.lcdNumberWpt.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumberWpt.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumberWpt.setObjectName(_fromUtf8("lcdNumberWpt"))
        self.horizontalLayout_8.addWidget(self.lcdNumberWpt)
        self.wptmin_toolButton = QtGui.QToolButton(self.dockWidgetContents)
        self.wptmin_toolButton.setObjectName(_fromUtf8("wptmin_toolButton"))
        self.horizontalLayout_8.addWidget(self.wptmin_toolButton)
        self.wptplus_toolButton = QtGui.QToolButton(self.dockWidgetContents)
        self.wptplus_toolButton.setObjectName(_fromUtf8("wptplus_toolButton"))
        self.horizontalLayout_8.addWidget(self.wptplus_toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lcdNumberSpeed = QtGui.QLCDNumber(self.dockWidgetContents)
        self.lcdNumberSpeed.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumberSpeed.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumberSpeed.setObjectName(_fromUtf8("lcdNumberSpeed"))
        self.horizontalLayout_2.addWidget(self.lcdNumberSpeed)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_2 = QtGui.QComboBox(self.dockWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.lcdNumberHeights = QtGui.QLCDNumber(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lcdNumberHeights.setFont(font)
        self.lcdNumberHeights.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumberHeights.setFrameShadow(QtGui.QFrame.Raised)
        self.lcdNumberHeights.setObjectName(_fromUtf8("lcdNumberHeights"))
        self.horizontalLayout_3.addWidget(self.lcdNumberHeights)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lcdNumberCompass = QtGui.QLCDNumber(self.dockWidgetContents)
        self.lcdNumberCompass.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdNumberCompass.setObjectName(_fromUtf8("lcdNumberCompass"))
        self.horizontalLayout_4.addWidget(self.lcdNumberCompass)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lcdCompassWpt = QtGui.QLCDNumber(self.dockWidgetContents)
        self.lcdCompassWpt.setFrameShape(QtGui.QFrame.NoFrame)
        self.lcdCompassWpt.setObjectName(_fromUtf8("lcdCompassWpt"))
        self.horizontalLayout_7.addWidget(self.lcdCompassWpt)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.pushButtonDisconnect = QtGui.QPushButton(self.dockWidgetContents)
        self.pushButtonDisconnect.setObjectName(_fromUtf8("pushButtonDisconnect"))
        self.verticalLayout.addWidget(self.pushButtonDisconnect)
        self.pushCloseButton = QtGui.QPushButton(self.dockWidgetContents)
        self.pushCloseButton.setObjectName(_fromUtf8("pushCloseButton"))
        self.verticalLayout.addWidget(self.pushCloseButton)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.hide)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.comboBox.hide)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonConnect.hide)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label.show)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.comboBox.show)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonConnect.show)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushCloseButton.hide)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushCloseButton.show)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.course_comboBox.hide)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_5.hide)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_5.show)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.course_comboBox.show)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LoadtoolButton.hide)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.LoadtoolButton.show)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_6.hide)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fixedHeightspinBox.hide)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_9.hide)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_6.show)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.fixedHeightspinBox.show)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_9.show)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonDisconnect.show)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonDisconnect.hide)
        QtCore.QObject.connect(self.pushButtonConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.groupBox.hide)
        QtCore.QObject.connect(self.pushButtonDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.groupBox.show)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.label_2.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lcdNumberSpeed.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.label_3.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.comboBox_2.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lcdNumberHeights.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.label_4.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lcdNumberCompass.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.label_7.setShown)
        QtCore.QObject.connect(self.checkBox, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.lcdCompassWpt.setShown)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "Flying Tracker", None))
        self.label.setText(_translate("DockWidget", "Port:", None))
        self.pushButtonConnect.setText(_translate("DockWidget", "Connect", None))
        self.label_5.setText(_translate("DockWidget", "Track shapefile", None))
        self.LoadtoolButton.setText(_translate("DockWidget", "Load", None))
        self.groupBox.setTitle(_translate("DockWidget", "Flight Settings:", None))
        self.label_6.setText(_translate("DockWidget", "Fixed altitude:", None))
        self.label_9.setText(_translate("DockWidget", "m", None))
        self.label_12.setText(_translate("DockWidget", "Distance from Wpt:", None))
        self.label_17.setText(_translate("DockWidget", "m", None))
        self.label_14.setText(_translate("DockWidget", "Compass from Wpt:", None))
        self.label_18.setText(_translate("DockWidget", "°", None))
        self.label_15.setText(_translate("DockWidget", "Distance from Track:", None))
        self.label_20.setText(_translate("DockWidget", "m", None))
        self.label_16.setText(_translate("DockWidget", "Distance from fixed altitude:", None))
        self.label_19.setText(_translate("DockWidget", "m", None))
        self.checkBox.setText(_translate("DockWidget", "Display telemetry data", None))
        self.label_10.setText(_translate("DockWidget", "GpsFix:", None))
        self.label_11.setText(_translate("DockWidget", "Satellites:", None))
        self.label_13.setText(_translate("DockWidget", "Zoom", None))
        self.ZoomOuttoolButton.setText(_translate("DockWidget", "-", None))
        self.ZoomIntoolButton.setText(_translate("DockWidget", "+", None))
        self.label_8.setText(_translate("DockWidget", "Wpt:", None))
        self.wptmin_toolButton.setText(_translate("DockWidget", "-", None))
        self.wptplus_toolButton.setText(_translate("DockWidget", "+", None))
        self.label_2.setText(_translate("DockWidget", "Speed (km/h):", None))
        self.label_3.setText(_translate("DockWidget", "Altitude above MSL in ", None))
        self.comboBox_2.setItemText(0, _translate("DockWidget", "m.", None))
        self.comboBox_2.setItemText(1, _translate("DockWidget", "ft.", None))
        self.label_4.setText(_translate("DockWidget", "Compass:", None))
        self.label_7.setText(_translate("DockWidget", "Compass to wpt:", None))
        self.pushButtonDisconnect.setText(_translate("DockWidget", "Disconnect", None))
        self.pushCloseButton.setText(_translate("DockWidget", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DockWidget = QtGui.QDockWidget()
    ui = Ui_DockWidget()
    ui.setupUi(DockWidget)
    DockWidget.show()
    sys.exit(app.exec_())

