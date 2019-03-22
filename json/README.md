# json库的使用
```python
import json

# json对象 / data.json文件内容（去掉变量名和等号）
j_data = {
  "results": [ 
      {
          "location": 
          {
              "id": "WX4FBXXFKE4F",
              "name": "北京",
              "country": "CN",
              "path": "北京,北京",
              "timezone": "Asia/Shanghai",
              "timezone_offset": "+08:00"
          }
      }]
}

# 内容是json格式的字符串
j_str = '''{"results": [{"location": {"id": "WX4FBXXFKE4F", "name": "\u5317\u4eac", "country": "CN", "path": "\u5317\u4eac,\u5317\u4eac", "timezone": "Asia/Shanghai", "timezone_offset": "+08:00"}}]}'''
```

## load 读 \[ str => json \]
1 . load(fd)  ```[文件读] # 读取fd中的字符串内容，并以json格式返回```
```python
  with open('data.json') as fd:
    a = json.load(fd) # >>> "{"results": [{"location" ... +08:00"}}]}"
```
2 . loads(s) ```[字符读] # 读取s，并以json格式返回```
```python
    dict1 = json.loads(j_str) # >>> {"results": [{"loc ... +08:00"}}]}  < class 'dict' >
```

## dump 写 \[ json => str \]
1 . dump(json, fd) ```[文件写]# 将json => str，并写入到fd中```
```python
with open("data.json", 'w') as fd:
  json.dump(j_data, fd) # 无返回值
```
2 . dumps(json) ```[字符写]# 将json => str```
```python
  str1 = json.dumps(j_data)
  print(str1) # >>> "{"results": [{"loc ... +08:00"}}]} " < class 'str' >
```