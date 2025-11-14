# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QGroupBox, QLCDNumber,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(973, 884)
        Widget.setMaximumSize(QSize(16777215, 1040))
        Widget.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.output_tabWidget_2 = QTabWidget(Widget)
        self.output_tabWidget_2.setObjectName(u"output_tabWidget_2")
        self.output_tabWidget_2.setMinimumSize(QSize(0, 140))
        font = QFont()
        font.setBold(True)
        self.output_tabWidget_2.setFont(font)
        self.output_tabWidget_2.setAutoFillBackground(False)
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_23 = QGridLayout(self.tab_10)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(3, 3, 3, 3)
        self.widget = QWidget(self.tab_10)
        self.widget.setObjectName(u"widget")
        self.gridLayout_16 = QGridLayout(self.widget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(3, 1, 3, 3)
        self.w = QLabel(self.widget)
        self.w.setObjectName(u"w")
        self.w.setFont(font)
        self.w.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.w.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.w, 0, 4, 1, 1)

        self.out_d = QLCDNumber(self.widget)
        self.out_d.setObjectName(u"out_d")
        self.out_d.setMinimumSize(QSize(100, 0))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(False)
        self.out_d.setFont(font1)
        self.out_d.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_d.setFrameShape(QFrame.StyledPanel)
        self.out_d.setFrameShadow(QFrame.Plain)
        self.out_d.setLineWidth(3)
        self.out_d.setSmallDecimalPoint(True)
        self.out_d.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_16.addWidget(self.out_d, 2, 5, 1, 1)

        self.out_n = QLCDNumber(self.widget)
        self.out_n.setObjectName(u"out_n")
        self.out_n.setMinimumSize(QSize(100, 0))
        self.out_n.setFont(font1)
        self.out_n.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_n.setFrameShape(QFrame.StyledPanel)
        self.out_n.setFrameShadow(QFrame.Plain)
        self.out_n.setLineWidth(3)
        self.out_n.setSmallDecimalPoint(True)
        self.out_n.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_16.addWidget(self.out_n, 4, 5, 1, 1)

        self.out_w = QLCDNumber(self.widget)
        self.out_w.setObjectName(u"out_w")
        self.out_w.setMinimumSize(QSize(100, 0))
        self.out_w.setFont(font1)
        self.out_w.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_w.setFrameShape(QFrame.StyledPanel)
        self.out_w.setFrameShadow(QFrame.Plain)
        self.out_w.setLineWidth(3)
        self.out_w.setSmallDecimalPoint(True)
        self.out_w.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_16.addWidget(self.out_w, 0, 5, 1, 1)

        self.out_type = QLabel(self.widget)
        self.out_type.setObjectName(u"out_type")
        self.out_type.setFont(font)
        self.out_type.setStyleSheet(u"color: rgb(255, 197, 0);")
        self.out_type.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.out_type, 4, 2, 1, 1)

        self.out_l = QLCDNumber(self.widget)
        self.out_l.setObjectName(u"out_l")
        self.out_l.setMinimumSize(QSize(100, 0))
        self.out_l.setFont(font1)
        self.out_l.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_l.setFrameShape(QFrame.StyledPanel)
        self.out_l.setFrameShadow(QFrame.Plain)
        self.out_l.setLineWidth(3)
        self.out_l.setSmallDecimalPoint(True)
        self.out_l.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_16.addWidget(self.out_l, 2, 2, 1, 1)

        self.l = QLabel(self.widget)
        self.l.setObjectName(u"l")
        self.l.setFont(font)
        self.l.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.l.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.l, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_2, 2, 6, 1, 1)

        self.label_type = QLabel(self.widget)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setFont(font)
        self.label_type.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_type.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_type, 4, 1, 1, 1)

        self.d = QLabel(self.widget)
        self.d.setObjectName(u"d")
        self.d.setFont(font)
        self.d.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.d.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.d, 2, 4, 1, 1)

        self.count = QLabel(self.widget)
        self.count.setObjectName(u"count")
        self.count.setFont(font)
        self.count.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.count.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.count, 4, 4, 1, 1)

        self.out_m = QLCDNumber(self.widget)
        self.out_m.setObjectName(u"out_m")
        self.out_m.setMinimumSize(QSize(100, 0))
        self.out_m.setFont(font1)
        self.out_m.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_m.setFrameShape(QFrame.StyledPanel)
        self.out_m.setFrameShadow(QFrame.Plain)
        self.out_m.setLineWidth(3)
        self.out_m.setSmallDecimalPoint(True)
        self.out_m.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_16.addWidget(self.out_m, 0, 2, 1, 1)

        self.m = QLabel(self.widget)
        self.m.setObjectName(u"m")
        self.m.setFont(font)
        self.m.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.m.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.m, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer, 2, 0, 1, 1)


        self.gridLayout_23.addWidget(self.widget, 0, 0, 1, 1)

        self.output_tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_24 = QGridLayout(self.tab_11)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(3, 3, 3, 3)
        self.widget_2 = QWidget(self.tab_11)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_29 = QGridLayout(self.widget_2)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(3, 1, 3, 3)
        self.out_d_3 = QLCDNumber(self.widget_2)
        self.out_d_3.setObjectName(u"out_d_3")
        self.out_d_3.setMinimumSize(QSize(100, 0))
        self.out_d_3.setFont(font1)
        self.out_d_3.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_d_3.setFrameShape(QFrame.StyledPanel)
        self.out_d_3.setFrameShadow(QFrame.Plain)
        self.out_d_3.setLineWidth(3)
        self.out_d_3.setSmallDecimalPoint(True)
        self.out_d_3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_29.addWidget(self.out_d_3, 2, 5, 1, 1)

        self.w_3 = QLabel(self.widget_2)
        self.w_3.setObjectName(u"w_3")
        self.w_3.setFont(font)
        self.w_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.w_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.w_3, 0, 4, 1, 1)

        self.out_m_3 = QLCDNumber(self.widget_2)
        self.out_m_3.setObjectName(u"out_m_3")
        self.out_m_3.setMinimumSize(QSize(100, 0))
        self.out_m_3.setFont(font1)
        self.out_m_3.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_m_3.setFrameShape(QFrame.StyledPanel)
        self.out_m_3.setFrameShadow(QFrame.Plain)
        self.out_m_3.setLineWidth(3)
        self.out_m_3.setSmallDecimalPoint(True)
        self.out_m_3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_29.addWidget(self.out_m_3, 0, 2, 1, 1)

        self.d_3 = QLabel(self.widget_2)
        self.d_3.setObjectName(u"d_3")
        self.d_3.setFont(font)
        self.d_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.d_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.d_3, 2, 4, 1, 1)

        self.out_w_3 = QLCDNumber(self.widget_2)
        self.out_w_3.setObjectName(u"out_w_3")
        self.out_w_3.setMinimumSize(QSize(100, 0))
        self.out_w_3.setFont(font1)
        self.out_w_3.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_w_3.setFrameShape(QFrame.StyledPanel)
        self.out_w_3.setFrameShadow(QFrame.Plain)
        self.out_w_3.setLineWidth(3)
        self.out_w_3.setSmallDecimalPoint(True)
        self.out_w_3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_29.addWidget(self.out_w_3, 0, 5, 1, 1)

        self.l_3 = QLabel(self.widget_2)
        self.l_3.setObjectName(u"l_3")
        self.l_3.setFont(font)
        self.l_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.l_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.l_3, 2, 1, 1, 1)

        self.m_3 = QLabel(self.widget_2)
        self.m_3.setObjectName(u"m_3")
        self.m_3.setFont(font)
        self.m_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.m_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_29.addWidget(self.m_3, 0, 1, 1, 1)

        self.out_l_3 = QLCDNumber(self.widget_2)
        self.out_l_3.setObjectName(u"out_l_3")
        self.out_l_3.setMinimumSize(QSize(100, 0))
        self.out_l_3.setFont(font1)
        self.out_l_3.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_l_3.setFrameShape(QFrame.StyledPanel)
        self.out_l_3.setFrameShadow(QFrame.Plain)
        self.out_l_3.setLineWidth(3)
        self.out_l_3.setSmallDecimalPoint(True)
        self.out_l_3.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_29.addWidget(self.out_l_3, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_3, 2, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_2, 0, 0, 1, 1)

        self.output_tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_25 = QGridLayout(self.tab_12)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(3, 3, 3, 3)
        self.widget_4 = QWidget(self.tab_12)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_31 = QGridLayout(self.widget_4)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(3, 1, 3, 3)
        self.out_l_4 = QLCDNumber(self.widget_4)
        self.out_l_4.setObjectName(u"out_l_4")
        self.out_l_4.setMinimumSize(QSize(100, 0))
        self.out_l_4.setFont(font1)
        self.out_l_4.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_l_4.setFrameShape(QFrame.StyledPanel)
        self.out_l_4.setFrameShadow(QFrame.Plain)
        self.out_l_4.setLineWidth(3)
        self.out_l_4.setSmallDecimalPoint(True)
        self.out_l_4.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_31.addWidget(self.out_l_4, 2, 2, 1, 1)

        self.d_5 = QLabel(self.widget_4)
        self.d_5.setObjectName(u"d_5")
        self.d_5.setFont(font)
        self.d_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.d_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.d_5, 2, 4, 1, 1)

        self.l_5 = QLabel(self.widget_4)
        self.l_5.setObjectName(u"l_5")
        self.l_5.setFont(font)
        self.l_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.l_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.l_5, 2, 1, 1, 1)

        self.out_w_4 = QLCDNumber(self.widget_4)
        self.out_w_4.setObjectName(u"out_w_4")
        self.out_w_4.setMinimumSize(QSize(100, 0))
        self.out_w_4.setFont(font1)
        self.out_w_4.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_w_4.setFrameShape(QFrame.StyledPanel)
        self.out_w_4.setFrameShadow(QFrame.Plain)
        self.out_w_4.setLineWidth(3)
        self.out_w_4.setSmallDecimalPoint(True)
        self.out_w_4.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_31.addWidget(self.out_w_4, 0, 5, 1, 1)

        self.out_d_4 = QLCDNumber(self.widget_4)
        self.out_d_4.setObjectName(u"out_d_4")
        self.out_d_4.setMinimumSize(QSize(100, 0))
        self.out_d_4.setFont(font1)
        self.out_d_4.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_d_4.setFrameShape(QFrame.StyledPanel)
        self.out_d_4.setFrameShadow(QFrame.Plain)
        self.out_d_4.setLineWidth(3)
        self.out_d_4.setSmallDecimalPoint(True)
        self.out_d_4.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_31.addWidget(self.out_d_4, 2, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_7, 2, 6, 1, 1)

        self.out_m_4 = QLCDNumber(self.widget_4)
        self.out_m_4.setObjectName(u"out_m_4")
        self.out_m_4.setMinimumSize(QSize(100, 0))
        self.out_m_4.setFont(font1)
        self.out_m_4.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_m_4.setFrameShape(QFrame.StyledPanel)
        self.out_m_4.setFrameShadow(QFrame.Plain)
        self.out_m_4.setLineWidth(3)
        self.out_m_4.setSmallDecimalPoint(True)
        self.out_m_4.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_31.addWidget(self.out_m_4, 0, 2, 1, 1)

        self.m_5 = QLabel(self.widget_4)
        self.m_5.setObjectName(u"m_5")
        self.m_5.setFont(font)
        self.m_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.m_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.m_5, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_8, 2, 0, 1, 1)

        self.w_5 = QLabel(self.widget_4)
        self.w_5.setObjectName(u"w_5")
        self.w_5.setFont(font)
        self.w_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.w_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_31.addWidget(self.w_5, 0, 4, 1, 1)


        self.gridLayout_25.addWidget(self.widget_4, 0, 0, 1, 1)

        self.output_tabWidget_2.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_26 = QGridLayout(self.tab_13)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(3, 3, 3, 3)
        self.widget_5 = QWidget(self.tab_13)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_32 = QGridLayout(self.widget_5)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.gridLayout_32.setContentsMargins(3, 1, 3, 3)
        self.out_l_5 = QLCDNumber(self.widget_5)
        self.out_l_5.setObjectName(u"out_l_5")
        self.out_l_5.setMinimumSize(QSize(100, 0))
        self.out_l_5.setFont(font1)
        self.out_l_5.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_l_5.setFrameShape(QFrame.StyledPanel)
        self.out_l_5.setFrameShadow(QFrame.Plain)
        self.out_l_5.setLineWidth(3)
        self.out_l_5.setSmallDecimalPoint(True)
        self.out_l_5.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_32.addWidget(self.out_l_5, 2, 2, 1, 1)

        self.out_w_5 = QLCDNumber(self.widget_5)
        self.out_w_5.setObjectName(u"out_w_5")
        self.out_w_5.setMinimumSize(QSize(100, 0))
        self.out_w_5.setFont(font1)
        self.out_w_5.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_w_5.setFrameShape(QFrame.StyledPanel)
        self.out_w_5.setFrameShadow(QFrame.Plain)
        self.out_w_5.setLineWidth(3)
        self.out_w_5.setSmallDecimalPoint(True)
        self.out_w_5.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_32.addWidget(self.out_w_5, 0, 5, 1, 1)

        self.l_6 = QLabel(self.widget_5)
        self.l_6.setObjectName(u"l_6")
        self.l_6.setFont(font)
        self.l_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.l_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.l_6, 2, 1, 1, 1)

        self.m_6 = QLabel(self.widget_5)
        self.m_6.setObjectName(u"m_6")
        self.m_6.setFont(font)
        self.m_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.m_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.m_6, 0, 1, 1, 1)

        self.d_6 = QLabel(self.widget_5)
        self.d_6.setObjectName(u"d_6")
        self.d_6.setFont(font)
        self.d_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.d_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.d_6, 2, 4, 1, 1)

        self.out_m_5 = QLCDNumber(self.widget_5)
        self.out_m_5.setObjectName(u"out_m_5")
        self.out_m_5.setMinimumSize(QSize(100, 0))
        self.out_m_5.setFont(font1)
        self.out_m_5.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_m_5.setFrameShape(QFrame.StyledPanel)
        self.out_m_5.setFrameShadow(QFrame.Plain)
        self.out_m_5.setLineWidth(3)
        self.out_m_5.setSmallDecimalPoint(True)
        self.out_m_5.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_32.addWidget(self.out_m_5, 0, 2, 1, 1)

        self.out_d_5 = QLCDNumber(self.widget_5)
        self.out_d_5.setObjectName(u"out_d_5")
        self.out_d_5.setMinimumSize(QSize(100, 0))
        self.out_d_5.setFont(font1)
        self.out_d_5.setStyleSheet(u"\n"
"  border: 2px solid rgb(255, 197, 0);\n"
"  border-width: 2px;\n"
"  border-radius: 10px;\n"
"\n"
"")
        self.out_d_5.setFrameShape(QFrame.StyledPanel)
        self.out_d_5.setFrameShadow(QFrame.Plain)
        self.out_d_5.setLineWidth(3)
        self.out_d_5.setSmallDecimalPoint(True)
        self.out_d_5.setSegmentStyle(QLCDNumber.Flat)

        self.gridLayout_32.addWidget(self.out_d_5, 2, 5, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_9, 2, 6, 1, 1)

        self.w_6 = QLabel(self.widget_5)
        self.w_6.setObjectName(u"w_6")
        self.w_6.setFont(font)
        self.w_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.w_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_32.addWidget(self.w_6, 0, 4, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)


        self.gridLayout_26.addWidget(self.widget_5, 0, 0, 1, 1)

        self.output_tabWidget_2.addTab(self.tab_13, "")

        self.gridLayout.addWidget(self.output_tabWidget_2, 2, 2, 1, 1)

        self.drawit = QWidget(Widget)
        self.drawit.setObjectName(u"drawit")
        self.drawit.setMinimumSize(QSize(500, 700))
        self.gridLayout_28 = QGridLayout(self.drawit)
        self.gridLayout_28.setObjectName(u"gridLayout_28")

        self.gridLayout.addWidget(self.drawit, 0, 2, 1, 3)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(400, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 6)
        self.line_3 = QFrame(self.frame)
        self.line_3.setObjectName(u"line_3")
        font2 = QFont()
        font2.setBold(False)
        self.line_3.setFont(font2)
        self.line_3.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_2.addWidget(self.line_3, 15, 0, 1, 2)

        self.calculate = QPushButton(self.frame)
        self.calculate.setObjectName(u"calculate")
        self.calculate.setMinimumSize(QSize(0, 50))
        self.calculate.setFont(font)
        self.calculate.setAutoFillBackground(False)
        self.calculate.setStyleSheet(u"QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(255, 197, 0);\n"
"    color:  rgb(37, 37, 37);\n"
"    font-size:  14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"    color:  rgb(255, 255, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.calculate, 11, 0, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.groupBox_step = QGroupBox(self.frame)
        self.groupBox_step.setObjectName(u"groupBox_step")
        self.gridLayout_3 = QGridLayout(self.groupBox_step)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.step_4 = QRadioButton(self.groupBox_step)
        self.step_4.setObjectName(u"step_4")

        self.gridLayout_3.addWidget(self.step_4, 1, 3, 1, 1)

        self.step_2 = QRadioButton(self.groupBox_step)
        self.step_2.setObjectName(u"step_2")

        self.gridLayout_3.addWidget(self.step_2, 1, 1, 1, 1)

        self.step_3 = QRadioButton(self.groupBox_step)
        self.step_3.setObjectName(u"step_3")

        self.gridLayout_3.addWidget(self.step_3, 1, 2, 1, 1)

        self.step_auto = QRadioButton(self.groupBox_step)
        self.step_auto.setObjectName(u"step_auto")
        self.step_auto.setFont(font)
        self.step_auto.setChecked(True)

        self.gridLayout_3.addWidget(self.step_auto, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_step, 6, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 12, 0, 1, 2)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFont(font2)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 2)

        self.groupBox_scheme_rocket = QGroupBox(self.frame)
        self.groupBox_scheme_rocket.setObjectName(u"groupBox_scheme_rocket")
        self.gridLayout_4 = QGridLayout(self.groupBox_scheme_rocket)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scheme_pack = QRadioButton(self.groupBox_scheme_rocket)
        self.scheme_pack.setObjectName(u"scheme_pack")

        self.gridLayout_4.addWidget(self.scheme_pack, 1, 2, 1, 1)

        self.scheme_tandem = QRadioButton(self.groupBox_scheme_rocket)
        self.scheme_tandem.setObjectName(u"scheme_tandem")
        self.scheme_tandem.setChecked(False)

        self.gridLayout_4.addWidget(self.scheme_tandem, 1, 1, 1, 1)

        self.scheme_auto = QRadioButton(self.groupBox_scheme_rocket)
        self.scheme_auto.setObjectName(u"scheme_auto")
        self.scheme_auto.setFont(font)
        self.scheme_auto.setChecked(True)

        self.gridLayout_4.addWidget(self.scheme_auto, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_scheme_rocket, 8, 0, 1, 2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_5 = QGridLayout(self.widget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line_4 = QFrame(self.widget_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFont(font2)
        self.line_4.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_5.addWidget(self.line_4, 0, 0, 1, 1)

        self.label_40 = QLabel(self.widget_3)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(u"color: rgb(255, 197, 0);")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_40, 0, 1, 1, 1)

        self.line_5 = QFrame(self.widget_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFont(font2)
        self.line_5.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QFrame.Shape.HLine)

        self.gridLayout_5.addWidget(self.line_5, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.widget_3, 13, 0, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 197, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 7, 0, 1, 2)

        self.SpinBox_mass_PN = QDoubleSpinBox(self.frame)
        self.SpinBox_mass_PN.setObjectName(u"SpinBox_mass_PN")
        self.SpinBox_mass_PN.setMaximumSize(QSize(80, 16777215))
        self.SpinBox_mass_PN.setStyleSheet(u"background-color: rgb(53, 54, 54);")
        self.SpinBox_mass_PN.setDecimals(1)
        self.SpinBox_mass_PN.setMinimum(100.000000000000000)
        self.SpinBox_mass_PN.setMaximum(20000.000000000000000)
        self.SpinBox_mass_PN.setSingleStep(500.000000000000000)
        self.SpinBox_mass_PN.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.SpinBox_mass_PN.setValue(5000.000000000000000)

        self.gridLayout_2.addWidget(self.SpinBox_mass_PN, 3, 1, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(100, 100, 100);")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 16, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 0, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 197, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 5, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 197, 0);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)

        self.comboBox_target = QComboBox(self.frame)
        self.comboBox_target.addItem("")
        self.comboBox_target.addItem("")
        self.comboBox_target.addItem("")
        self.comboBox_target.addItem("")
        self.comboBox_target.addItem("")
        self.comboBox_target.addItem("")
        self.comboBox_target.addItem("")
        self.comboBox_target.addItem("")
        self.comboBox_target.setObjectName(u"comboBox_target")
        self.comboBox_target.setMinimumSize(QSize(0, 30))
        self.comboBox_target.setAutoFillBackground(False)
        self.comboBox_target.setStyleSheet(u"background-color: rgb(53, 54, 54);")

        self.gridLayout_2.addWidget(self.comboBox_target, 2, 0, 1, 2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_39, 2, 0, 1, 1)

        self.fuel_4 = QComboBox(self.frame_2)
        self.fuel_4.addItem("")
        self.fuel_4.addItem("")
        self.fuel_4.addItem("")
        self.fuel_4.addItem("")
        self.fuel_4.setObjectName(u"fuel_4")
        self.fuel_4.setMinimumSize(QSize(0, 30))
        self.fuel_4.setAutoFillBackground(False)
        self.fuel_4.setStyleSheet(u"background-color: rgb(53, 54, 54);")

        self.gridLayout_11.addWidget(self.fuel_4, 3, 1, 1, 1)

        self.label_38 = QLabel(self.frame_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_38, 1, 0, 1, 1)

        self.label_36 = QLabel(self.frame_2)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_36, 3, 0, 1, 1)

        self.fuel_2 = QComboBox(self.frame_2)
        self.fuel_2.addItem("")
        self.fuel_2.addItem("")
        self.fuel_2.addItem("")
        self.fuel_2.addItem("")
        self.fuel_2.setObjectName(u"fuel_2")
        self.fuel_2.setMinimumSize(QSize(0, 30))
        self.fuel_2.setAutoFillBackground(False)
        self.fuel_2.setStyleSheet(u"background-color: rgb(53, 54, 54);")

        self.gridLayout_11.addWidget(self.fuel_2, 1, 1, 1, 1)

        self.label_37 = QLabel(self.frame_2)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.label_37, 0, 0, 1, 1)

        self.fuel_1 = QComboBox(self.frame_2)
        self.fuel_1.addItem("")
        self.fuel_1.addItem("")
        self.fuel_1.addItem("")
        self.fuel_1.addItem("")
        self.fuel_1.setObjectName(u"fuel_1")
        self.fuel_1.setMinimumSize(QSize(0, 30))
        self.fuel_1.setAutoFillBackground(False)
        self.fuel_1.setStyleSheet(u"background-color: rgb(53, 54, 54);")

        self.gridLayout_11.addWidget(self.fuel_1, 0, 1, 1, 1)

        self.fuel_3 = QComboBox(self.frame_2)
        self.fuel_3.addItem("")
        self.fuel_3.addItem("")
        self.fuel_3.addItem("")
        self.fuel_3.addItem("")
        self.fuel_3.setObjectName(u"fuel_3")
        self.fuel_3.setMinimumSize(QSize(0, 30))
        self.fuel_3.setAutoFillBackground(False)
        self.fuel_3.setStyleSheet(u"background-color: rgb(53, 54, 54);")

        self.gridLayout_11.addWidget(self.fuel_3, 2, 1, 1, 1)

        self.s1 = QDoubleSpinBox(self.frame_2)
        self.s1.setObjectName(u"s1")
        self.s1.setStyleSheet(u"background-color: rgb(53, 54, 54);")
        self.s1.setAlignment(Qt.AlignCenter)
        self.s1.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.s1.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.s1.setValue(7.690000000000000)

        self.gridLayout_11.addWidget(self.s1, 0, 2, 1, 1)

        self.s2 = QDoubleSpinBox(self.frame_2)
        self.s2.setObjectName(u"s2")
        self.s2.setStyleSheet(u"background-color: rgb(53, 54, 54);")
        self.s2.setAlignment(Qt.AlignCenter)
        self.s2.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.s2.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.s2.setValue(12.330000000000000)

        self.gridLayout_11.addWidget(self.s2, 1, 2, 1, 1)

        self.s3 = QDoubleSpinBox(self.frame_2)
        self.s3.setObjectName(u"s3")
        self.s3.setStyleSheet(u"background-color: rgb(53, 54, 54);")
        self.s3.setAlignment(Qt.AlignCenter)
        self.s3.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.s3.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.s3.setValue(9.430000000000000)

        self.gridLayout_11.addWidget(self.s3, 2, 2, 1, 1)

        self.s4 = QDoubleSpinBox(self.frame_2)
        self.s4.setObjectName(u"s4")
        self.s4.setStyleSheet(u"background-color: rgb(53, 54, 54);")
        self.s4.setAlignment(Qt.AlignCenter)
        self.s4.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.s4.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.s4.setValue(9.430000000000000)

        self.gridLayout_11.addWidget(self.s4, 3, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 10, 0, 1, 2)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(u"color: rgb(255, 197, 0);")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_35, 9, 0, 1, 2)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(34, 34, 34);")

        self.gridLayout_2.addWidget(self.textEdit, 14, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 3, 1)

        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFont(font2)
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QFrame.Shape.VLine)

        self.gridLayout.addWidget(self.line_2, 0, 1, 3, 1)


        self.retranslateUi(Widget)

        self.output_tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"AutoRocket", None))
        self.w.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u044a\u0451\u043c \u0420\u041d, \u043c3", None))
        self.out_type.setText(QCoreApplication.translate("Widget", u"-", None))
        self.l.setText(QCoreApplication.translate("Widget", u"\u0414\u043b\u0438\u043d\u0430 \u0420\u041d, \u043c", None))
        self.label_type.setText(QCoreApplication.translate("Widget", u"\u0422\u0438\u043f \u043a\u043e\u043c\u043f\u043e\u043d\u043e\u0432\u043a\u0438", None))
        self.d.setText(QCoreApplication.translate("Widget", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0420\u041d, \u043c", None))
        self.count.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u043b-\u0432\u043e \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None))
        self.m.setText(QCoreApplication.translate("Widget", u"\u041c\u0430\u0441\u0441\u0430 \u0420\u041d, \u0442", None))
        self.output_tabWidget_2.setTabText(self.output_tabWidget_2.indexOf(self.tab_10), QCoreApplication.translate("Widget", u"\u041e\u0431\u0449\u0430\u044f \u0441\u0432\u043e\u0434\u043a\u0430", None))
        self.w_3.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u044a\u0451\u043c \u0420\u041d, \u043c3", None))
        self.d_3.setText(QCoreApplication.translate("Widget", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0420\u041d, \u043c", None))
        self.l_3.setText(QCoreApplication.translate("Widget", u"\u0414\u043b\u0438\u043d\u0430 \u0420\u041d, \u043c", None))
        self.m_3.setText(QCoreApplication.translate("Widget", u"\u041c\u0430\u0441\u0441\u0430 \u0420\u041d, \u043a\u0433", None))
        self.output_tabWidget_2.setTabText(self.output_tabWidget_2.indexOf(self.tab_11), QCoreApplication.translate("Widget", u"\u0421\u0442\u0443\u043f\u0435\u043d\u044c I", None))
        self.d_5.setText(QCoreApplication.translate("Widget", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0420\u041d, \u043c", None))
        self.l_5.setText(QCoreApplication.translate("Widget", u"\u0414\u043b\u0438\u043d\u0430 \u0420\u041d, \u043c", None))
        self.m_5.setText(QCoreApplication.translate("Widget", u"\u041c\u0430\u0441\u0441\u0430 \u0420\u041d, \u043a\u0433", None))
        self.w_5.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u044a\u0451\u043c \u0420\u041d, \u043c3", None))
        self.output_tabWidget_2.setTabText(self.output_tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("Widget", u"\u0421\u0442\u0443\u043f\u0435\u043d\u044c II", None))
        self.l_6.setText(QCoreApplication.translate("Widget", u"\u0414\u043b\u0438\u043d\u0430 \u0420\u041d, \u043c", None))
        self.m_6.setText(QCoreApplication.translate("Widget", u"\u041c\u0430\u0441\u0441\u0430 \u0420\u041d, \u0442", None))
        self.d_6.setText(QCoreApplication.translate("Widget", u"\u0414\u0438\u0430\u043c\u0435\u0442\u0440 \u0420\u041d, \u043c", None))
        self.w_6.setText(QCoreApplication.translate("Widget", u"\u041e\u0431\u044a\u0451\u043c \u0420\u041d, \u043c3", None))
        self.output_tabWidget_2.setTabText(self.output_tabWidget_2.indexOf(self.tab_13), QCoreApplication.translate("Widget", u"\u0421\u0442\u0443\u043f\u0435\u043d\u044c III", None))
        self.calculate.setText(QCoreApplication.translate("Widget", u"\u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0441\u0447\u0451\u0442", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u041c\u0430\u0441\u0441\u0430 \u043f\u043e\u043b\u0435\u0437\u043d\u043e\u0439 \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0438, \u0432 \u043a\u0433", None))
        self.groupBox_step.setTitle("")
        self.step_4.setText(QCoreApplication.translate("Widget", u"4", None))
        self.step_2.setText(QCoreApplication.translate("Widget", u"2", None))
        self.step_3.setText(QCoreApplication.translate("Widget", u"3", None))
        self.step_auto.setText(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.groupBox_scheme_rocket.setTitle("")
        self.scheme_pack.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u043a\u0435\u0442", None))
        self.scheme_tandem.setText(QCoreApplication.translate("Widget", u"\u0422\u0430\u043d\u0434\u0435\u043c", None))
        self.scheme_auto.setText(QCoreApplication.translate("Widget", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438", None))
        self.label_40.setText(QCoreApplication.translate("Widget", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u0421\u0445\u0435\u043c\u0430 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"Designed by (cosm1c) Mikhail Kolobakhin for SSAU in 2024 y.", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0426\u0435\u043b\u044c \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.comboBox_target.setItemText(0, QCoreApplication.translate("Widget", u"\u041d\u0430 \u043d\u0438\u0437\u043a\u0443\u044e \u043a\u0440\u0443\u0433\u043e\u0432\u0443\u044e \u043e\u0440\u0431\u0438\u0442\u0443 (9,2 \u043a\u043c/\u0441)", None))
        self.comboBox_target.setItemText(1, QCoreApplication.translate("Widget", u"\u041d\u0430 \u044d\u043b\u0435\u043f\u0442\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u043e\u0440\u0431\u0438\u0442\u0443 \u0441 \u0430\u043f\u043e\u0433\u0435\u0435\u043c 40 000 \u043a\u043c (12,3 \u043a\u043c/\u0441)", None))
        self.comboBox_target.setItemText(2, QCoreApplication.translate("Widget", u"\u041d\u0430 \u0441\u0442\u0430\u0446\u0438\u043e\u043d\u0430\u0440\u043d\u0443\u044e \u043e\u0440\u0431\u0438\u0442\u0443 (13,7 \u043a\u043c/\u0441)", None))
        self.comboBox_target.setItemText(3, QCoreApplication.translate("Widget", u"\u0417\u0430 \u043f\u0440\u0435\u0434\u0435\u043b\u044b \u0441\u0444\u0435\u0440\u044b \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f \u0417\u0435\u043c\u043b\u0438 (\u0438\u0441\u043a\u0443\u0441\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f \u043f\u043b\u0430\u043d\u0435\u0442\u0430) (12,5 \u043a\u043c/\u0441)", None))
        self.comboBox_target.setItemText(4, QCoreApplication.translate("Widget", u"\u041e\u0431\u043b\u0451\u0442 \u041b\u0443\u043d\u044b (13,5 \u043a\u043c/\u0441)", None))
        self.comboBox_target.setItemText(5, QCoreApplication.translate("Widget", u"\u0412\u044b\u0432\u0435\u0434\u0435\u043d\u0438\u0435 \u041a\u0410 \u043d\u0430 \u0441\u0435\u043b\u0435\u043d\u043e\u0446\u0435\u043d\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u043e\u0440\u0431\u0438\u0442\u0443 (\u0441\u043f\u0443\u0442\u043d\u0438\u043a \u041b\u0443\u043d\u044b) (13,8 \u043a\u043c/\u0441)", None))
        self.comboBox_target.setItemText(6, QCoreApplication.translate("Widget", u"\u041f\u043e\u043b\u0451\u0442 \u041a\u0410 \u043a \u041b\u0443\u043d\u0435 \u0441 \u043f\u043e\u0441\u0430\u0434\u043a\u043e\u0439 \u043d\u0430 \u043f\u043e\u0432\u0435\u0440\u0445\u043d\u043e\u0441\u0442\u044c (16,5 \u043a\u043c/\u0441)", None))
        self.comboBox_target.setItemText(7, QCoreApplication.translate("Widget", u"\u041f\u043e\u043b\u0451\u0442 \u041a\u0410 \u0432\u0431\u043b\u0438\u0437\u0438 \u0438\u043b\u0438 \u0441 \u043f\u043e\u0441\u0430\u0434\u043a\u043e\u0439 \u041c\u0430\u0440\u0441\u0430 (\u0412\u0435\u043d\u0435\u0440\u044b)  (13,5 \u043a\u043c/\u0441)", None))

        self.comboBox_target.setPlaceholderText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0436\u0435\u043b\u0430\u0435\u043c\u0443\u044e \u0446\u0435\u043b\u044c \u0432\u044b\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.label_39.setText(QCoreApplication.translate("Widget", u"III", None))
        self.fuel_4.setItemText(0, QCoreApplication.translate("Widget", u"\u041a\u0435\u0440\u043e\u0441\u0438\u043d + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 1000 \u043a\u0433/\u043c3, w = 3475 \u043c/\u0441)", None))
        self.fuel_4.setItemText(1, QCoreApplication.translate("Widget", u"\u0412\u043e\u0434\u043e\u0440\u043e\u0434 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 200 \u043a\u0433/\u043c3, w = 4500 \u043c/\u0441)", None))
        self.fuel_4.setItemText(2, QCoreApplication.translate("Widget", u"\u0421\u041f\u0413 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 820 \u043a\u0433/\u043c3, w = 3740 \u043c/\u0441)", None))
        self.fuel_4.setItemText(3, QCoreApplication.translate("Widget", u"\u041d\u0414\u041c\u0413 + 4NO2 (p = 1280 \u043a\u0433/\u043c3, w = 2795 \u043c/\u0441)", None))

        self.fuel_4.setPlaceholderText("")
        self.label_38.setText(QCoreApplication.translate("Widget", u"II", None))
        self.label_36.setText(QCoreApplication.translate("Widget", u"IV", None))
        self.fuel_2.setItemText(0, QCoreApplication.translate("Widget", u"\u041a\u0435\u0440\u043e\u0441\u0438\u043d + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 1000 \u043a\u0433/\u043c3, w = 3475 \u043c/\u0441)", None))
        self.fuel_2.setItemText(1, QCoreApplication.translate("Widget", u"\u0412\u043e\u0434\u043e\u0440\u043e\u0434 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 200 \u043a\u0433/\u043c3, w = 4500 \u043c/\u0441)", None))
        self.fuel_2.setItemText(2, QCoreApplication.translate("Widget", u"\u0421\u041f\u0413 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 820 \u043a\u0433/\u043c3, w = 3740 \u043c/\u0441)", None))
        self.fuel_2.setItemText(3, QCoreApplication.translate("Widget", u"\u041d\u0414\u041c\u0413 + 4NO2 (p = 1280 \u043a\u0433/\u043c3, w = 2795 \u043c/\u0441)", None))

        self.fuel_2.setPlaceholderText("")
        self.label_37.setText(QCoreApplication.translate("Widget", u"I", None))
        self.fuel_1.setItemText(0, QCoreApplication.translate("Widget", u"\u041a\u0435\u0440\u043e\u0441\u0438\u043d + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 1000 \u043a\u0433/\u043c3, w = 3475 \u043c/\u0441)", None))
        self.fuel_1.setItemText(1, QCoreApplication.translate("Widget", u"\u0412\u043e\u0434\u043e\u0440\u043e\u0434 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 200 \u043a\u0433/\u043c3, w = 4500 \u043c/\u0441)", None))
        self.fuel_1.setItemText(2, QCoreApplication.translate("Widget", u"\u0421\u041f\u0413 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 820 \u043a\u0433/\u043c3, w = 3740 \u043c/\u0441)", None))
        self.fuel_1.setItemText(3, QCoreApplication.translate("Widget", u"\u041d\u0414\u041c\u0413 + 4NO2 (p = 1280 \u043a\u0433/\u043c3, w = 2795 \u043c/\u0441)", None))

        self.fuel_1.setPlaceholderText("")
        self.fuel_3.setItemText(0, QCoreApplication.translate("Widget", u"\u041a\u0435\u0440\u043e\u0441\u0438\u043d + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 1000 \u043a\u0433/\u043c3, w = 3475 \u043c/\u0441)", None))
        self.fuel_3.setItemText(1, QCoreApplication.translate("Widget", u"\u0412\u043e\u0434\u043e\u0440\u043e\u0434 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 200 \u043a\u0433/\u043c3, w = 4500 \u043c/\u0441)", None))
        self.fuel_3.setItemText(2, QCoreApplication.translate("Widget", u"\u0421\u041f\u0413 + \u043a\u0438\u0441\u043b\u043e\u0440\u043e\u0434 (p = 820 \u043a\u0433/\u043c3, w = 3740 \u043c/\u0441)", None))
        self.fuel_3.setItemText(3, QCoreApplication.translate("Widget", u"\u041d\u0414\u041c\u0413 + 4NO2 (p = 1280 \u043a\u0433/\u043c3, w = 2795 \u043c/\u0441)", None))

        self.fuel_3.setPlaceholderText("")
        self.label_35.setText(QCoreApplication.translate("Widget", u"\u0422\u0438\u043f \u0442\u043e\u043f\u043b\u0438\u0432\u0430 \u0431\u043b\u043e\u043a\u043e\u0432 \u0438 \u0438\u0445 \u043a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0438\u0432\u043d\u0430\u044f \u0445-\u043a\u0430", None))
        self.textEdit.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u0435 \u0440\u0430\u0441\u0447\u0451\u0442, \u0434\u043b\u044f \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u043e\u043f\u0442\u0438\u043c\u0438\u0437\u0430\u0446\u0438\u0438</span></p></body></html>", None))
    # retranslateUi

