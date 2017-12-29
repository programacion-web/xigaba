#!/usr/bin/env python3

# Program created for play audios of time in zapoteco'
#
# Created by: Python 3.6, PyQt5 5.9.2.
#
# Author: Raul Espinosa raul@ninja-code.de
#
# WARNING! All changes made in this file will be lost!
# 
# Version 0.2 GUI

import time
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(383, 263)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 127, 168))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(46, 52, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(138, 226, 52))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        Form.setPalette(palette)
        Form.setPalette(palette)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 361, 181))
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(110, 240, 160, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setRange(0, 100)
        self.horizontalSlider.setSingleStep(1)
        self.runButton = QtWidgets.QPushButton(Form)
        self.runButton.setGeometry(QtCore.QRect(50, 180, 80, 25))
        self.runButton.setObjectName("runButton")
        self.runButton1 = QtWidgets.QPushButton(Form)
        self.runButton1.setGeometry(QtCore.QRect(250, 180, 80, 25))
        self.runButton1.setObjectName("runButton1")
        self.runButton1.setEnabled(False)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 220, 55, 17))
        self.label_2.setObjectName("label_2")
        self.timer = QtCore.QTimer(Form)
        self.timer.start(1000)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(200, 0, 180, 61))
        self.lcdNumber.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.display(time.strftime("%H" + ":" + "%M" + ":" + "%S"))
        self.lcdNumber.setObjectName("lcdNumber")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(150, 180, 71, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(92, 53, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 185, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 53, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 185, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 53, 102))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(114, 159, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.spinBox.setPalette(palette)
        self.spinBox.setSuffix("min")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "XIGABA"))
        Form.setToolTip(_translate("Form",
                                   "<html><head/><body><pre style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'monospace\'; background-color:#ffffff;\">Creado con Software Libre.</span></pre></body></html>"))
        self.label.setToolTip(_translate("Form", "<html><head/><body><p>Dictador de horario.</p></body></html>"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><pre align=\"center\" style=\" margin-top:15px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><a name=\"taag_output_text\"/><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\">)</span><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\"> (                               </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\"> ( /( )\\ ) (       (      (    (      </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\"> )\\()|()/( )\\ )    )\\   ( )\\   )\\     </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\">((_)\\ /(_)|()/( ((((_)( )((_|(((_)(   </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\">__((_|_))  /(_))_)\\ _ )((_)_ )\\ _ )\\  </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\">\\ \\/ /_ _|(_)) __(_)_\\(_) _ )(_)_\\(_) </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\"> &gt;  &lt; | |   | (_ |/ _ \\ | _ \\ / _ \\   </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; color:#555753; background-color:#729fcf;\">/_/\\_\\___|   \\___/_/ \\_\\|___//_/ \\_\\  </span></pre><pre align=\"center\" style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#729fcf;\"><span style=\" font-family:\'monospace\'; font-size:6pt; color:#555753; background-color:#729fcf;\">version 0.2 GUI</span></pre></body></html>"))
        self.runButton.setText(_translate("Form", "Iniciar"))
        self.runButton1.setText(_translate("Form", "Detener"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><pre align=\"center\" style=\" margin-top:0px; margin-bottom:15px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#000000;\"><a name=\"taag_output_text\"/><span style=\" font-family:\'monospace\'; color:#ef2929; background-color:#000000;\">VOLUMEN</span></pre></body></html>"))


class Widget(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.runButton.clicked.connect(self.iniciar)
        self.runButton1.clicked.connect(self.detener)
        self.timer.timeout.connect(self.update_time)
        self.horizontalSlider.valueChanged.connect(self.valueHandler)
        self.spinBox.value()

    def update_time(self):
        self.lcdNumber.display(time.strftime("%H" + ":" + "%M" + ":" + "%S"))

    def valueHandler(self, value):
        scaledValue = float(value) / 100
        return scaledValue

    def iniciar(self):
    	self.runButton.setEnabled(False)
    	self.spinBox.setEnabled(False)
    	self.runButton1.setEnabled(True)
    	self.runnable = Runnable(self)
    	QtCore.QThreadPool.globalInstance().start(self.runnable)

    def detener(self):
    	self.runButton.setEnabled(True)
    	self.runButton1.setEnabled(False)
    	self.runnable = Runnable(self)
    	QtCore.QThreadPool.globalInstance().clear(self.runnable)


class Runnable(QtCore.QRunnable):
    def __init__(self, w, *args, **kwargs):
        QtCore.QRunnable.__init__(self, *args, **kwargs)
        self.w = w

    def run(self):
        while True:
            time.sleep(0.5)
            second_test = time.strftime('%S')
            minute_test = time.strftime('%M')
            hour_test = time.strftime('%H')
            tiempo = time.strftime("%H" + ":" + "%M" + ":" + "%S")
            self.position_initial = self.w.horizontalSlider.value()
            scaledValue = float(self.position_initial) / 100
            min_constancia = self.w.spinBox.value()
            minuter = int(minute_test) % int(min_constancia) == 0

            QtCore.QMetaObject.invokeMethod(self.w.lcdNumber, "display",
                                            QtCore.Qt.QueuedConnection,
                                            QtCore.Q_ARG(str, tiempo))
            if int(minute_test) == int(00) and int(second_test) == int(00):
                filen = 'HRS' + hour_test + '_O.mp3.mp3'
                print(filen)
                subprocess.Popen(["play", filen, "vol", scaledValue]).communicate()
            #elif int(second_test) == int(00):
            elif minuter == True and int(second_test) == int(00):
                filen = 'HRS' + hour_test + '.mp3'
                filen2 = 'MIN' + minute_test + '.mp3.mp3'
                print(filen)
                print(filen2)
                subprocess.Popen(["play", filen, "vol", str(scaledValue)]).communicate()
                subprocess.Popen(["play", filen2, "vol", str(scaledValue)]).communicate()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())
