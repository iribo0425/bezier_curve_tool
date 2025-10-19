# -*- coding: utf-8 -*-
DECIMAL_COUNT = 6

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QMenuBar, QPushButton, QSizePolicy, QSlider, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 680)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setMaximumSize(QSize(120, 16777215))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label.setMargin(0)
        self.horizontalLayout.addWidget(self.label)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(5, 0))
        self.widget.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout.addWidget(self.widget)
        self.combo_box_plane = QComboBox(self.centralwidget)
        self.combo_box_plane.setObjectName(u"combo_box_plane")
        self.horizontalLayout.addWidget(self.combo_box_plane)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_message = QLabel(self.centralwidget)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setStyleSheet(u"color: yellow;")
        self.verticalLayout.addWidget(self.label_message)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 2))
        self.frame.setMaximumSize(QSize(16777215, 2))
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_editPt0 = QVBoxLayout()
        self.verticalLayout_editPt0.setObjectName(u"verticalLayout_editPt0")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setMargin(0)
        self.horizontalLayout_2.addWidget(self.label_3)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(5, 0))
        self.widget_2.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.label_edit_pt_num0 = QLabel(self.centralwidget)
        self.label_edit_pt_num0.setObjectName(u"label_edit_pt_num0")
        self.horizontalLayout_2.addWidget(self.label_edit_pt_num0)
        self.verticalLayout_editPt0.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(120, 0))
        self.label_5.setMaximumSize(QSize(120, 16777215))
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setMargin(0)
        self.horizontalLayout_3.addWidget(self.label_5)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(5, 0))
        self.widget_3.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.label_tan_handle_num0 = QLabel(self.centralwidget)
        self.label_tan_handle_num0.setObjectName(u"label_tan_handle_num0")
        self.horizontalLayout_3.addWidget(self.label_tan_handle_num0)
        self.verticalLayout_editPt0.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(120, 0))
        self.label_6.setMaximumSize(QSize(120, 16777215))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setMargin(0)
        self.horizontalLayout_4.addWidget(self.label_6)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(5, 0))
        self.widget_4.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_4.addWidget(self.widget_4)
        self.line_edit_edit_pt_pos_x0 = QLineEdit(self.centralwidget)
        self.line_edit_edit_pt_pos_x0.setObjectName(u"line_edit_edit_pt_pos_x0")
        self.horizontalLayout_4.addWidget(self.line_edit_edit_pt_pos_x0)
        self.line_edit_edit_pt_pos_y0 = QLineEdit(self.centralwidget)
        self.line_edit_edit_pt_pos_y0.setObjectName(u"line_edit_edit_pt_pos_y0")
        self.horizontalLayout_4.addWidget(self.line_edit_edit_pt_pos_y0)
        self.line_edit_edit_pt_pos_z0 = QLineEdit(self.centralwidget)
        self.line_edit_edit_pt_pos_z0.setObjectName(u"line_edit_edit_pt_pos_z0")
        self.horizontalLayout_4.addWidget(self.line_edit_edit_pt_pos_z0)
        self.verticalLayout_editPt0.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(120, 0))
        self.label_7.setMaximumSize(QSize(120, 16777215))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_5.addWidget(self.label_7)
        self.widget_5 = QWidget(self.centralwidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(5, 0))
        self.horizontalLayout_5.addWidget(self.widget_5)
        self.line_edit_tan_handle_pos_x0 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_pos_x0.setObjectName(u"line_edit_tan_handle_pos_x0")
        self.horizontalLayout_5.addWidget(self.line_edit_tan_handle_pos_x0)
        self.line_edit_tan_handle_pos_y0 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_pos_y0.setObjectName(u"line_edit_tan_handle_pos_y0")
        self.horizontalLayout_5.addWidget(self.line_edit_tan_handle_pos_y0)
        self.line_edit_tan_handle_pos_z0 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_pos_z0.setObjectName(u"line_edit_tan_handle_pos_z0")
        self.horizontalLayout_5.addWidget(self.line_edit_tan_handle_pos_z0)
        self.verticalLayout_editPt0.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(120, 0))
        self.label_8.setMaximumSize(QSize(120, 16777215))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.label_8)
        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(5, 0))
        self.widget_6.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_6.addWidget(self.widget_6)
        self.slider_tan_handle_angle0 = QSlider(self.centralwidget)
        self.slider_tan_handle_angle0.setObjectName(u"slider_tan_handle_angle0")
        self.slider_tan_handle_angle0.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalLayout_6.addWidget(self.slider_tan_handle_angle0)
        self.line_edit_tan_handle_angle0 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_angle0.setObjectName(u"line_edit_tan_handle_angle0")
        self.horizontalLayout_6.addWidget(self.line_edit_tan_handle_angle0)
        self.verticalLayout_editPt0.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(120, 0))
        self.label_16.setMaximumSize(QSize(120, 16777215))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_12.addWidget(self.label_16)
        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(5, 0))
        self.widget_7.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_12.addWidget(self.widget_7)
        self.slider_tan_handle_len0 = QSlider(self.centralwidget)
        self.slider_tan_handle_len0.setObjectName(u"slider_tan_handle_len0")
        self.slider_tan_handle_len0.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalLayout_12.addWidget(self.slider_tan_handle_len0)
        self.line_edit_tan_handle_len0 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_len0.setObjectName(u"line_edit_tan_handle_len0")
        self.horizontalLayout_12.addWidget(self.line_edit_tan_handle_len0)
        self.verticalLayout_editPt0.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(120, 0))
        self.label_17.setMaximumSize(QSize(120, 16777215))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_13.addWidget(self.label_17)
        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(5, 0))
        self.widget_8.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_13.addWidget(self.widget_8)
        self.line_edit_tan_handle_height0 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_height0.setObjectName(u"line_edit_tan_handle_height0")
        self.horizontalLayout_13.addWidget(self.line_edit_tan_handle_height0)
        self.verticalLayout_editPt0.addLayout(self.horizontalLayout_13)
        self.verticalLayout.addLayout(self.verticalLayout_editPt0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 2))
        self.frame_2.setMaximumSize(QSize(16777215, 2))
        self.frame_2.setFrameShape(QFrame.Shape.HLine)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout.addWidget(self.frame_2)
        self.verticalLayout_editPt1 = QVBoxLayout()
        self.verticalLayout_editPt1.setObjectName(u"verticalLayout_editPt1")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(120, 0))
        self.label_10.setMaximumSize(QSize(120, 16777215))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_7.addWidget(self.label_10)
        self.widget_9 = QWidget(self.centralwidget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(5, 0))
        self.widget_9.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_7.addWidget(self.widget_9)
        self.label_edit_pt_num1 = QLabel(self.centralwidget)
        self.label_edit_pt_num1.setObjectName(u"label_edit_pt_num1")
        self.horizontalLayout_7.addWidget(self.label_edit_pt_num1)
        self.verticalLayout_editPt1.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(120, 0))
        self.label_12.setMaximumSize(QSize(120, 16777215))
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_8.addWidget(self.label_12)
        self.widget_10 = QWidget(self.centralwidget)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(5, 0))
        self.widget_10.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_8.addWidget(self.widget_10)
        self.label_tan_handle_num1 = QLabel(self.centralwidget)
        self.label_tan_handle_num1.setObjectName(u"label_tan_handle_num1")
        self.horizontalLayout_8.addWidget(self.label_tan_handle_num1)
        self.verticalLayout_editPt1.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(120, 0))
        self.label_13.setMaximumSize(QSize(120, 16777215))
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_9.addWidget(self.label_13)
        self.widget_11 = QWidget(self.centralwidget)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(5, 0))
        self.widget_11.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_9.addWidget(self.widget_11)
        self.line_edit_edit_pt_pos_x1 = QLineEdit(self.centralwidget)
        self.line_edit_edit_pt_pos_x1.setObjectName(u"line_edit_edit_pt_pos_x1")
        self.horizontalLayout_9.addWidget(self.line_edit_edit_pt_pos_x1)
        self.line_edit_edit_pt_pos_y1 = QLineEdit(self.centralwidget)
        self.line_edit_edit_pt_pos_y1.setObjectName(u"line_edit_edit_pt_pos_y1")
        self.horizontalLayout_9.addWidget(self.line_edit_edit_pt_pos_y1)
        self.line_edit_edit_pt_pos_z1 = QLineEdit(self.centralwidget)
        self.line_edit_edit_pt_pos_z1.setObjectName(u"line_edit_edit_pt_pos_z1")
        self.horizontalLayout_9.addWidget(self.line_edit_edit_pt_pos_z1)
        self.verticalLayout_editPt1.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(120, 0))
        self.label_14.setMaximumSize(QSize(120, 16777215))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_10.addWidget(self.label_14)
        self.widget_12 = QWidget(self.centralwidget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(5, 0))
        self.widget_12.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_10.addWidget(self.widget_12)
        self.line_edit_tan_handle_pos_x1 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_pos_x1.setObjectName(u"line_edit_tan_handle_pos_x1")
        self.horizontalLayout_10.addWidget(self.line_edit_tan_handle_pos_x1)
        self.line_edit_tan_handle_pos_y1 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_pos_y1.setObjectName(u"line_edit_tan_handle_pos_y1")
        self.horizontalLayout_10.addWidget(self.line_edit_tan_handle_pos_y1)
        self.line_edit_tan_handle_pos_z1 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_pos_z1.setObjectName(u"line_edit_tan_handle_pos_z1")
        self.horizontalLayout_10.addWidget(self.line_edit_tan_handle_pos_z1)
        self.verticalLayout_editPt1.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(120, 0))
        self.label_15.setMaximumSize(QSize(120, 16777215))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_11.addWidget(self.label_15)
        self.widget_13 = QWidget(self.centralwidget)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(5, 0))
        self.widget_13.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_11.addWidget(self.widget_13)
        self.slider_tan_handle_angle1 = QSlider(self.centralwidget)
        self.slider_tan_handle_angle1.setObjectName(u"slider_tan_handle_angle1")
        self.slider_tan_handle_angle1.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalLayout_11.addWidget(self.slider_tan_handle_angle1)
        self.line_edit_tan_handle_angle1 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_angle1.setObjectName(u"line_edit_tan_handle_angle1")
        self.horizontalLayout_11.addWidget(self.line_edit_tan_handle_angle1)
        self.verticalLayout_editPt1.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(120, 0))
        self.label_18.setMaximumSize(QSize(120, 16777215))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_14.addWidget(self.label_18)
        self.widget_14 = QWidget(self.centralwidget)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMinimumSize(QSize(5, 0))
        self.widget_14.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_14.addWidget(self.widget_14)
        self.slider_tan_handle_len1 = QSlider(self.centralwidget)
        self.slider_tan_handle_len1.setObjectName(u"slider_tan_handle_len1")
        self.slider_tan_handle_len1.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalLayout_14.addWidget(self.slider_tan_handle_len1)
        self.line_edit_tan_handle_len1 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_len1.setObjectName(u"line_edit_tan_handle_len1")
        self.horizontalLayout_14.addWidget(self.line_edit_tan_handle_len1)
        self.verticalLayout_editPt1.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(120, 0))
        self.label_19.setMaximumSize(QSize(120, 16777215))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayout_15.addWidget(self.label_19)
        self.widget_15 = QWidget(self.centralwidget)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(5, 0))
        self.widget_15.setMaximumSize(QSize(5, 16777215))
        self.horizontalLayout_15.addWidget(self.widget_15)
        self.line_edit_tan_handle_height1 = QLineEdit(self.centralwidget)
        self.line_edit_tan_handle_height1.setObjectName(u"line_edit_tan_handle_height1")
        self.horizontalLayout_15.addWidget(self.line_edit_tan_handle_height1)
        self.verticalLayout_editPt1.addLayout(self.horizontalLayout_15)
        self.verticalLayout.addLayout(self.verticalLayout_editPt1)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 2))
        self.frame_3.setMaximumSize(QSize(16777215, 2))
        self.frame_3.setFrameShape(QFrame.Shape.HLine)
        self.frame_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout.addWidget(self.frame_3)
        self.button_set_angles = QPushButton(self.centralwidget)
        self.button_set_angles.setObjectName(u"button_set_angles")
        self.verticalLayout.addWidget(self.button_set_angles)
        self.button_set_lens = QPushButton(self.centralwidget)
        self.button_set_lens.setObjectName(u"button_set_lens")
        self.verticalLayout.addWidget(self.button_set_lens)
        self.button_set_heights = QPushButton(self.centralwidget)
        self.button_set_heights.setObjectName(u"button_set_heights")
        self.verticalLayout.addWidget(self.button_set_heights)
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.label_20)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Bezier Curve Tool", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plane", None))
        self.label_message.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Edit Pt Num", None))
        self.label_edit_pt_num0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Num", None))
        self.label_tan_handle_num0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Edit Pt Pos", None))
        self.line_edit_edit_pt_pos_x0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_edit_pt_pos_y0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_edit_pt_pos_z0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Pos", None))
        self.line_edit_tan_handle_pos_x0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_tan_handle_pos_y0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_tan_handle_pos_z0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Angle", None))
        self.line_edit_tan_handle_angle0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Length", None))
        self.line_edit_tan_handle_len0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Height", None))
        self.line_edit_tan_handle_height0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Edit Pt Num", None))
        self.label_edit_pt_num1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Num", None))
        self.label_tan_handle_num1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Edit Pt Pos", None))
        self.line_edit_edit_pt_pos_x1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_edit_pt_pos_y1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_edit_pt_pos_z1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Pos", None))
        self.line_edit_tan_handle_pos_x1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_tan_handle_pos_y1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.line_edit_tan_handle_pos_z1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Angle", None))
        self.line_edit_tan_handle_angle1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Length", None))
        self.line_edit_tan_handle_len1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Tan Handle Height", None))
        self.line_edit_tan_handle_height1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_set_angles.setText(QCoreApplication.translate("MainWindow", u"Set tan handle angles to 0", None))
        self.button_set_lens.setText(QCoreApplication.translate("MainWindow", u"Set tan handle lengths to 0.5", None))
        self.button_set_heights.setText(QCoreApplication.translate("MainWindow", u"Set tan handle heights to 0", None))
        self.label_20.setText("")

