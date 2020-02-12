#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog,QMainWindow
from PyQt5.uic import loadUi


class probe2(QMainWindow):
	def __init__(self):
		super(probe2,self).__init__()
		loadUi('probe_2.ui',self)
		self.setWindowTitle('Probe 2')
		self.pushButton.clicked.connect(self.on_pushButton_clicked)
	@pyqtSlot()
	def on_pushButton_clicked(self):
		d_arr = [] # distances array
		d = float(self.entryDist.toPlainText())
		for ang in range(-15,16,2):
			#print(ang)
			valDist = d/math.cos(ang*math.pi/180)
			d_arr.append(format(valDist,'.2f'))
		d_arr_str = ''
		for distV in d_arr:
			d_arr_str = d_arr_str + distV + ' '
		self.label.setText(d_arr_str)
		#print(float(self.entryDist.toPlainText()))

	

app = QApplication(sys.argv)
widget = probe2()
widget.show()
sys.exit(app.exec_())
