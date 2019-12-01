import sys
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog,qApp
# from PyQt5.Qt import *

class Mywindow(QtWidgets.QWidget):
    def __init__(self):
        super(Mywindow,self).__init__()
        # self.myButton=QtWidgets.QPushButton(self)
        # self.myButton.setObjectName("myButton")
        # self.myButton.setText("open")
        # self.myButton.setGeometry(100,100,100,30)
        # self.myButton.clicked.connect(self.msg)
    def msg(self):
        # QFileDialog.getExistingDirectory()self参数同样不能省略
        # directory=QFileDialog.getExistingDirectory(self,"选择文件夹","./")
        # print(directory)
        directory1=QFileDialog.getExistingDirectory(self,"选择文件夹","./")
        # print(directory1)
        fileName1,filetype=QFileDialog.getOpenFileName(self,"选取文件",directory1,
                                                      "All Files(*);;Text Files(*.txt)")
        print(fileName1)
# def msg():
#     # directory1=QFileDialog.getExistingDirectory("选择文件夹","./")
#     # # print(directory1)
#     # fileName1,filetype=QFileDialog.getOpenFileName("选取文件",directory1,
#     #                                               "All Files(*);;Text Files(*.txt)")
#     # print(fileName1)
#     print("open file")


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    # w=QWidget()
    w=QtWidgets.QMainWindow()
    # w=QtWidgets.QWidget()
    w.setWindowTitle("translation")
    # 在主窗口下加入菜单栏
    menu=w.menuBar()

    # print(type(menu))
    #定义一个暂时用的类
    mwid=Mywindow()


    #定义一个下拉菜单的action
    open1=QtWidgets.QAction(QtGui.QIcon("file.ico"),"&open")
    open1.triggered.connect(mwid.msg)                       #传入函数指针,我试了半天


    #菜单栏添加菜单
    file=menu.addMenu("file")
    # menu.addMenu("nihao")

    #添加了下拉菜单的内容
    file.addAction(open1)


    # start x ,start y , w的宽度,h的高度
    w.setGeometry(500,300,500,500)
    button=QtWidgets.QPushButton(w)
    button.setText("file")
    button.setGeometry(200,250,100,30)

    # menu=QtWidgets.QMenu()   #菜单的类
    # menu.addAction("open")
    # menu.addSeparator()
    # button.setMenu(menu)    #按键的下拉
    w.show()

    # myshow=Mywindow()
    # myshow.show()
    sys.exit(app.exec_())
