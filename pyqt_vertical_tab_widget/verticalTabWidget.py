from PyQt5.QtCore import QRect, QPoint, Qt
from PyQt5.QtWidgets import QTabWidget, QTabBar, QStylePainter, QStyleOptionTab, QStyle, QProxyStyle, qApp, \
    QApplication, QWidget


class TabBar(QTabBar):
    # Transpose the size (if v size is bigger than h size, change each other)
    def tabSizeHint(self, index):
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        s.scale(s.width() * 2, s.height() * 2, Qt.KeepAspectRatio)
        return s

    # Make text visible adequately
    def paintEvent(self, event):
        painter = QStylePainter(self)
        style_option = QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(style_option, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, style_option)
            painter.save()

            size = style_option.rect.size()
            size.transpose()
            rect = QRect(QPoint(), size)
            rect.moveCenter(style_option.rect.center())
            style_option.rect = rect

            center = self.tabRect(i).center()
            painter.translate(center)
            painter.rotate(90)
            painter.translate(center*-1)
            painter.drawControl(QStyle.CE_TabBarTabLabel, style_option)
            painter.restore()

class VerticalTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setTabBar(TabBar(self))
        self.setTabPosition(QTabWidget.West)