from ...core.functions import Function
from ...qt_core import *
from .menu_button import MenuButton


class MenuWidget(QtWidgets.QWidget):
    _COLLAPSED_WIDTH = 50
    _EXPANDED_WIDTH = 200
    _BUTTON_SIZE = 46
    _BORDER_RADIUS = 10
    _bg_color = "#282a36"

    def __init__(self):
        super().__init__()
        self.setMinimumWidth(self._COLLAPSED_WIDTH)
        self._layout = QtWidgets.QVBoxLayout()
        self._layout.setContentsMargins(2, 2, 2, 2)
        self.setLayout(self._layout)

        self._menu_button = MenuButton(Function.icon_path("menu-burger.svg"), "Menu")
        self._menu_button.setFixedHeight(self._BUTTON_SIZE)
        self._menu_button.setSwitchable(True)
        self._menu_button.released.connect(self.toggleMenu)
        self._layout.addWidget(self._menu_button)

        self._top_menu = QtWidgets.QWidget()
        self._top_menu.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)

        self._middle_menu = QtWidgets.QWidget()
        self._middle_menu.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self._bottom_menu = QtWidgets.QWidget()
        self._bottom_menu.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)

        self._layout.addWidget(self._top_menu)
        self._layout.addWidget(self._middle_menu)
        self._layout.addWidget(self._bottom_menu)

    def toggleMenu(self):
        pass

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)

        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.setBrush(QtGui.QBrush(QtGui.QColor(self._bg_color)))
        painter.drawRoundedRect(0, 0, self.width(), self.height(), self._BORDER_RADIUS, self._BORDER_RADIUS)