import hou
import math
import re
from enum import Enum
from PySide6 import QtCore, QtWidgets, QtGui

class Vector3Utils(object):
    @staticmethod
    def back():
        return hou.Vector3(0.0, 0.0, -1.0)

    @staticmethod
    def down():
        return hou.Vector3(0.0, -1.0, 0.0)

    @staticmethod
    def forward():
        return hou.Vector3(0.0, 0.0, 1.0)

    @staticmethod
    def left():
        return hou.Vector3(1.0, 0.0, 0.0)

    @staticmethod
    def negative_inf():
        return hou.Vector3(-float("inf"), -float("inf"), -float("inf"))

    @staticmethod
    def one():
        return hou.Vector3(1.0, 1.0, 1.0)

    @staticmethod
    def positive_inf():
        return hou.Vector3(float("inf"), float("inf"), float("inf"))

    @staticmethod
    def right():
        return hou.Vector3(-1.0, 0.0, 0.0)

    @staticmethod
    def up():
        return hou.Vector3(0.0, 1.0, 0.0)

    @staticmethod
    def zero():
        return hou.Vector3(0.0, 0.0, 0.0)

    @staticmethod
    def is_almost_equal(a, b, tolerance=0.00001):
        return a.isAlmostEqual(b, tolerance)

def get_delta_angle(current, target):
    c = normalize_angle(current)
    t = normalize_angle(target)

    delta_angle = t - c

    if delta_angle > 180.0:
        delta_angle = t - 360.0 - c
    elif delta_angle < -180.0:
        delta_angle = t + 360.0 - c

    return delta_angle

