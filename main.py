from PyQt5 import QtWidgets, QtCore, QtGui
from collections import deque
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QColor, QPixmap, QIcon, QPalette, QBrush, QImage, QPen
from PyQt5.QtWidgets import QGridLayout, QWidget, QPushButton, QColorDialog, QHBoxLayout, QFileDialog, QVBoxLayout, \
    QLabel
import traceback


class StartWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.window2 = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pixel Art')
        self.setWindowIcon(QIcon('resources/logo.png'))
        # self.setStyleSheet("""background-color: yellow;""")
        self.pix = QtGui.QPixmap('resources/title.png')
        self.label = QLabel(self)
        self.label.setPixmap(self.pix)
        self.label.resize(300, 75)
        self.label.move(168, 100)
        self.button = QtWidgets.QPushButton('НАЧАТЬ', self)
        self.button.move(240, 260)
        self.button.setStyleSheet('background-color: #003366;'
                                  'color: #FFFFFF;'
                                  'border-style: outset;'
                                  'border-radius: 10px;'
                                  'border-color: #003366;'
                                  'padding: 10px;'
                                  'min-width: 6em;'
                                  'min-height: 2em;'
                                  'font-size: 18px;')
        self.button.clicked.connect(self.openWindow)

        self.setGeometry(100, 100, 600, 600)
        self.setFixedSize(640, 600)

        self.Exit = QtWidgets.QPushButton("Выход", self)
        # self.Exit.setStyleSheet('background-color: #000;')
        self.Exit.setStyleSheet('background-color: #003366;'
                                'color: #FFFFFF;'
                                'border-style: outset;'
                                'border-radius: 10px;'
                                'border-color: #003366;'
                                'padding: 10px;'
                                'min-width: 6em;'
                                'min-height: 2em;'
                                'font-size: 18px;')
        self.Exit.move(240, 350)
        self.Exit.clicked.connect(self.exit_app)

    def exit_app(self):
        app.exit()

    def openWindow(self):
        self.hide()
        self.window2 = Menu(self)
        self.window2.setGeometry(self.geometry())
        self.window2.show()


class Menu(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parentWindow = parent
        self.window3 = None
        self.initUI()
        self.setWindowTitle('Pixel Art')

    def initUI(self):
        self.buttonBack = QPushButton('Назад', self)
        self.buttonBack.setStyleSheet('background-color: #003366;'
                                      'color: #FFFFFF;'
                                      'border-style: outset;'
                                      'border-radius: 10px;'
                                      'border-color: #003366;'
                                      'padding: 10px;'
                                      'min-width: 6em;'
                                      'min-height: 2em;'
                                      'font-size: 18px;')
        self.buttonBack.move(12, 10)
        self.buttonBack.clicked.connect(self.back)
        grid = QGridLayout()
        # self.setStyleSheet("background-color: yellow;")
        self.button1 = QPushButton('16x16 px', self)
        self.button1.clicked.connect(self.openPixelArt16)
        self.button1.setIcon(QtGui.QIcon('images/1a.jpg'))
        self.button1.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button1, 0, 0)

        self.button2 = QPushButton('16x16 px', self)
        self.button2.clicked.connect(self.openPixelArt16)
        self.button2.setIcon(QIcon('images/2a.jpg'))
        self.button2.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button2, 0, 1)

        self.button3 = QPushButton('16x16 px', self)
        self.button3.clicked.connect(self.openPixelArt16)
        self.button3.setIcon(QIcon('images/3a.jpg'))
        self.button3.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button3, 0, 2)

        self.button4 = QPushButton('32x32 px', self)
        self.button4.clicked.connect(self.openPixelArt32)
        self.button4.setIcon(QIcon('images/4a.jpg'))
        self.button4.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button4, 1, 0)

        self.button5 = QPushButton('32x32 px', self)
        self.button5.clicked.connect(self.openPixelArt32)
        self.button5.setIcon(QIcon('images/5a.jpg'))
        self.button5.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button5, 1, 1)

        self.button6 = QPushButton('32x32 px', self)
        self.button6.clicked.connect(self.openPixelArt32)
        self.button6.setIcon(QIcon('images/6a.jpg'))
        self.button6.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button6, 1, 2)
        self.setLayout(grid)

        self.button7 = QPushButton('32x32 px', self)
        self.button7.clicked.connect(self.openPixelArt32)
        self.button7.setIcon(QIcon('images/no.jpg'))
        self.button7.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button7, 1, 3)
        self.setLayout(grid)

        self.button8 = QPushButton('16x16 px', self)
        self.button8.clicked.connect(self.openPixelArt16)
        self.button8.setIcon(QIcon('images/no.jpg'))
        self.button8.setIconSize(QtCore.QSize(128, 128))
        grid.addWidget(self.button8, 0, 3)
        self.setLayout(grid)

        self.setFixedSize(900, 600)

    def openPixelArt16(self):
        self.hide()
        self.window3 = PixelArt16(self)
        self.window3.setGeometry(self.geometry())
        self.window3.show()

    def openPixelArt32(self):
        self.hide()
        self.window4 = PixelArt32(self)
        self.window4.setGeometry(self.geometry())
        self.window4.show()

    def back(self):
        self.hide()
        sw.show()

    # Это не нужно
    # def show_image_in_image_window(self, image):
    #     pass
    #     # image = self.button1.icon().pixmap(self.button1.iconSize()).toImage()
    #     # ImageWindow.show_image(self, image)


