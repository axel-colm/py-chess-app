from ...qt_core import *


class MenuButton(QtWidgets.QWidget):
    clicked = QtCore.Signal(object)
    released = QtCore.Signal(object)

    _switchable = False
    _checked = False
    _mouse_pressed = False
    _mouse_on = False

    _bg_color = "#282a36"
    _bg_color_pressed = "#282a36"
    _bg_color_on = "#282a36"
    _bg_color_active = "#282a36"

    _color = "#eeeeee"
    _color_pressed = "#eeeeee"
    _color_on = "#ffffff"
    _color_active = "#ffffff"


    def __init__(self, icon_path: str, text: str):
        super().__init__()
        self._icon_path = icon_path
        self._text = text

    def setSwitchable(self, switchable: bool):
        self._switchable = switchable

    def mousePressEvent(self, event):
        self._mouse_pressed = True
        self.update()

        self.clicked.emit(self)

    def mouseReleaseEvent(self, event):
        self._mouse_pressed = False
        if self._switchable:
            self._checked = not self._checked
        self.update()

        self.released.emit(self)

    def enterEvent(self, event):
        self._mouse_on = True
        self.update()

    def leaveEvent(self, event):
        self._mouse_on = False
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform)

        # Draw background
        if self._mouse_pressed:
            bg_color = self._bg_color_pressed
            color = self._color_pressed
        elif self._mouse_on:
            bg_color = self._bg_color_on
            color = self._color_on
        elif self._checked:
            bg_color = self._bg_color_active
            color = self._color_active
        else:
            bg_color = self._bg_color
            color = self._color

        painter.setPen(QtCore.Qt.PenStyle.NoPen)
        painter.setBrush(QtGui.QColor(bg_color))
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 10, 10)

        # Draw icon
        icon = QtGui.QIcon(self._icon_path)
        margin = 8
        icon_size = self.height() - 2 * margin

        icon_color = QtGui.QColor(color)
        icon_color.setAlpha(255)
        pixmap = icon.pixmap(icon_size, icon_size)

        p = QtGui.QPainter(pixmap)
        p.setCompositionMode(QtGui.QPainter.CompositionMode.CompositionMode_SourceIn)
        p.fillRect(pixmap.rect(), icon_color)
        p.end()

        painter.drawPixmap(margin, margin, pixmap)