def get_up_vec(forward_vec):
    up_vec = forward_vec.cross(Vector3Utils.left())

    if up_vec.y() < 0.0:
        up_vec *= -1

    return up_vec

def normalize_angle(angle):
    a = angle

    while a > 180.0:
        a -= 360.0

    while a < -180.0:
        a += 360.0

    return a

def project_vec_on_plane(vec, normal):
    return vec - vec.dot(normal) / normal.dot(normal) * normal

def add_property(instance, name, initial_val, b_can_set=True, eq=lambda x, y: x == y):
    attr_name = f"_{type(instance).__name__}__{name}"
    setattr(instance, attr_name, initial_val)

    signal_name = f"on_{name}_changed"
    setattr(type(instance), signal_name, QtCore.Signal(type(initial_val)))

    def getter():
        return getattr(instance, attr_name)

    setattr(instance, name, getter)

    attr_name_setting = f"_{type(instance).__name__}__{name}_setting"
    setattr(instance, attr_name_setting, False)

    def setter(val):
        if getattr(instance, attr_name_setting):
            return

        val_ = getattr(instance, attr_name)
        if not eq(val, val_):
            setattr(instance, attr_name_setting, True)
            setattr(instance, attr_name, val)
            getattr(instance, f"on_{name}_changed").emit(val)
            setattr(instance, attr_name_setting, False)

    private_setter_name = f"_{type(instance).__name__}__set_{name}"
    setattr(instance, private_setter_name, setter)

    if b_can_set:
        public_setter_name = f"set_{name}"
        setattr(instance, public_setter_name, setter)

