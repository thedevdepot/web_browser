from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


def __init__(self, *args. **kwargs):
    super(MyWebBrowser, self).__init__(*args, **kwargs)

self.window = QWidget()
self.window.setWindowTitle("Python Web Browser")

self.layout = QVBoxLayout()
self.horizontal = QHBoxLayout()

self.url_bar = QTextEdit()
self.go_btn = setMinimumHeight(38)

self.go_btn = setMinimumHeight(38)

self.go_btn = QPushButton("<")
self.go_btn = setMinimumHeight(38)

self.go_btn = QPushButton(">")
self.go_btn = setMinimumHeight(38)

self.horizontal.addWidget(self.url_bar)
self.horizontal.addWidget(self.go_btn)
self.horizontal.addWidget(self.back_btn)
self.horizontal.addWidget(self.forward_btn)

self.browser = QWebEngineView()