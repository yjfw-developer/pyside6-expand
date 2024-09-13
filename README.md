# PySide6-Expand

## 0.安装 
```
#安装
pip install pyside6-expand

#使用
from pyside6_expand.expand_signal import mouse_signal
```

## 1.拓展 - - 鼠标信号：
将`@mouse_signal`修饰在继承`QWidget`的类上，运行时程序会动态将信号覆盖到QWidget上。<br>
支持的信号有:<br>
1. left_clicked 左键点击
2. left_double_clicked 左键双击
3. left_long_press 左键长按
4. right_clicked 右键点击
5. right_double_clicked 右键双击
6. right_long_press 右键长按<br>

各个信号之间执行不冲突。

注意：<br>
该修饰器重写了`mouseDoubleClickEvent`,`mousePressEvent`,`mouseReleaseEvent`<br>
先执行`mousePressEvent`后执行信号 <br>
先执行`mouseReleaseEvent`后执行信号逻辑<br>
不能再次重写`mouseDoubleClickEvent` 否则`left_double_clicked`和`right_double_clicked`信号将失效
###使用例子：
```python
from pyside6_expand.expand_signal import mouse_signal
from PySide6.QtWidgets import QWidget,QApplication
@mouse_signal
class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()
if __name__ == '__main__':
    app = QApplication()
    widget = CustomWidget()
    widget.left_clicked.connect(lambda: print("左键点击"))
    widget.left_double_clicked.connect(lambda: print("左键双击"))
    widget.left_long_press.connect(lambda :print("左键长按"))
    widget.right_clicked.connect(lambda: print("右键点击"))
    widget.right_double_clicked.connect(lambda: print("右键双击"))
    widget.right_long_press.connect(lambda :print("右键长按"))
    widget.show()
    app.exec()
```

## 其他功能正在快速拓展中 ~ ~：