class Plane(Enum):
    XY = "XY (Front)"
    YZ = "YZ (Right)"
    ZX = "ZX (Top)"

class EditPt(QtCore.QObject):
    def __init__(self):
        add_property(self, "edit_pt_num", 0)
        add_property(self, "tan_handle_num", 0)
        add_property(self, "edit_pt_pos", Vector3Utils.zero(), True, Vector3Utils.is_almost_equal)
        add_property(self, "tan_handle_pos", Vector3Utils.zero(), True, Vector3Utils.is_almost_equal)
        add_property(self, "tan_handle_angle", 0.0, True, math.isclose)
        add_property(self, "tan_handle_len", 0.0, True, math.isclose)
        add_property(self, "tan_handle_height", 0.0, True, math.isclose)

        super(EditPt, self).__init__()

    def disable(self):
        self.set_edit_pt_num(0)
        self.set_tan_handle_num(0)
        self.set_edit_pt_pos(Vector3Utils.zero())
        self.set_tan_handle_pos(Vector3Utils.zero())
        self.set_tan_handle_angle(0.0)
        self.set_tan_handle_len(0.0)
        self.set_tan_handle_height(0.0)

    def __eq__(self, other):
        return (self.__edit_pt_num == other.__edit_pt_num)\
            and (self.__tan_handle_num == other.__tan_handle_num)\
            and self.__edit_pt_pos.isAlmostEqual(other.__edit_pt_pos)\
            and self.__tan_handle_pos.isAlmostEqual(other.__tan_handle_pos)\
            and math.isclose(self.__tan_handle_angle, other.__tan_handle_angle)\
            and math.isclose(self.__tan_handle_len, other.__tan_handle_len)\
            and math.isclose(self.__tan_handle_height, other.__tan_handle_height)

    def __ne__(self, other):
        return not self.__eq__(other)

