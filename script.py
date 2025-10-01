# -*- coding: utf-8 -*-
import hou
import math
import re
from enum import Enum
from PySide6 import QtCore, QtGui, QtWidgets

class Vector3(object):
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

class Plane(Enum):
    XY = "XY (Front)"
    YZ = "YZ (Right)"
    ZX = "ZX (Top)"

class EditPt(object):
    def __init__(self):
        super(EditPt, self).__init__()

        self.edit_pt_num = 0
        self.tan_handle_num = 0
        self.tan_handle_angle = 0.0
        self.tan_handle_len = 0.0
        self.tan_handle_height = 0.0

class Segment(object):
    def __init__(self):
        super(Segment, self).__init__()

        self.edit_pt0 = EditPt()
        self.edit_pt1 = EditPt()

    def __eq__(self, other):
        min_num0 = min(self.edit_pt0.edit_pt_num, self.edit_pt1.edit_pt_num)
        max_num0 = max(self.edit_pt0.edit_pt_num, self.edit_pt1.edit_pt_num)

        min_num1 = min(other.edit_pt0.edit_pt_num, other.edit_pt1.edit_pt_num)
        max_num1 = max(other.edit_pt0.edit_pt_num, other.edit_pt1.edit_pt_num)

        return (min_num0 == min_num1)\
            and (max_num0 == max_num1)

    def __ne__(self, other):
        min_num0 = min(self.edit_pt0.edit_pt_num, self.edit_pt1.edit_pt_num)
        max_num0 = max(self.edit_pt0.edit_pt_num, self.edit_pt1.edit_pt_num)

        min_num1 = min(other.edit_pt0.edit_pt_num, other.edit_pt1.edit_pt_num)
        max_num1 = max(other.edit_pt0.edit_pt_num, other.edit_pt1.edit_pt_num)

        return (min_num0 != min_num1)\
            or (max_num0 != max_num1)

class Curve(object):
    def __init__(self):
        super(Curve, self).__init__()

        self.segments = []

def project_vec_on_plane(vec, normal):
    return vec - vec.dot(normal) / normal.dot(normal) * normal

def get_up_vec(forward_vec):
    up_vec = forward_vec.cross(Vector3.left())

    if up_vec.y() < 0.0:
        up_vec *= -1

    return up_vec

def get_curves(geo):
    curves = []

    for prim in geo.prims():
        curve = Curve()

        segment_count = (len(prim.vertices()) - 1) // 3

        for segment_num in range(segment_count):
            segment = Segment()

            segment.edit_pt0.edit_pt_num = prim.vertices()[segment_num * 3 + 0].point().number()
            segment.edit_pt0.tan_handle_num = prim.vertices()[segment_num * 3 + 1].point().number()
            segment.edit_pt1.edit_pt_num = prim.vertices()[segment_num * 3 + 3].point().number()
            segment.edit_pt1.tan_handle_num = prim.vertices()[segment_num * 3 + 2].point().number()

            curve.segments.append(segment)

        curves.append(curve)

    return curves

