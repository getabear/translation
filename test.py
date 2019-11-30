import youdao
import analytical_pdf
a=youdao.youdao()
path="./text.pdf"
analytical_pdf.parse(path,"./2.txt")
with open ("./2.txt","r") as f:
    text=f.read()
    print(text)
