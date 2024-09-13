<!-- BEGIN NAVIGATION -->
<div align="center">
  <a href="README.md">English</a> |
  <a href="README_CN.md">中文</a>
</div>
<!-- END NAVIGATION -->


### 中文版

# PySide6-Expand 使用指南

## 0. 安装

通过 pip 安装 PySide6-Expand:

```shell
pip install pyside6-expand
```

然后可以在代码中导入所需的模块：

```python
from pyside6_expand.expand_signal import mouse_signal
```

## 1. 拓展 - 鼠标信号

将 `@mouse_signal` 装饰器应用于继承自 `QWidget` 的类，这样在运行时，程序会动态地将鼠标事件信号绑定到 `QWidget` 上。

### 支持的信号

- `left_clicked`: 左键点击
- `left_double_clicked`: 左键双击
- `left_long_press`: 左键长按
- `right_clicked`: 右键点击
- `right_double_clicked`: 右键双击
- `right_long_press`: 右键长按

这些信号彼此独立工作，互不干扰。

### 注意事项

- `@mouse_signal` 装饰器会重写 `mouseDoubleClickEvent`, `mousePressEvent`, 和 `mouseReleaseEvent` 方法。
- 在处理鼠标按下事件时，首先会调用 `mousePressEvent`，然后触发相应的信号。
- 在处理鼠标释放事件时，首先会调用 `mouseReleaseEvent`，然后触发相应的信号逻辑。
- 不要再次重写 `mouseDoubleClickEvent` 方法，否则 `left_double_clicked` 和 `right_double_clicked` 信号将会失效。

### 示例代码

```python
from pyside6_expand.expand_signal import mouse_signal
from PySide6.QtWidgets import QWidget, QApplication

@mouse_signal
class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication([])
    widget = CustomWidget()
    
    # 连接信号与槽函数
    widget.left_clicked.connect(lambda: print("左键点击"))
    widget.left_double_clicked.connect(lambda: print("左键双击"))
    widget.left_long_press.connect(lambda: print("左键长按"))
    widget.right_clicked.connect(lambda: print("右键点击"))
    widget.right_double_clicked.connect(lambda: print("右键双击"))
    widget.right_long_press.connect(lambda: print("右键长按"))

    widget.show()
    app.exec()
```

## 其他功能

本项目正在积极开发新的功能，请持续关注更新。