def set_detailed_segment_param(geo, plane_normal, segment):
    edit_pt_pos0 = geo.points()[segment.edit_pt0.edit_pt_num].position()
    tan_handle_pos0 = geo.points()[segment.edit_pt0.tan_handle_num].position()
    edit_pt_pos1 = geo.points()[segment.edit_pt1.edit_pt_num].position()
    tan_handle_pos1 = geo.points()[segment.edit_pt1.tan_handle_num].position()

    quat0 = hou.Quaternion()
    quat0.setToVectors(plane_normal, Vector3.forward())
    up_vec = get_up_vec(plane_normal)
    up_vec_rotated = quat0.rotate(up_vec)
    quat1 = hou.Quaternion()
    quat1.setToVectors(up_vec_rotated, Vector3.up())
    quat = quat0 * quat1

    edit_pt_pos0_rotated = quat.rotate(edit_pt_pos0)
    tan_handle_pos0_rotated = quat.rotate(tan_handle_pos0)
    edit_pt_pos1_rotated = quat.rotate(edit_pt_pos1)
    tan_handle_pos1_rotated = quat.rotate(tan_handle_pos1)

    edit_pt_pos0_projected = project_vec_on_plane(edit_pt_pos0_rotated, Vector3.forward())
    tan_handle_pos0_projected = project_vec_on_plane(tan_handle_pos0_rotated, Vector3.forward())
    edit_pt_pos1_projected = project_vec_on_plane(edit_pt_pos1_rotated, Vector3.forward())
    tan_handle_pos1_projected = project_vec_on_plane(tan_handle_pos1_rotated, Vector3.forward())

    diff00 = edit_pt_pos1_projected - edit_pt_pos0_projected

    if diff00.isAlmostEqual(Vector3.zero()):
        segment.edit_pt0.tan_handle_angle = 0.0
        segment.edit_pt0.tan_handle_len = 0.0
        segment.edit_pt0.tan_handle_height = 0.0
    else:
        diff01 = tan_handle_pos0_projected - edit_pt_pos0_projected

        angle00 = math.degrees(math.atan2(diff00.y(), diff00.x()))
        angle01 = math.degrees(math.atan2(diff01.y(), diff01.x()))
        segment.edit_pt0.tan_handle_angle = get_delta_angle(angle00, angle01)

        segment.edit_pt0.tan_handle_len = diff01.length() / diff00.length()

        segment.edit_pt0.tan_handle_height = tan_handle_pos0_rotated.z()

    diff10 = edit_pt_pos0_projected - edit_pt_pos1_projected

    if diff10.isAlmostEqual(Vector3.zero()):
        segment.edit_pt1.tan_handle_angle = 0.0
        segment.edit_pt1.tan_handle_len = 0.0
        segment.edit_pt1.tan_handle_height = 0.0
    else:
        diff11 = tan_handle_pos1_projected - edit_pt_pos1_projected

        angle10 = math.degrees(math.atan2(diff10.y(), diff10.x()))
        angle11 = math.degrees(math.atan2(diff11.y(), diff11.x()))
        segment.edit_pt1.tan_handle_angle = get_delta_angle(angle10, angle11)

        segment.edit_pt1.tan_handle_len = diff11.length() / diff10.length()

        segment.edit_pt1.tan_handle_height = tan_handle_pos1_rotated.z()

def get_tan_handle_pos(geo, plane_normal, segment, edit_pt_index):
    edit_pt0 = EditPt()
    edit_pt1 = EditPt()

    if edit_pt_index == 0:
        edit_pt0 = segment.edit_pt0
        edit_pt1 = segment.edit_pt1
    else:
        edit_pt0 = segment.edit_pt1
        edit_pt1 = segment.edit_pt0

    edit_pt_pos0 = geo.points()[edit_pt0.edit_pt_num].position()
    edit_pt_pos1 = geo.points()[edit_pt1.edit_pt_num].position()

    quat00 = hou.Quaternion()
    quat00.setToVectors(plane_normal, Vector3.forward())
    up_vec = get_up_vec(plane_normal)
    up_vec_rotated = quat00.rotate(up_vec)
    quat01 = hou.Quaternion()
    quat01.setToVectors(up_vec_rotated, Vector3.up())
    quat0 = quat00 * quat01

    edit_pt_pos0_rotated = quat0.rotate(edit_pt_pos0)
    edit_pt_pos1_rotated = quat0.rotate(edit_pt_pos1)

    edit_pt_pos0_projected = project_vec_on_plane(edit_pt_pos0_rotated, Vector3.forward())
    edit_pt_pos1_projected = project_vec_on_plane(edit_pt_pos1_rotated, Vector3.forward())

    quat1 = hou.Quaternion(edit_pt0.tan_handle_angle, Vector3.forward())

    tan_handle_pos0_projected = quat1.rotate((edit_pt_pos1_projected - edit_pt_pos0_projected) * edit_pt0.tan_handle_len) + edit_pt_pos0_projected

    tan_handle_pos0_rotated = tan_handle_pos0_projected + hou.Vector3(0.0, 0.0, edit_pt0.tan_handle_height)

    return quat0.inverse().rotate(tan_handle_pos0_rotated)