class Pixel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QColor(255, 255, 255)

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.rect()
        painter.fillRect(rect, self.color)

    def setColor(self, color):
        self.color = color
        self.update()


class PixelArt16(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parentWindow = parent
        self.drawing = False
        self.pixels = []
        self.setWindowTitle('Pixel Art')
        self.color = QColor(0, 0, 0)
        self.pixels = []
        for i in range(16):
            row = []
            for j in range(16):
                pixel = Pixel(self)
                pixel.setMinimumSize(20, 20)
                row.append(pixel)
            self.pixels.append(row)

        self.filling = False

        gridLayout = QGridLayout(self)
        for i in range(16):
            for j in range(16):
                gridLayout.addWidget(self.pixels[i][j], i, j)

        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.image.fill(Qt.white)

        self.colorButton = QPushButton('Палитра', self)
        self.colorButton.setIcon(QIcon('resources/paint.png'))
        self.colorButton.clicked.connect(self.showColorDialog)
        self.colorButton.resize(110, 40)
        self.colorButton.move(0, 0)

        self.eraserButton = QPushButton('Ластик', self)
        self.eraserButton.setIcon((QIcon('resources/eraser.png')))
        self.eraserButton.clicked.connect(self.eraser)
        self.eraserButton.resize(110, 40)
        self.eraserButton.move(110, 0)

        self.fillButton = QPushButton('Заливка', self)
        self.fillButton.setIcon(QIcon('resources/bucket.png'))
        self.fillButton.clicked.connect(self.fill)
        self.fillButton.resize(110, 40)
        self.fillButton.move(220, 0)

        self.ImageButton = QPushButton('Картинка', self)
        self.ImageButton.setIcon(QIcon('resources/card.png'))
        self.ImageButton.clicked.connect(self.ShowImage)
        self.ImageButton.resize(110, 40)
        self.ImageButton.move(330, 0)

        self.BackButton = QPushButton('Назад', self)
        self.BackButton.setIcon(QIcon('resources/back.png'))
        self.BackButton.clicked.connect(self.BackToMenu)
        self.BackButton.resize(110, 40)
        self.BackButton.move(440, 0)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.colorButton)
        hbox.addWidget(self.eraserButton)
        hbox.addWidget(self.fillButton)
        hbox.addWidget(self.BackButton)

        saveButton = QPushButton('Сохранить', self)
        saveButton.setIcon(QIcon('resources/save.png'))
        saveButton.resize(110, 40)
        saveButton.move(550, 0)
        saveButton.clicked.connect(self.save)
        hbox.addWidget(saveButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(gridLayout)
        self.setLayout(vbox)

    def showColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color

    def ShowImage(self):
        self.window4 = ImageWindow()
        self.window4.show()

    def BackToMenu(self):
        self.hide()
        self.window2 = Menu(self)
        self.window2.setGeometry(self.geometry())
        self.window2.show()

    def eraser(self):
        self.color = QColor(255, 255, 255)

    def fill_clicked(self):
        if not self.filling:
            self.filling = True
        else:
            self.filling = False

    # Не работает
    def fill(self, event):
        # for row in self.pixels:
        #     for pixel in row:
        #         if pixel.color == QColor(255, 255, 255):
        #             pixel.setColor(self.color)
        #
        xPos, yPos = event.pos().x(), event.pos().y()
        mat = self.pixels
        x, y = None, None
        replacement = self.color
        for i in range(32):
            for j in range(32):
                pixel = self.pixels[i][j]
                print(pixel)
        #         if pixel.geometry().contains(QPoint(xPos, yPos)):
        #             x, y = i, j
        # if x and y:
        #
        #     # Ниже перечислены все восемь возможных перемещений.
        #     row = [-1, -1, -1, 0, 0, 1, 1, 1]
        #     col = [-1, 0, 1, -1, 1, -1, 0, 1]
        #
        #     # проверяет, можно ли перейти к пикселю (x, y) из
        #     # текущий пиксель. Функция возвращает false, если пиксель
        #     # имеет другой цвет или недействительный пиксель
        #     def isSafe(mat, x, y, target):
        #         return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target
        #
        #     # Заливка с помощью DFS
        #     def floodfill(mat, x, y, replacement):
        #
        #         # Базовый вариант
        #         if not mat or not len(mat):
        #             return
        #
        #         # получить целевой цвет
        #         target = mat[x][y]
        #
        #         # Целевой цвет # такой же, как и при замене
        #         if target == replacement:
        #             return
        #
        #         # заменить текущий цвет пикселя цветом замены
        #         mat[x][y] = replacement
        #
        #         # обрабатывает все восемь соседних пикселей текущего пикселя и
        #         # повторяется для каждого допустимого пикселя
        #         for k in range(len(row)):
        #
        #             # , если соседний пиксель в позиции (x + row[k], y + col[k])
        #             # допустимый пиксель и имеет тот же цвет, что и текущий пиксель
        #             if isSafe(mat, x + row[k], y + col[k], target):
        #                 floodfill(mat, x + row[k], y + col[k], replacement)
        #
        #     floodfill(mat, x, y, replacement)

    def draw(self, event):
        painter = QPainter(self.image)
        xPos = event.pos().x()
        yPos = event.pos().y()
        for i in range(16):
            for j in range(16):
                pixel = self.pixels[i][j]
                if pixel.geometry().contains(QPoint(xPos, yPos)):
                    pixel.setColor(self.color)
                    painter.setPen(QPen(QtGui.QColor(pixel.color), 3, Qt.SolidLine))
                    painter.drawRect(j * 30 - 3, i * 30 - 3, 30 - 4, 30 - 4)
                    painter.fillRect(j * 30 - 3, i * 30 - 3, 30 - 4, 30 - 4, QtGui.QColor(pixel.color))
                    self.update()

    def load_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Load Image', '', 'Images (*.png *.jpg);;All Files (*)')
        if filename:
            self.image_path = filename
            pixmap = QPixmap(filename)
            self.label.setPixmap(pixmap)

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "":
            return
        self.image.save(filePath)

    def mousePressEvent(self, event):
        self.drawing = True
        self.draw(event)

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.draw(event)

    def mouseReleaseEvent(self, event):
        self.drawing = False

    def closeWindow(self):
        self.hide()
        self.parentWindow.show()


class PixelArt32(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parentWindow = parent
        self.drawing = False
        self.pixels = []
        self.setWindowTitle('Pixel Art')
        self.color = QColor(0, 0, 0)

        self.filling = False

        self.image = QImage(self.size(), QImage.Format_RGB32)

        # setting canvas color to white
        self.image.fill(Qt.white)

        for i in range(32):
            row = []
            for j in range(32):
                pixel = Pixel(self)
                pixel.setMinimumSize(20, 20)
                row.append(pixel)
            self.pixels.append(row)

        gridLayout = QGridLayout(self)
        for i in range(32):
            for j in range(32):
                gridLayout.addWidget(self.pixels[i][j], i, j)

        self.colorButton = QPushButton('Палитра', self)
        self.colorButton.setIcon(QIcon('resources/paint.png'))
        self.colorButton.clicked.connect(self.showColorDialog)
        self.colorButton.resize(110, 40)
        self.colorButton.move(0, 0)

        self.eraserButton = QPushButton('Ластик', self)
        self.eraserButton.setIcon((QIcon('resources/eraser.png')))
        self.eraserButton.clicked.connect(self.eraser)
        self.eraserButton.resize(110, 40)
        self.eraserButton.move(110, 0)

        self.fillButton = QPushButton('Заливка', self)
        self.fillButton.setIcon(QIcon('resources/bucket.png'))
        self.fillButton.clicked.connect(self.fill_clicked)
        self.fillButton.resize(110, 40)
        self.fillButton.move(220, 0)

        self.ImageButton = QPushButton('Картинка', self)
        self.ImageButton.setIcon(QIcon('resources/card.png'))
        self.ImageButton.clicked.connect(self.ShowImage)
        self.ImageButton.resize(110, 40)
        self.ImageButton.move(330, 0)

        self.BackButton = QPushButton('Назад', self)
        self.BackButton.setIcon(QIcon('resources/back.png'))
        self.BackButton.clicked.connect(self.BackToMenu)
        self.BackButton.resize(110, 40)
        self.BackButton.move(440, 0)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.colorButton)
        hbox.addWidget(self.eraserButton)
        hbox.addWidget(self.fillButton)
        hbox.addWidget(self.BackButton)

        saveButton = QPushButton('Сохранить', self)
        saveButton.setIcon(QIcon('resources/save.png'))
        saveButton.resize(110, 40)
        saveButton.move(550, 0)
        saveButton.clicked.connect(self.save)
        hbox.addWidget(saveButton)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(gridLayout)
        self.setLayout(vbox)

    def showColorDialog(self):
        self.filling = False
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color

    def ShowImage(self):
        self.window4 = ImageWindow()
        self.window4.show()

    def BackToMenu(self):
        self.hide()
        self.window2 = Menu(self)
        self.window2.setGeometry(self.geometry())
        self.window2.show()

    def eraser(self):
        self.filling = False
        self.color = QColor(255, 255, 255)

    def fill_clicked(self):
        if not self.filling:
            self.filling = True
        else:
            self.filling = False
    # Не работает
    def fill(self, event):
        # for row in self.pixels:
        #     for pixel in row:
        #         if pixel.color == QColor(255, 255, 255):
        #             pixel.setColor(self.color)
        #
        xPos, yPos = event.pos().x(), event.pos().y()
        mat = self.pixels
        x, y = None, None
        replacement = self.color
        for i in range(32):
            for j in range(32):
                pixel = self.pixels[i][j]
                print(pixel)
        #         if pixel.geometry().contains(QPoint(xPos, yPos)):
        #             x, y = i, j
        # if x and y:
        #
        #     # Ниже перечислены все восемь возможных перемещений.
        #     row = [-1, -1, -1, 0, 0, 1, 1, 1]
        #     col = [-1, 0, 1, -1, 1, -1, 0, 1]
        #
        #     # проверяет, можно ли перейти к пикселю (x, y) из
        #     # текущий пиксель. Функция возвращает false, если пиксель
        #     # имеет другой цвет или недействительный пиксель
        #     def isSafe(mat, x, y, target):
        #         return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and mat[x][y] == target
        #
        #     # Заливка с помощью DFS
        #     def floodfill(mat, x, y, replacement):
        #
        #         # Базовый вариант
        #         if not mat or not len(mat):
        #             return
        #
        #         # получить целевой цвет
        #         target = mat[x][y]
        #
        #         # Целевой цвет # такой же, как и при замене
        #         if target == replacement:
        #             return
        #
        #         # заменить текущий цвет пикселя цветом замены
        #         mat[x][y] = replacement
        #
        #         # обрабатывает все восемь соседних пикселей текущего пикселя и
        #         # повторяется для каждого допустимого пикселя
        #         for k in range(len(row)):
        #
        #             # , если соседний пиксель в позиции (x + row[k], y + col[k])
        #             # допустимый пиксель и имеет тот же цвет, что и текущий пиксель
        #             if isSafe(mat, x + row[k], y + col[k], target):
        #                 floodfill(mat, x + row[k], y + col[k], replacement)
        #
        #     floodfill(mat, x, y, replacement)

    def draw(self, event):
        painter = QPainter(self.image)
        xPos = event.pos().x()
        yPos = event.pos().y()
        for i in range(32):
            for j in range(32):
                pixel = self.pixels[i][j]
                if pixel.geometry().contains(QPoint(xPos, yPos)):
                    pixel.setColor(self.color)
                    painter.setPen(QPen(QtGui.QColor(pixel.color), 3, Qt.SolidLine))
                    painter.drawRect(j * 15 - 3, i * 15 - 3, 15 - 4, 15 - 4)
                    painter.fillRect(j * 15 - 3, i * 15 - 3, 15 - 4, 15 - 4, QtGui.QColor(pixel.color))
                    self.update()

    def load_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Load Image', '', 'Images (*.png *.jpg);;All Files (*)')
        if filename:
            self.image_path = filename
            pixmap = QPixmap(filename)
            self.label.setPixmap(pixmap)

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "":
            return
        self.image.save(filePath)

    def mousePressEvent(self, event):
        if not self.filling:
            self.drawing = True
            self.draw(event)
        else:
            self.fill(event)

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.draw(event)

    def mouseReleaseEvent(self, event):
        self.drawing = False

    def closeWindow(self):
        self.hide()
        self.parentWindow.show()


class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)

    def show_image(self, image):
        pixmap = QtGui.QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)
        self.label.adjustSize()

    def BackToMenu(self):
        self.hide()
        self.window3 = PixelArt16(self)
        self.window3.setGeometry(self.geometry())
        self.window3.show()

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.BackButton)


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    QtWidgets.QApplication.quit()


if __name__ == '__main__':
    import sys

    sys.excepthook = excepthook
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('resources/logo.png'))
    sw = StartWindow()
    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("resources/texture.jpg")))
    pixelArt16 = PixelArt16(sw)
    pixelArt32 = PixelArt32(sw)
    sw.setPalette(palette)
    app.setPalette(palette)
    sw.show()
    sys.exit(app.exec_())

# кнопка сохранения
