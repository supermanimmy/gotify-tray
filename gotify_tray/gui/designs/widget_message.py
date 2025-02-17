# Form implementation generated from reading ui file 'gotify_tray/gui/designs\widget_message.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 90)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_frame = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_frame.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_frame.setContentsMargins(0, 0, -1, 0)
        self.gridLayout_frame.setVerticalSpacing(3)
        self.gridLayout_frame.setObjectName("gridLayout_frame")
        self.label_message = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_message.sizePolicy().hasHeightForWidth())
        self.label_message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_message.setFont(font)
        self.label_message.setWordWrap(True)
        self.label_message.setOpenExternalLinks(True)
        self.label_message.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_message.setObjectName("label_message")
        self.gridLayout_frame.addWidget(self.label_message, 4, 3, 1, 4)
        self.pb_delete = QtWidgets.QPushButton(self.frame)
        self.pb_delete.setText("")
        self.pb_delete.setFlat(True)
        self.pb_delete.setObjectName("pb_delete")
        self.gridLayout_frame.addWidget(self.pb_delete, 1, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_frame.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 2, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.gridLayout_frame.addItem(spacerItem1, 0, 3, 1, 4)
        self.label_date = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_date.setFont(font)
        self.label_date.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_date.setObjectName("label_date")
        self.gridLayout_frame.addWidget(self.label_date, 1, 5, 1, 1)
        self.label_title = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_title.setFont(font)
        self.label_title.setWordWrap(True)
        self.label_title.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.label_title.setObjectName("label_title")
        self.gridLayout_frame.addWidget(self.label_title, 1, 3, 1, 1)
        self.label_image = QtWidgets.QLabel(self.frame)
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout_frame.addWidget(self.label_image, 1, 2, 1, 1)
        self.label_priority = QtWidgets.QLabel(self.frame)
        self.label_priority.setMaximumSize(QtCore.QSize(6, 16777215))
        self.label_priority.setText("")
        self.label_priority.setObjectName("label_priority")
        self.gridLayout_frame.addWidget(self.label_priority, 0, 1, 5, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_message.setText(_translate("Form", "TextLabel"))
        self.label_date.setText(_translate("Form", "Date"))
        self.label_title.setText(_translate("Form", "Title"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
