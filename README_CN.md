### 中文

# PySide6-扩展使用指南

## 0. 安装

使用pip安装PySide6-Expand:

```shell
pip install pyside6-expand
```

然后在代码中导入所需的模块：

```python
from pyside6_expand.expand_signal import mouse_signal
```

## 1. 扩展 - 鼠标事件信号

将`@mouse_signal`装饰器应用到继承自`QWidget`的类上以在运行时动态绑定鼠标事件信号。

### 支持的信号

- `left_clicked`: 左键点击
- `left_double_clicked`: 左键双击
- `left_long_press`: 左键长按
- `right_clicked`: 右键点击
- `right_double_clicked`: 右键双击
- `right_long_press`: 右键长按

### 信号参数：

- `widget实例`
- 比如 `widget.left_clicked.connect(lambda w:print(w))`
- `w:<__main__.CustomWidget(0x1f691a60910) at 0x000001F6936C6280>`

这些信号独立运作，并且互不干扰。

### 注意事项

- `@mouse_signal`装饰器会覆盖`mouseDoubleClickEvent`，`mousePressEvent`以及`mouseReleaseEvent`方法。
- 在处理鼠标按下事件时，`mousePressEvent`首先被调用，接着是相应的信号。
- 在处理鼠标释放事件时，`mouseReleaseEvent`首先被调用，然后才是对应信号的逻辑。
- 不要再次覆盖`mouseDoubleClickEvent`，否则`left_double_clicked`和`right_double_clicked`信号将无法正常工作。

### 示例代码

```python
from pyside6_expand.expand_signal import mouse_signal
from PySide6.QtWidgets import QWidget, QApplication

@mouse_signal(long_press_threshold=500) # 或者 @mouse_signal()
class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication([])
    widget = CustomWidget()
    
    # 连接信号与槽函数
    widget.left_clicked.connect(lambda item: print("左键点击"))
    widget.left_double_clicked.connect(lambda item: print("左键双击"))
    widget.left_long_press.connect(lambda item: print("左键长按"))
    widget.right_clicked.connect(lambda item: print("右键点击"))
    widget.right_double_clicked.connect(lambda item: print("右键双击"))
    widget.right_long_press.connect(lambda item: print("右键长按"))

    widget.show()
    app.exec()
```

## 新功能

本项目正在积极开发新特性，请关注后续更新。