try:
    fh = open("testfile", "x")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 文件已经存在")
else:
    print ("内容写入文件成功")
    fh.close()