class Segment(QtCore.QObject):
    def __init__(self):
        add_property(self, "plane_normal", Vector3Utils.forward(), True, Vector3Utils.is_almost_equal)
        add_property(self, "edit_pt0", EditPt(), False)
        add_property(self, "edit_pt1", EditPt(), False)

        super(Segment, self).__init__()

        self.__b_is_setting = False

        def f(val):
            self.__set_tan_handle_additional_params(0)
            self.__set_tan_handle_additional_params(1)

        self.on_plane_normal_changed.connect(f)

        def f(val):
            self.__set_tan_handle_additional_params(0)
            self.__set_tan_handle_additional_params(1)

        self.__edit_pt0.on_edit_pt_pos_changed.connect(f)
        self.__edit_pt0.on_tan_handle_pos_changed.connect(lambda val: self.__set_tan_handle_additional_params(0))
        self.__edit_pt0.on_tan_handle_angle_changed.connect(lambda: self.__set_tan_handle_pos(0))
        self.__edit_pt0.on_tan_handle_len_changed.connect(lambda: self.__set_tan_handle_pos(0))
        self.__edit_pt0.on_tan_handle_height_changed.connect(lambda: self.__set_tan_handle_pos(0))

        def f(val):
            self.__set_tan_handle_additional_params(0)
            self.__set_tan_handle_additional_params(1)

        self.__edit_pt1.on_edit_pt_pos_changed.connect(f)
        self.__edit_pt1.on_tan_handle_pos_changed.connect(lambda val: self.__set_tan_handle_additional_params(1))
        self.__edit_pt1.on_tan_handle_angle_changed.connect(lambda: self.__set_tan_handle_pos(1))
        self.__edit_pt1.on_tan_handle_len_changed.connect(lambda: self.__set_tan_handle_pos(1))
        self.__edit_pt1.on_tan_handle_height_changed.connect(lambda: self.__set_tan_handle_pos(1))

    def disable(self):
        self.edit_pt0().disable()
        self.edit_pt1().disable()

    def __eq__(self, other):
        return (self.__b_is_setting == other.__b_is_setting)\
            and (self.__plane_normal.isAlmostEqual(other.__plane_normal))\
            and (self.__edit_pt0 == other.__edit_pt0)\
            and (self.__edit_pt1 == other.__edit_pt1)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __set_tan_handle_pos(self, edit_pt_index):
        if self.__b_is_setting:
            return

        edit_pt0 = EditPt()
        edit_pt1 = EditPt()

        if edit_pt_index == 0:
            edit_pt0 = self.__edit_pt0
            edit_pt1 = self.__edit_pt1
        else:
            edit_pt0 = self.__edit_pt1
            edit_pt1 = self.__edit_pt0

        quat00 = hou.Quaternion()
        quat00.setToVectors(self.__plane_normal, Vector3Utils.forward())
        up_vec = get_up_vec(self.__plane_normal)
        up_vec_rotated = quat00.rotate(up_vec)
        quat01 = hou.Quaternion()
        quat01.setToVectors(up_vec_rotated, Vector3Utils.up())
        quat0 = quat00 * quat01

        edit_pt_pos0_rotated = quat0.rotate(edit_pt0.edit_pt_pos())
        edit_pt_pos1_rotated = quat0.rotate(edit_pt1.edit_pt_pos())

        edit_pt_pos0_projected = project_vec_on_plane(edit_pt_pos0_rotated, Vector3Utils.forward())
        edit_pt_pos1_projected = project_vec_on_plane(edit_pt_pos1_rotated, Vector3Utils.forward())

        quat1 = hou.Quaternion(edit_pt0.tan_handle_angle(), Vector3Utils.forward())

        tan_handle_pos0_projected = quat1.rotate((edit_pt_pos1_projected - edit_pt_pos0_projected) * edit_pt0.tan_handle_len()) + edit_pt_pos0_projected

        tan_handle_pos0_rotated = tan_handle_pos0_projected + hou.Vector3(0.0, 0.0, edit_pt0.tan_handle_height())

        new_tan_handle_pos = quat0.inverse().rotate(tan_handle_pos0_rotated)

        self.__b_is_setting = True

        edit_pt0.set_tan_handle_pos(new_tan_handle_pos)

        self.__b_is_setting = False

    def __set_tan_handle_additional_params(self, edit_pt_index):
        if self.__b_is_setting:
            return

        edit_pt0 = EditPt()
        edit_pt1 = EditPt()

        if edit_pt_index == 0:
            edit_pt0 = self.__edit_pt0
            edit_pt1 = self.__edit_pt1
        else:
            edit_pt0 = self.__edit_pt1
            edit_pt1 = self.__edit_pt0

        quat0 = hou.Quaternion()
        quat0.setToVectors(self.__plane_normal, Vector3Utils.forward())
        up_vec = get_up_vec(self.__plane_normal)
        up_vec_rotated = quat0.rotate(up_vec)
        quat1 = hou.Quaternion()
        quat1.setToVectors(up_vec_rotated, Vector3Utils.up())
        quat = quat0 * quat1

        edit_pt_pos0_rotated = quat.rotate(edit_pt0.edit_pt_pos())
        tan_handle_pos0_rotated = quat.rotate(edit_pt0.tan_handle_pos())
        edit_pt_pos1_rotated = quat.rotate(edit_pt1.edit_pt_pos())

        edit_pt_pos0_projected = project_vec_on_plane(edit_pt_pos0_rotated, Vector3Utils.forward())
        tan_handle_pos0_projected = project_vec_on_plane(tan_handle_pos0_rotated, Vector3Utils.forward())
        edit_pt_pos1_projected = project_vec_on_plane(edit_pt_pos1_rotated, Vector3Utils.forward())

        diff0 = edit_pt_pos1_projected - edit_pt_pos0_projected
        diff1 = tan_handle_pos0_projected - edit_pt_pos0_projected

        if not diff0.isAlmostEqual(Vector3Utils.zero()):
            self.__b_is_setting = True

            angle0 = math.degrees(math.atan2(diff0.y(), diff0.x()))
            angle1 = math.degrees(math.atan2(diff1.y(), diff1.x()))
            delta_angle = get_delta_angle(angle0, angle1)
            edit_pt0.set_tan_handle_angle(delta_angle)

            edit_pt0.set_tan_handle_len(diff1.length() / diff0.length())

            edit_pt0.set_tan_handle_height(tan_handle_pos0_rotated.z())

            self.__b_is_setting = False

