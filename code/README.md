# Python编码
## 编码的作用
- <strong>所有数据</strong>实际均以<strong>二进制</strong>形式（bytes）进行处理（硬盘存储、网络数据传输）

## encode 编码
```python
# unicode_obj.encode(code) -> bytes_obj

str1 = "好".encode('gbk') # 将unicode对象字符串"好"，以gbk编码进行编码
```


## decode 解码
```python
# bytes_obj.decode(code) -> unicode_obj

str2 = str1.decode('gbk') # 以gbk编码规则对str1进行解码，以获取unicode对象
```
