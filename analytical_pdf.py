import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

'''
 解析pdf 文本，保存到txt文件中
'''

def parse(path,dest):  #path->dest
    fp = open(path, 'rb') # 以二进制读模式打开
    #用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages(): # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
            with open(dest, 'w') as f:
                for x in layout:
                    if (isinstance(x, LTTextBoxHorizontal)):   #如果为字符就可以添加到文件中
                            results = x.get_text()
                            print(results)
                            f.write(results + '\n')
                f.close()

path="D:/360Downloads/text.pdf"
parse(path,"./2.txt")


# #先借助标准库函数来解析
# import sys,importlib
# importlib.reload(sys)
# import PyPDF2   #该库对中文的支持很差,所以我们使用pdfminer
# # import youdao
# # import pdfminer    #终于可以用了
#
# path="D:/360Downloads/嵌入式开发实习 - 周军 - 应届生 - 17132302080.pdf"
#
#
# with open(path,"rb") as f:
#     pdf_document=PyPDF2.PdfFileReader(f)
#     print(pdf_document.numPages)
#     first_page=pdf_document.getPage(0)
#     i=first_page.extractText()#目前仅支持word转pdf的文档提取,并且只能提取数字和英文
#     ret=""
#     for j in i:
#         if j=='\n':
#             j=''
#         ret+=j
#     print(ret)