class MainModel(QtCore.QObject):
    def __init__(self):
        add_property(self, "message", "", False)
        add_property(self, "segment", Segment(), False)

        super(MainModel, self).__init__()

        self.__node_path = ""

        self.__segment.edit_pt0().on_edit_pt_pos_changed.connect(lambda val: self.__set_pt_pos(self.__segment.edit_pt0().edit_pt_num(), val))
        self.__segment.edit_pt0().on_tan_handle_pos_changed.connect(lambda val: self.__set_pt_pos(self.__segment.edit_pt0().tan_handle_num(), val))
        self.__segment.edit_pt1().on_edit_pt_pos_changed.connect(lambda val: self.__set_pt_pos(self.__segment.edit_pt1().edit_pt_num(), val))
        self.__segment.edit_pt1().on_tan_handle_pos_changed.connect(lambda val: self.__set_pt_pos(self.__segment.edit_pt1().tan_handle_num(), val))

        hou.ui.addEventLoopCallback(self.__event_loop_callback)

    def deinit(self):
        hou.ui.removeEventLoopCallback(self.__event_loop_callback)

    def set_tan_handle_angles(self):
        self.__segment.edit_pt0().set_tan_handle_angle(0.0)
        self.__segment.edit_pt1().set_tan_handle_angle(0.0)

    def set_tan_handle_lens(self):
        self.__segment.edit_pt0().set_tan_handle_len(0.5)
        self.__segment.edit_pt1().set_tan_handle_len(0.5)

    def set_tan_handle_heights(self):
        self.__segment.edit_pt0().set_tan_handle_height(0.0)
        self.__segment.edit_pt1().set_tan_handle_height(0.0)

    def __event_loop_callback(self):
        if not hou.selectedNodes():
            self.__disable_segment("Please select a Curve node.")

            return

        node_selected = hou.selectedNodes()[0]

        if node_selected.type().name() != "curve::2.0":
            self.__disable_segment("Please select a Curve node.")

            return

        param_outputtype = node_selected.parm("outputtype")
        prim_type = param_outputtype.eval()

        if prim_type != 2:
            self.__disable_segment("Please set the Primitive Type to Bezier Curve.")

            return

        scene_viewer = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)

        if scene_viewer.currentState() != "sidefx_curve":
            self.__disable_segment("Please select the Handles tool.")

            return

        param_activepoints = node_selected.parm("activepoints")
        active_pt_nums = param_activepoints.eval()
        m = re.fullmatch(r"(\d+) (\d+)", active_pt_nums)

        if not m:
            self.__disable_segment("Please select a segment.")

            return

        active_pt_num0 = min(int(m.group(1)), int(m.group(2)))
        active_pt_num1 = max(int(m.group(1)), int(m.group(2)))

        edit_pt_num0 = 0
        tan_handle_num0 = 0
        edit_pt_num1 = 0
        tan_handle_num1 = 0
        b_is_found = False
        geo_selected = node_selected.geometry()

        for prim in geo_selected.prims():
            segment_count = (len(prim.vertices()) - 1) // 3

            for segment_num in range(segment_count):
                edit_pt_num0 = prim.vertices()[segment_num * 3 + 0].point().number()
                tan_handle_num0 = prim.vertices()[segment_num * 3 + 1].point().number()
                edit_pt_num1 = prim.vertices()[segment_num * 3 + 3].point().number()
                tan_handle_num1 = prim.vertices()[segment_num * 3 + 2].point().number()

                min_edit_pt_num = min(edit_pt_num0, edit_pt_num1)
                max_edit_pt_num = max(edit_pt_num0, edit_pt_num1)

                if (min_edit_pt_num == active_pt_num0)\
                    and (max_edit_pt_num == active_pt_num1):
                    b_is_found = True

                    break

            if b_is_found:
                break

        if not b_is_found:
            self.__disable_segment("Please select a segment.")

            return

        self.__set_message("")
        self.__node_path = node_selected.path()
        self.__segment.edit_pt0().set_edit_pt_num(edit_pt_num0)
        self.__segment.edit_pt0().set_tan_handle_num(tan_handle_num0)
        self.__segment.edit_pt0().set_edit_pt_pos(geo_selected.points()[edit_pt_num0].position())
        self.__segment.edit_pt0().set_tan_handle_pos(geo_selected.points()[tan_handle_num0].position())
        self.__segment.edit_pt1().set_edit_pt_num(edit_pt_num1)
        self.__segment.edit_pt1().set_tan_handle_num(tan_handle_num1)
        self.__segment.edit_pt1().set_edit_pt_pos(geo_selected.points()[edit_pt_num1].position())
        self.__segment.edit_pt1().set_tan_handle_pos(geo_selected.points()[tan_handle_num1].position())

    def __disable_segment(self, message):
        self.__set_message(message)
        self.__node_path = ""
        self.__segment.disable()

    def __set_pt_pos(self, num, new_pos):
        if not self.__node_path:
            return

        node = hou.node(self.__node_path)
        geo = node.geometry()

        old_pos = geo.points()[num].position()
        translate = new_pos - old_pos

        param_active_pt_nums = node.parm("activepoints")
        param_active_pt_nums.set(str(num))

        param_translate = node.parmTuple("translate")
        param_translate.set(translate)

        param_mode = node.parm("mode")
        mode = param_mode.eval()

        if mode == 0:
            param_mode.set(1)
            param_mode.set(0)
        else:
            param_mode.set(0)
            param_mode.set(1)

def set_b_is_widget_enabled_in_layout_rec(layout, val):
    for i in range(layout.count()):
        item = layout.itemAt(i)

        if item.widget():
            item.widget().setEnabled(val)
        elif item.layout():
            set_b_is_widget_enabled_in_layout_rec(item.layout(), val)

class FloatLineEditWrapper(QtCore.QObject):
    on_val_changed = QtCore.Signal(float)

    def __init__(self, line_edit, min_val=-float("inf"), max_val=float("inf"), decimal_count=6):
        super(FloatLineEditWrapper, self).__init__()

        self.__line_edit = line_edit

        self.__line_edit.editingFinished.connect(self.__line_edit_editingFinished)
        self.__line_edit.textChanged.connect(self.__line_edit_textChanged)

        validator = QtGui.QDoubleValidator()
        validator.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator.setDecimals(decimal_count)
        validator.setBottom(min_val)
        validator.setTop(max_val)
        self.__line_edit.setValidator(validator)

        text = self.__fixup(0.0)
        self.__line_edit.setText(text)

    def line_edit(self):
        return self.__line_edit

    def val(self):
        try:
            return float(self.__line_edit.text())
        except:
            return 0.0

    def set_val(self, val):
        text0 = self.__fixup(val)
        text1 = self.__fixup(self.val())

        if text0 != text1:
            self.__line_edit.setText(text0)

    def __line_edit_editingFinished(self):
        text = self.__fixup(self.val())
        self.__line_edit.setText(text)
        self.__line_edit.clearFocus()

    def __line_edit_textChanged(self, text):
        self.on_val_changed.emit(self.val())

    def __fixup(self, f):
        return self.__line_edit.validator().fixup(f"{f:f}")

