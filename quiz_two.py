#简述with方法打开处理文件帮我我们做了什么？
f=open("./1.txt","wb")
try:
    f.write("hello world")
except:
        pass
finally:
        f.close()