<!-- BEGIN NAVIGATION -->
<div align="center">
  <a href="README.md">English</a> |
  <a href="README_CN.md">中文</a>
</div>
<!-- END NAVIGATION -->

### English

# PySide6-Expand Usage Guide

## 0. Installation

Install PySide6-Expand using pip:

```shell
pip install pyside6-expand
```

Then import the required module in your code:

```python
from pyside6_expand.expand_signal import mouse_signal
```

## 1. Extension - Mouse Signals

Apply the `@mouse_signal` decorator to classes that inherit from `QWidget` to dynamically bind mouse event signals at runtime.

### Supported Signals

- `left_clicked`: Left button click
- `left_double_clicked`: Left button double click
- `left_long_press`: Left button long press
- `right_clicked`: Right button click
- `right_double_clicked`: Right button double click
- `right_long_press`: Right button long press

### Signals Arg:

- `arg for the instance of widget`
- such as `widget.left_clicked.connect(lambda w:print(w))` 
- `w:<__main__.CustomWidget(0x1f691a60910) at 0x000001F6936C6280>`

These signals operate independently and do not interfere with each other.

### Notes

- The `@mouse_signal` decorator overrides the methods `mouseDoubleClickEvent`, `mousePressEvent`, and `mouseReleaseEvent`.
- When handling mouse press events, `mousePressEvent` is called first, followed by the corresponding signal.
- When handling mouse release events, `mouseReleaseEvent` is called first, followed by the logic of the respective signal.
- Do not override `mouseDoubleClickEvent` again, otherwise the `left_double_clicked` and `right_double_clicked` signals will fail to work.

### Example Code

```python
from pyside6_expand.expand_signal import mouse_signal
from PySide6.QtWidgets import QWidget, QApplication

@mouse_signal(long_press_threshold=500) # or @mouse_signal()
class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication([])
    widget = CustomWidget()
    
    # Connect signals to slots
    widget.left_clicked.connect(lambda item: print("Left button clicked"))
    widget.left_double_clicked.connect(lambda item: print("Left button double clicked"))
    widget.left_long_press.connect(lambda item: print("Left button long pressed"))
    widget.right_clicked.connect(lambda item: print("Right button clicked"))
    widget.right_double_clicked.connect(lambda item: print("Right button double clicked"))
    widget.right_long_press.connect(lambda item: print("Right button long pressed"))

    widget.show()
    app.exec()
```

## Additional Features

This project is actively developing new features, so stay tuned for updates.