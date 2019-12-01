from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QFileDialog
import sys
from analytical_pdf import parse
import youdao

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):

        #QtWidgets.QAction()必须传入self参数,不然就不能显示,肝了很久才知道
        openaction=QtWidgets.QAction(QtGui.QIcon("file.ico"),"&open",self)
        openaction.setShortcut("ctrl+o")
        openaction.setStatusTip("open a file")
        openaction.triggered.connect(self.openFile)

        self.statusBar()

        menu=self.menuBar()
        file=menu.addMenu("&File")
        file.addAction(openaction)

        # 设置标题,图标,大小及窗口起始位置
        self.setWindowTitle("translation")
        self.setGeometry(500, 500, 500, 400)
        self.setWindowIcon(QtGui.QIcon("bear.ico"))

        #设置文本输出框
        self.textEdit=QtWidgets.QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.show()






    def openFile(self):    #用来打开pdf文件

        #函数返回两个值,第一个为文件路径,第二个为文件类型
        fileName,fileType=QFileDialog.getOpenFileName(self,"选择文件","./","*.pdf")
        parse(fileName,"./1.txt")
        a=youdao.youdao()
        with open("./1.txt","r",encoding="utf-8") as f:

            temp_str=f.readline()
            #执行翻译功能
            temp_str=a.fun(temp_str)
            all_str=temp_str
            while(temp_str):
                temp_str=f.readline()
                if len(temp_str):
                    temp_str=a.fun(temp_str)
                all_str+='\n'+temp_str
                # temp_str=None
            self.textEdit.setText(all_str)

app = QtWidgets.QApplication(sys.argv)
a=mywindow()
sys.exit(app.exec_())