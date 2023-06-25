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
from PyQt5.QtCore import QTimer
import cv2


class Window(QWidget):
    def __init__(self):
        # initialize all parent and child classes
        super().__init__()
        # window variable
        self.window_width, self.window_height = 600, 450
        # image variable
        self.image_width, self.image_height = 600, 450

        # load icon
        self.capture_icon = QIcon(cam_icon_path)

        # set up the window
        self.setWindowTitle("Camera App")
        self.setGeometry(100, 100, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)

        # set up timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        self.ui()

    def ui(self):
        """ Contains all the ui elements. Like buttons, labels, etc. """

        # layout
        grid = QGridLayout()
        self.setLayout(grid)

        # image label
        self.img_label = QLabel(self)
        self.img_label.setGeometry(0, 0, self.image_width, self.image_height)

        # create Button
        self.capture_btn = QPushButton("Start", self)
        self.capture_btn.setIcon(self.capture_icon)
        self.capture_btn.setStyleSheet(
            " border: 1px solid black; border-radius: 15px; padding: 5px; font-size: 20px; font-weight: bold;")
        self.capture_btn.setFixedSize(100, 50)
        self.capture_btn.clicked.connect(self.save_img)

        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        # add widgets to the layout grid
        grid.addWidget(self.capture_btn, 0, 0)
        grid.addWidget(self.img_label, 0, 1)

        self.show()

    def update(self):
        """ Updates the ui elements """
        _, self.frame = self.cap.read()
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width

        # create QImage from image
        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.img_label.setPixmap(QPixmap.fromImage(q_frame))

    def save_img(self):
        """ Saves the image from camera"""
        print("save image")
        # save image
        cv2.imwrite("image.jpg", self.frame)

    def record(self):
        """ Records the video """
        pass


# run
cam_icon_path = './assets/capture.jpg'


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
