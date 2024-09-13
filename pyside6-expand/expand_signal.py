from PySide6.QtCore import Signal, QTimer, Qt
from PySide6.QtGui import QMouseEvent


def mouse_signal(widget_cls):
    """
    set_mouse_signal

    Signal:
        left_double_clicked
        right_double_clicked
        left_clicked
        right_clicked
        left_long_press
        right_long_press
    """

    widget_cls.left_double_clicked = Signal()
    widget_cls.right_double_clicked = Signal()
    widget_cls.left_clicked = Signal()
    widget_cls.right_clicked = Signal()
    widget_cls.left_long_press = Signal()
    widget_cls.right_long_press = Signal()

    widget_cls.long_press_threshold = 500
    widget_cls.long_press_start = False
    widget_cls.long_press_timer = QTimer()
    widget_cls.isDouble = False

    # 长按函数
    def __timeout_then_is_long_press(self, btn):
        if self.long_press_start:
            if btn == Qt.MouseButton.LeftButton:
                self.left_long_press.emit()
            elif btn == Qt.MouseButton.RightButton:
                self.right_long_press.emit()
            self.long_press_start = False

    def mousePressEvent(self, e: QMouseEvent):
        self.oldMousePressEvent(e)
        btn = e.button()
        if btn != Qt.MouseButton.LeftButton and btn != Qt.MouseButton.RightButton:
            return
        self.long_press_start = True
        self.long_press_timer.timeout.connect(
            lambda: __timeout_then_is_long_press(self, btn)
        )
        self.long_press_timer.start(widget_cls.long_press_threshold)

    def mouseReleaseEvent(self, e: QMouseEvent):
        self.long_press_timer.stop()
        self.long_press_timer = QTimer()
        if self.long_press_start:
            self.long_press_start = False
        else:
            return
        if e.button() == Qt.MouseButton.LeftButton:
            def is_clicked():
                if not self.isDouble:
                    self.left_clicked.emit()
                self.isDouble = False

            QTimer.singleShot(100, lambda: is_clicked())
            self.oldMouseReleaseEvent(e)
        elif e.button() == Qt.MouseButton.RightButton:
            def is_clicked():
                if not self.isDouble:
                    self.right_clicked.emit()
                self.isDouble = False

            QTimer.singleShot(100, lambda: is_clicked())
            self.oldMouseReleaseEvent(e)

    def mouseDoubleClickEvent(self, e: QMouseEvent):
        self.isDouble = True
        btn = e.button()
        if btn == Qt.MouseButton.LeftButton:
            self.left_double_clicked.emit()
        elif btn == Qt.MouseButton.RightButton:
            self.right_double_clicked.emit()

    widget_cls.__timeout_then_is_long_press = __timeout_then_is_long_press
    widget_cls.oldMousePressEvent = widget_cls.mousePressEvent
    widget_cls.oldMouseReleaseEvent = widget_cls.mouseReleaseEvent
    widget_cls.oldMouseDoubleClickEvent = widget_cls.mouseDoubleClickEvent
    setattr(widget_cls, 'mousePressEvent', mousePressEvent)
    setattr(widget_cls, 'mouseReleaseEvent', mouseReleaseEvent)
    setattr(widget_cls, 'mouseDoubleClickEvent', mouseDoubleClickEvent)
    return widget_cls