def normalize_angle(angle):
    a = angle

    while a > 180.0:
        a -= 360.0

    while a < -180.0:
        a += 360.0

    return a

def get_delta_angle(current, target):
    c = normalize_angle(current)
    t = normalize_angle(target)

    delta_angle = t - c

    if delta_angle > 180.0:
        delta_angle = t - 360.0 - c
    elif delta_angle < -180.0:
        delta_angle = t + 360.0 - c

    return delta_angle

def create_header(*args, **kwargs):
    header = QtWidgets.QLabel(*args, **kwargs)
    header.setStyleSheet("margin-right: 5px;")

    return header

def create_separator(parent=None):
    separator = QtWidgets.QFrame(parent)
    separator.setFrameShape(QtWidgets.QFrame.HLine)
    separator.setFrameShadow(QtWidgets.QFrame.Sunken)
    separator.setFixedHeight(2)

    return separator

def set_float_to_line_edit(line_edit, f):
    text = line_edit.validator().fixup(f"{f:f}")
    line_edit.setText(text)

class FloatSliderLineEditLinker(QtCore.QObject):
    on_val_changed = QtCore.Signal(float)

    def __init__(self, slider, line_edit):
        super(FloatSliderLineEditLinker, self).__init__()

        self.__b_is_setting_val = False

        self.__line_edit = line_edit
        self.__line_edit.textChanged.connect(self.line_edit_textChanged)
        self.__focus_out_event = self.__line_edit.focusOutEvent
        self.__line_edit.focusOutEvent = self.__line_edit_focusOutEvent

        self.__slider = slider
        val_multiplier = self.__get_val_multiplier()
        self.__slider.setMinimum(self.__line_edit.validator().bottom() * val_multiplier)
        self.__slider.setMaximum(self.__line_edit.validator().top() * val_multiplier)
        self.__slider.valueChanged.connect(self.slider_valueChanged)

    @property
    def val(self):
        try:
            return float(self.__line_edit.text())
        except:
            pass

        return 0.0

    @val.setter
    def val(self, v):
        if self.__b_is_setting_val:
            return

        self.__b_is_setting_val = True

        val = v * self.__get_val_multiplier()
        self.__slider.setValue(val)

        set_float_to_line_edit(self.__line_edit, v)

        self.on_val_changed.emit(self.val)

        self.__b_is_setting_val = False

    def slider_valueChanged(self, value):
        if self.__b_is_setting_val:
            return

        self.__b_is_setting_val = True

        val = value / self.__get_val_multiplier()
        set_float_to_line_edit(self.__line_edit, val)

        self.on_val_changed.emit(self.val)

        self.__b_is_setting_val = False

    def line_edit_textChanged(self, text):
        if self.__b_is_setting_val:
            return

        self.__b_is_setting_val = True

        try:
            val = float(text) * self.__get_val_multiplier()
            self.__slider.setValue(val)

            self.on_val_changed.emit(self.val)
        except:
            pass

        self.__b_is_setting_val = False

    def __line_edit_focusOutEvent(self, event):
        self.__focus_out_event(event)

        if self.__b_is_setting_val:
            return

        self.__b_is_setting_val = True

        val = self.__slider.value() / self.__get_val_multiplier()
        set_float_to_line_edit(self.__line_edit, val)

        self.on_val_changed.emit(self.val)

        self.__b_is_setting_val = False

    def __get_val_multiplier(self):
        return pow(10, self.__line_edit.validator().decimals())

