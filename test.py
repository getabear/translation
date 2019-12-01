from youdao import youdao
a=youdao()
with open("./1.txt","r") as f:
    temp_str=f.readline()
    while(temp_str):
        print(temp_str)
        temp_str = f.readline()


