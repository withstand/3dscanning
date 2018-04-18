from OpenGL.GL import *
from OpenGL.GLU import *
from pyqtgraph.Qt import QtGui
from PyQt5.QtOpenGL import *
from show_cloud import *



class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.widget, self.view3d = make_3d_widget(get_data_hdf5('1'))
        self.widget.setMinimumSize(640, 480)
        self.list = QtGui.QListWidget()
        
        for item in get_test_data_list():
            self.list.addItem(item)

        self.list.currentItemChanged.connect(self.on_select_change)

        mainLayout = QtGui.QHBoxLayout() 

        mainLayout.addWidget(self.list)
        mainLayout.addWidget(self.widget)

        self.setLayout(mainLayout)

    def on_select_change(self, curr, prev):
        self.setWindowTitle(curr.text())
        update_3d_scatter(self.view3d, get_data_hdf5(curr.text()))
        self.widget.show()


if __name__ == '__main__':
    app = QtGui.QApplication(['Yo'])
    window = MainWindow()
    window.show()
    app.exec_()