class EditPtWidget(QtWidgets.QWidget):
    on_tan_handle_angle_changed = QtCore.Signal(float)
    on_tan_handle_len_changed = QtCore.Signal(float)
    on_tan_handle_height_changed = QtCore.Signal(float)

    def __init__(self, parent=None, header_size_x=120, decimal_count=6):
        super(EditPtWidget, self).__init__(parent)

        layout_root = QtWidgets.QGridLayout(self)
        layout_root.setColumnMinimumWidth(0, header_size_x)
        layout_root.setColumnStretch(0, 0)
        layout_root.setColumnStretch(1, 1)
        layout_root.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout_root)

        row_index = 0

        header_edit_pt_num0 = create_header("Edit Pt Num", self)
        header_edit_pt_num0.setAlignment(QtCore.Qt.AlignRight)
        layout_root.addWidget(header_edit_pt_num0, row_index, 0, 1, 1)

        self.__label_edit_pt_num1 = QtWidgets.QLabel("0", self)
        layout_root.addWidget(self.__label_edit_pt_num1, row_index, 1, 1, 2)

        row_index += 1

        header_tan_handle_num0 = create_header("Tan Handle Num", self)
        header_tan_handle_num0.setAlignment(QtCore.Qt.AlignRight)
        layout_root.addWidget(header_tan_handle_num0, row_index, 0, 1, 1)

        self.__label_tan_handle_num1 = QtWidgets.QLabel("0", self)
        layout_root.addWidget(self.__label_tan_handle_num1, row_index, 1, 1, 2)

        row_index += 1

        header_tan_handle_angle = create_header("Tan Handle Angle", self)
        header_tan_handle_angle.setAlignment(QtCore.Qt.AlignRight)
        layout_root.addWidget(header_tan_handle_angle, row_index, 0, 1, 1)

        slider_tan_handle_angle = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        layout_root.addWidget(slider_tan_handle_angle, row_index, 1, 1, 1)

        validator_tan_handle_angle = QtGui.QDoubleValidator()
        validator_tan_handle_angle.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator_tan_handle_angle.setDecimals(decimal_count)
        validator_tan_handle_angle.setBottom(-180.0)
        validator_tan_handle_angle.setTop(180.0)

        line_edit_tan_handle_angle = QtWidgets.QLineEdit("", self)
        line_edit_tan_handle_angle.setValidator(validator_tan_handle_angle)
        layout_root.addWidget(line_edit_tan_handle_angle, row_index, 2, 1, 1)

        self.__fslel_tan_handle_angle = FloatSliderLineEditLinker(slider_tan_handle_angle, line_edit_tan_handle_angle)
        self.__fslel_tan_handle_angle.on_val_changed.connect(self.__fslel_tan_handle_angle_on_val_changed)

        row_index += 1

        header_tan_handle_len = create_header("Tan Handle Length", self)
        header_tan_handle_len.setAlignment(QtCore.Qt.AlignRight)
        layout_root.addWidget(header_tan_handle_len, row_index, 0, 1, 1)

        slider_tan_handle_len = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        layout_root.addWidget(slider_tan_handle_len, row_index, 1, 1, 1)

        validator_tan_handle_len = QtGui.QDoubleValidator()
        validator_tan_handle_len.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator_tan_handle_len.setDecimals(decimal_count)
        validator_tan_handle_len.setBottom(0.0)
        validator_tan_handle_len.setTop(1.0)

        line_edit_tan_handle_len = QtWidgets.QLineEdit("", self)
        line_edit_tan_handle_len.setValidator(validator_tan_handle_len)
        layout_root.addWidget(line_edit_tan_handle_len, row_index, 2, 1, 1)

        self.__fslel_tan_handle_len = FloatSliderLineEditLinker(slider_tan_handle_len, line_edit_tan_handle_len)
        self.__fslel_tan_handle_len.on_val_changed.connect(self.__fslel_tan_handle_len_on_val_changed)

        row_index += 1

        header_tan_handle_height = create_header("Tan Handle Height", self)
        header_tan_handle_height.setAlignment(QtCore.Qt.AlignRight)
        layout_root.addWidget(header_tan_handle_height, row_index, 0, 1, 1)

        validator_tan_handle_height = QtGui.QDoubleValidator()
        validator_tan_handle_height.setNotation(QtGui.QDoubleValidator.Notation.StandardNotation)
        validator_tan_handle_height.setDecimals(decimal_count)

        self.__line_edit_tan_handle_height = QtWidgets.QLineEdit("", self)
        self.__line_edit_tan_handle_height.setValidator(validator_tan_handle_height)
        self.__line_edit_tan_handle_height.textChanged.connect(self.__line_edit_tan_handle_height_textChanged)
        layout_root.addWidget(self.__line_edit_tan_handle_height, row_index, 1, 1, 2)

    @property
    def b_is_enabled(self):
        return self.children()[0].isEnabled()

    @b_is_enabled.setter
    def b_is_enabled(self, val):
        for child in self.children():
            if not isinstance(child, QtWidgets.QLayout):
                child.setEnabled(val)

    def setup(self, edit_pt):
        self.__label_edit_pt_num1.setText(str(edit_pt.edit_pt_num))
        self.__label_tan_handle_num1.setText(str(edit_pt.tan_handle_num))
        self.__fslel_tan_handle_angle.val = edit_pt.tan_handle_angle
        self.__fslel_tan_handle_len.val = edit_pt.tan_handle_len
        set_float_to_line_edit(self.__line_edit_tan_handle_height, edit_pt.tan_handle_height)

    def __fslel_tan_handle_angle_on_val_changed(self, val):
        self.on_tan_handle_angle_changed.emit(val)

    def __fslel_tan_handle_len_on_val_changed(self, val):
        self.on_tan_handle_len_changed.emit(val)

    def __line_edit_tan_handle_height_textChanged(self, text):
        try:
            self.on_tan_handle_height_changed.emit(float(text))
        except:
            pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.__node_path = ""
        self.__plane_normal = Vector3.forward()
        self.__segment = Segment()

        self.setWindowTitle("Bezier Curve Tool")
        self.resize(400, 450)

        scroll_area_central = QtWidgets.QScrollArea(self)
        scroll_area_central.setWidgetResizable(True)
        self.setCentralWidget(scroll_area_central)

        widget_root = QtWidgets.QWidget(self)
        scroll_area_central.setWidget(widget_root)

        layout_root = QtWidgets.QGridLayout(self)
        layout_root.setColumnMinimumWidth(0, 120)
        layout_root.setColumnStretch(0, 0)
        layout_root.setColumnStretch(1, 1)
        widget_root.setLayout(layout_root)

        row_index = 0

        header_plane = create_header("Plane", self)
        header_plane.setAlignment(QtCore.Qt.AlignRight)
        layout_root.addWidget(header_plane, row_index, 0, 1, 1)

        combo_box_plane = QtWidgets.QComboBox()

        for plane in Plane:
            combo_box_plane.addItem(plane.value)

        combo_box_plane.currentTextChanged.connect(self.__combo_box_plane_currentTextChanged)
        layout_root.addWidget(combo_box_plane, row_index, 1, 1, 1)

        row_index += 1

        self.__label_message = QtWidgets.QLabel("", self)
        self.__label_message.setStyleSheet("color: yellow;")
        layout_root.addWidget(self.__label_message, row_index, 0, 1, 2)

        row_index += 1

        separator = create_separator(self)
        layout_root.addWidget(separator, row_index, 0, 1, 2)

        row_index += 1

        self.__edit_pt_widget0 = EditPtWidget(self, 120, 6)
        self.__edit_pt_widget0.on_tan_handle_angle_changed.connect(self.__edit_pt_widget0_on_tan_handle_angle_changed)
        self.__edit_pt_widget0.on_tan_handle_len_changed.connect(self.__edit_pt_widget0_on_tan_handle_len_changed)
        self.__edit_pt_widget0.on_tan_handle_height_changed.connect(self.__edit_pt_widget0_on_tan_handle_height_changed)
        layout_root.addWidget(self.__edit_pt_widget0, row_index, 0, 1, 2)

        row_index += 1

        separator = create_separator(self)
        layout_root.addWidget(separator, row_index, 0, 1, 2)

        row_index += 1

        self.__edit_pt_widget1 = EditPtWidget(self, 120, 6)
        self.__edit_pt_widget1.on_tan_handle_angle_changed.connect(self.__edit_pt_widget1_on_tan_handle_angle_changed)
        self.__edit_pt_widget1.on_tan_handle_len_changed.connect(self.__edit_pt_widget1_on_tan_handle_len_changed)
        self.__edit_pt_widget1.on_tan_handle_height_changed.connect(self.__edit_pt_widget1_on_tan_handle_height_changed)
        layout_root.addWidget(self.__edit_pt_widget1, row_index, 0, 1, 2)

        row_index += 1

        separator = create_separator(self)
        layout_root.addWidget(separator, row_index, 0, 1, 2)

        row_index += 1

        self.__button_set_angles = QtWidgets.QPushButton("Set tan handle angles to 0", self)
        self.__button_set_angles.clicked.connect(self.__button_set_angles_clicked)
        layout_root.addWidget(self.__button_set_angles, row_index, 0, 1, 2)

        row_index += 1

        self.__button_set_lens = QtWidgets.QPushButton("Set tan handle lengths to 0.5", self)
        self.__button_set_lens.clicked.connect(self.__button_set_lens_clicked)
        layout_root.addWidget(self.__button_set_lens, row_index, 0, 1, 2)

        row_index += 1

        self.__button_set_heights = QtWidgets.QPushButton("Set tan handle heights to 0", self)
        self.__button_set_heights.clicked.connect(self.__button_set_heights_clicked)
        layout_root.addWidget(self.__button_set_heights, row_index, 0, 1, 2)

        row_index += 1

        label_dummy = QtWidgets.QLabel("", self)
        label_dummy.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        layout_root.addWidget(label_dummy, row_index, 0, 1, 2)

        self.__update_segment_widgets(True)

        hou.ui.addEventLoopCallback(self.__event_loop_callback)

    def __event_loop_callback(self):
        self.__update_segment_widgets(False)

    def closeEvent(self, ev):
        hou.ui.removeEventLoopCallback(self.__event_loop_callback)

    def __combo_box_plane_currentTextChanged(self, index):
        if index == Plane.XY.value:
            self.__plane_normal = Vector3.forward()
        elif index == Plane.YZ.value:
            self.__plane_normal = Vector3.left()
        else:
            self.__plane_normal = Vector3.up()

        self.__update_segment_widgets(True)

    def __edit_pt_widget0_on_tan_handle_angle_changed(self, val):
        self.__segment.edit_pt0.tan_handle_angle = val
        self.__update_tan_handle_pos(0)

    def __edit_pt_widget0_on_tan_handle_len_changed(self, val):
        self.__segment.edit_pt0.tan_handle_len = val
        self.__update_tan_handle_pos(0)

    def __edit_pt_widget0_on_tan_handle_height_changed(self, val):
        self.__segment.edit_pt0.tan_handle_height = val
        self.__update_tan_handle_pos(0)

    def __edit_pt_widget1_on_tan_handle_angle_changed(self, val):
        self.__segment.edit_pt1.tan_handle_angle = val
        self.__update_tan_handle_pos(1)

    def __edit_pt_widget1_on_tan_handle_len_changed(self, val):
        self.__segment.edit_pt1.tan_handle_len = val
        self.__update_tan_handle_pos(1)

    def __edit_pt_widget1_on_tan_handle_height_changed(self, val):
        self.__segment.edit_pt1.tan_handle_height = val
        self.__update_tan_handle_pos(1)

    def __button_set_angles_clicked(self):
        self.__segment.edit_pt0.tan_handle_angle = 0.0
        self.__update_tan_handle_pos(0)

        self.__segment.edit_pt1.tan_handle_angle = 0.0
        self.__update_tan_handle_pos(1)

        self.__update_segment_widgets(True)

    def __button_set_lens_clicked(self):
        self.__segment.edit_pt0.tan_handle_len = 0.5
        self.__update_tan_handle_pos(0)

        self.__segment.edit_pt1.tan_handle_len = 0.5
        self.__update_tan_handle_pos(1)

        self.__update_segment_widgets(True)

    def __button_set_heights_clicked(self):
        self.__segment.edit_pt0.tan_handle_height = 0.0
        self.__update_tan_handle_pos(0)

        self.__segment.edit_pt1.tan_handle_height = 0.0
        self.__update_tan_handle_pos(1)

        self.__update_segment_widgets(True)

    def __update_tan_handle_pos(self, edit_pt_index):
        node = hou.node(self.__node_path)

        if not node:
            return

        geo = node.geometry()

        edit_pt = EditPt()

        if edit_pt_index == 0:
            edit_pt = self.__segment.edit_pt0
        else:
            edit_pt = self.__segment.edit_pt1

        old_tan_handle_pos = geo.points()[edit_pt.tan_handle_num].position()
        new_tan_handle_pos = get_tan_handle_pos(geo, self.__plane_normal, self.__segment, edit_pt_index)
        translate = new_tan_handle_pos - old_tan_handle_pos

        param_active_pt_nums = node.parm("activepoints")
        param_active_pt_nums.set(str(edit_pt.tan_handle_num))

        param_translate = node.parmTuple("translate")
        param_translate.set(translate)

        param_mode = node.parm("mode")
        mode = param_mode.eval()

        if mode == 0:
            param_mode.set(1)
            param_mode.set(0)
        elif mode == 1:
            param_mode.set(0)
            param_mode.set(1)

    def __disable_segment_widgets(self, message):
        self.__node_path = ""
        self.__segment = Segment()

        self.__label_message.setText(message)

        self.__edit_pt_widget0.b_is_enabled = False
        self.__edit_pt_widget1.b_is_enabled = False

        self.__edit_pt_widget0.setup(self.__segment.edit_pt0)
        self.__edit_pt_widget1.setup(self.__segment.edit_pt1)

        self.__button_set_angles.setEnabled(False)
        self.__button_set_lens.setEnabled(False)
        self.__button_set_heights.setEnabled(False)

    def __update_segment_widgets(self, b_force_update):
        if not hou.selectedNodes():
            self.__disable_segment_widgets("Please select a Curve node.")

            return

        node_selected = hou.selectedNodes()[0]

        if node_selected.type().name() != "curve::2.0":
            self.__disable_segment_widgets("Please select a Curve node.")

            return

        param_outputtype = node_selected.parm("outputtype")
        prim_type = param_outputtype.eval()

        if prim_type != 2:
            self.__disable_segment_widgets("Please set the Primitive Type to Bezier Curve.")

            return

        scene_viewer = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)

        if scene_viewer.currentState() != "sidefx_curve":
            self.__disable_segment_widgets("Please select the Handles tool.")

            return

        param_activepoints = node_selected.parm("activepoints")
        active_pt_nums = param_activepoints.eval()

        m = re.fullmatch(r"(\d+) (\d+)", active_pt_nums)

        if not m:
            self.__disable_segment_widgets("Please select a segment.")

            return

        active_pt_num0 = int(m.group(1))
        active_pt_num1 = int(m.group(2))

        geo_selected = node_selected.geometry()
        curves = get_curves(geo_selected)

        segment = Segment()
        b_is_found = False

        for curve in curves:
            for seg in curve.segments:
                if ((seg.edit_pt0.edit_pt_num == active_pt_num0) and (seg.edit_pt1.edit_pt_num == active_pt_num1))\
                    or ((seg.edit_pt0.edit_pt_num == active_pt_num1) and (seg.edit_pt1.edit_pt_num == active_pt_num0)):
                    segment = seg
                    b_is_found = True

                    break

        if not b_is_found:
            self.__disable_segment_widgets("Please select a segment.")

            return

        node_path_selected = node_selected.path()

        if not b_force_update:
            if (node_path_selected == self.__node_path)\
                and (segment == self.__segment):
                return

        self.__node_path = node_path_selected
        self.__segment = segment
        set_detailed_segment_param(geo_selected, self.__plane_normal, self.__segment)

        self.__label_message.setText("")

        self.__edit_pt_widget0.b_is_enabled = True
        self.__edit_pt_widget1.b_is_enabled = True

        self.__edit_pt_widget0.setup(self.__segment.edit_pt0)
        self.__edit_pt_widget1.setup(self.__segment.edit_pt1)

        self.__button_set_angles.setEnabled(True)
        self.__button_set_lens.setEnabled(True)
        self.__button_set_heights.setEnabled(True)

def show_main_window():
    main_window = MainWindow(hou.qt.mainWindow())
    main_window.show()

show_main_window()
