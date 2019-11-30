import youdao
import analytical_pdf
a=youdao.youdao()
path="./web.pdf"
# path="D:/360Downloads/嵌入式开发实习 - 周军 - 应届生 - 17132302080.pdf"
analytical_pdf.parse(path,"./2.txt")
with open ("./2.txt","r",encoding='utf-8') as f:
    text=f.read()
    print(text)