class FloatSlider(QtCore.QObject):
    on_val_changed = QtCore.Signal(float)

    def __init__(self, slider, min_val=-float("inf"), max_val=float("inf"), decimal_count=6):
        super(FloatSlider, self).__init__()

        self.__multiplier = pow(10, decimal_count)

        self.__slider = slider
        self.__slider.setMinimum(min_val * self.__multiplier)
        self.__slider.setMaximum(max_val * self.__multiplier)
        self.__slider.valueChanged.connect(self.__slider_valueChanged)

    def slider(self):
        return self.__slider

    def val(self):
        return self.__slider.value() / self.__multiplier
    
    def set_val(self, val):
        self.__slider.setValue(val * self.__multiplier)

    def __slider_valueChanged(self, value):
        self.on_val_changed.emit(self.val())

class MainView(QtWidgets.QMainWindow):
    def __init__(self, main_model, parent=None):
        super(MainView, self).__init__(parent)

        self.__main_model = main_model

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)
        self.setWindowTitle("Bezier Curve Tool")

        for plane in Plane:
            self.__ui.combo_box_plane.addItem(plane.value)

        def f(text):
            if text == Plane.XY.value:
                self.__main_model.segment().set_plane_normal(Vector3Utils.forward())
            elif text == Plane.YZ.value:
                self.__main_model.segment().set_plane_normal(Vector3Utils.left())
            else:
                self.__main_model.segment().set_plane_normal(Vector3Utils.up())

        self.__ui.combo_box_plane.currentTextChanged.connect(f)

        def f(val):
            self.__ui.label_message.setText(val)
            set_b_is_widget_enabled_in_layout_rec(self.__ui.verticalLayout_editPt0, val == "")
            set_b_is_widget_enabled_in_layout_rec(self.__ui.verticalLayout_editPt1, val == "")
            self.__ui.button_set_angles.setEnabled(val == "")
            self.__ui.button_set_lens.setEnabled(val == "")
            self.__ui.button_set_heights.setEnabled(val == "")

        self.__main_model.on_message_changed.connect(f)

        self.__flew_edit_pt_pos_x0 = FloatLineEditWrapper(self.__ui.line_edit_edit_pt_pos_x0, decimal_count=DECIMAL_COUNT)
        self.__flew_edit_pt_pos_y0 = FloatLineEditWrapper(self.__ui.line_edit_edit_pt_pos_y0, decimal_count=DECIMAL_COUNT)
        self.__flew_edit_pt_pos_z0 = FloatLineEditWrapper(self.__ui.line_edit_edit_pt_pos_z0, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_pos_x0 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_pos_x0, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_pos_y0 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_pos_y0, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_pos_z0 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_pos_z0, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_angle0 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_angle0, -180.0, 180.0, DECIMAL_COUNT)
        self.__fsw_tan_handle_angle0 = FloatSlider(self.__ui.slider_tan_handle_angle0, -180.0, 180.0, DECIMAL_COUNT)
        self.__flew_tan_handle_len0 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_len0, 0.0, 1.0, DECIMAL_COUNT)
        self.__fsw_tan_handle_len0 = FloatSlider(self.__ui.slider_tan_handle_len0, 0.0, 1.0, DECIMAL_COUNT)
        self.__flew_tan_handle_height0 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_height0, decimal_count=DECIMAL_COUNT)

        self.__setup_edit_pt_widgets(
            self.__main_model.segment().edit_pt0(),
            self.__ui.label_edit_pt_num0,
            self.__ui.label_tan_handle_num0,
            self.__flew_edit_pt_pos_x0,
            self.__flew_edit_pt_pos_y0,
            self.__flew_edit_pt_pos_z0,
            self.__flew_tan_handle_pos_x0,
            self.__flew_tan_handle_pos_y0,
            self.__flew_tan_handle_pos_z0,
            self.__flew_tan_handle_angle0,
            self.__fsw_tan_handle_angle0,
            self.__flew_tan_handle_len0,
            self.__fsw_tan_handle_len0,
            self.__flew_tan_handle_height0
        )

        self.__flew_edit_pt_pos_x1 = FloatLineEditWrapper(self.__ui.line_edit_edit_pt_pos_x1, decimal_count=DECIMAL_COUNT)
        self.__flew_edit_pt_pos_y1 = FloatLineEditWrapper(self.__ui.line_edit_edit_pt_pos_y1, decimal_count=DECIMAL_COUNT)
        self.__flew_edit_pt_pos_z1 = FloatLineEditWrapper(self.__ui.line_edit_edit_pt_pos_z1, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_pos_x1 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_pos_x1, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_pos_y1 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_pos_y1, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_pos_z1 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_pos_z1, decimal_count=DECIMAL_COUNT)
        self.__flew_tan_handle_angle1 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_angle1, -180.0, 180.0, DECIMAL_COUNT)
        self.__fsw_tan_handle_angle1 = FloatSlider(self.__ui.slider_tan_handle_angle1, -180.0, 180.0, DECIMAL_COUNT)
        self.__flew_tan_handle_len1 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_len1, 0.0, 1.0, DECIMAL_COUNT)
        self.__fsw_tan_handle_len1 = FloatSlider(self.__ui.slider_tan_handle_len1, 0.0, 1.0, DECIMAL_COUNT)
        self.__flew_tan_handle_height1 = FloatLineEditWrapper(self.__ui.line_edit_tan_handle_height1, decimal_count=DECIMAL_COUNT)

        self.__setup_edit_pt_widgets(
            self.__main_model.segment().edit_pt1(),
            self.__ui.label_edit_pt_num1,
            self.__ui.label_tan_handle_num1,
            self.__flew_edit_pt_pos_x1,
            self.__flew_edit_pt_pos_y1,
            self.__flew_edit_pt_pos_z1,
            self.__flew_tan_handle_pos_x1,
            self.__flew_tan_handle_pos_y1,
            self.__flew_tan_handle_pos_z1,
            self.__fsw_tan_handle_angle1,
            self.__flew_tan_handle_angle1,
            self.__fsw_tan_handle_len1,
            self.__flew_tan_handle_len1,
            self.__flew_tan_handle_height1
        )

        self.__ui.button_set_angles.clicked.connect(self.__main_model.set_tan_handle_angles)
        self.__ui.button_set_lens.clicked.connect(self.__main_model.set_tan_handle_lens)
        self.__ui.button_set_heights.clicked.connect(self.__main_model.set_tan_handle_heights)

    def closeEvent(self, ev):
        self.__main_model.deinit()

    def __setup_edit_pt_widgets(
        self,
        edit_pt,
        label_edit_pt_num,
        label_tan_handle_num,
        flew_edit_pt_pos_x,
        flew_edit_pt_pos_y,
        flew_edit_pt_pos_z,
        flew_tan_handle_pos_x,
        flew_tan_handle_pos_y,
        flew_tan_handle_pos_z,
        fsw_tan_handle_angle,
        flew_tan_handle_angle,
        fsw_tan_handle_len,
        flew_tan_handle_len,
        flew_tan_handle_height):

        edit_pt.on_edit_pt_num_changed.connect(lambda val: label_edit_pt_num.setText(str(val)))

        edit_pt.on_tan_handle_num_changed.connect(lambda val: label_tan_handle_num.setText(str(val)))

        def f(val):
            edit_pt_pos = hou.Vector3(edit_pt.edit_pt_pos())
            edit_pt_pos[0] = val
            edit_pt.set_edit_pt_pos(edit_pt_pos)

        flew_edit_pt_pos_x.on_val_changed.connect(f)

        def f(val):
            edit_pt_pos = hou.Vector3(edit_pt.edit_pt_pos())
            edit_pt_pos[1] = val
            edit_pt.set_edit_pt_pos(edit_pt_pos)

        flew_edit_pt_pos_y.on_val_changed.connect(f)

        def f(val):
            edit_pt_pos = hou.Vector3(edit_pt.edit_pt_pos())
            edit_pt_pos[2] = val
            edit_pt.set_edit_pt_pos(edit_pt_pos)

        flew_edit_pt_pos_z.on_val_changed.connect(f)

        def f(val):
            flew_edit_pt_pos_x.set_val(val.x())
            flew_edit_pt_pos_y.set_val(val.y())
            flew_edit_pt_pos_z.set_val(val.z())

        edit_pt.on_edit_pt_pos_changed.connect(f)

        def f(val):
            tan_handle_pos = hou.Vector3(edit_pt.tan_handle_pos())
            tan_handle_pos[0] = val
            edit_pt.set_tan_handle_pos(tan_handle_pos)

        flew_tan_handle_pos_x.on_val_changed.connect(f)

        def f(val):
            tan_handle_pos = hou.Vector3(edit_pt.tan_handle_pos())
            tan_handle_pos[1] = val
            edit_pt.set_tan_handle_pos(tan_handle_pos)

        flew_tan_handle_pos_y.on_val_changed.connect(f)

        def f(val):
            tan_handle_pos = hou.Vector3(edit_pt.tan_handle_pos())
            tan_handle_pos[2] = val
            edit_pt.set_tan_handle_pos(tan_handle_pos)

        flew_tan_handle_pos_z.on_val_changed.connect(f)

        def f(val):
            flew_tan_handle_pos_x.set_val(val.x())
            flew_tan_handle_pos_y.set_val(val.y())
            flew_tan_handle_pos_z.set_val(val.z())

        edit_pt.on_tan_handle_pos_changed.connect(f)

        fsw_tan_handle_angle.on_val_changed.connect(lambda val: edit_pt.set_tan_handle_angle(val))
        edit_pt.on_tan_handle_angle_changed.connect(lambda val: fsw_tan_handle_angle.set_val(val))

        flew_tan_handle_angle.on_val_changed.connect(lambda val: edit_pt.set_tan_handle_angle(val))
        edit_pt.on_tan_handle_angle_changed.connect(lambda val: flew_tan_handle_angle.set_val(val))

        fsw_tan_handle_len.on_val_changed.connect(lambda val: edit_pt.set_tan_handle_len(val))
        edit_pt.on_tan_handle_len_changed.connect(lambda val: fsw_tan_handle_len.set_val(val))

        flew_tan_handle_len.on_val_changed.connect(lambda val: edit_pt.set_tan_handle_len(val))
        edit_pt.on_tan_handle_len_changed.connect(lambda val: flew_tan_handle_len.set_val(val))

        flew_tan_handle_height.on_val_changed.connect(lambda val: edit_pt.set_tan_handle_height(val))
        edit_pt.on_tan_handle_height_changed.connect(lambda val: flew_tan_handle_height.set_val(val))

def show_main_view():
    main_model = MainModel()
    main_view = MainView(main_model, hou.qt.mainWindow())
    main_view.show()

show_main_view()
