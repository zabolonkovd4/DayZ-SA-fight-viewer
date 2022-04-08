import sys
from MapQGraphicsView import MapQGraphicsView
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap
MAP_FILEPATH = 'map2/created/map.png'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gv = MapQGraphicsView()
    gv.resize(1440, 990)

    scene = QGraphicsScene()
    pixmap = QPixmap(MAP_FILEPATH)
    scene.addPixmap(pixmap)

    gv.setScene(scene)
    gv.show()
    app.exec()


