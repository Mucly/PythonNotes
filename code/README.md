#Python编码
##编码的作用
- <strong>所有数据</strong>实际均以<strong>二进制</strong>形式（bytes）进行处理（硬盘存储、网络数据传输）

    #encode编码方法  
    \# S.encode(code) -> bytes
    str1 = "好"
    str1.encode('gbk') \# 以code编码对unicode对象S（字符串）进行编码