""" 
    Create a camera app using PyQt5
    Author:  Farzana Pomy
    Purpose:    To learn how to use PyQt5 to create a camera app
    Created:    25/06/2023
"""


import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import QWidget
import cv2


class Window(QWidget):
    def __init__(self):
        # initialize all parent and child classes
        super().__init__()
        # window variable
        self.window_width, self.window_height = 600, 450
        # image variable
        self.image_width, self.image_height = 600, 450

        # set up the window
        self.setWindowTitle("Camera App")
        self.setGeometry(100, 100, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)
        self.ui()

    def ui(self):
        """ Contains all the ui elements. Like buttons, labels, etc. """
        # image label
        self.img_label = QLabel(self)
        self.img_label.setGeometry(0, 0, self.image_width, self.image_height)
        self.show()

    def update(self):
        """ Updates the ui elements """
        pass

    def save_img(self):
        """ Saves the image from camera"""
        pass

    def record(self):
        """ Records the video """
        pass


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
