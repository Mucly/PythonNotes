# csv库的使用
```python
import csv
```

## 写入
```python
stu1 = ['a', 26]
stu2 = [['b', 27,], ['c', 28]]

# 这里用了“追加写”的模式；newline必须加，否则多空行
with open("1.csv", "w", newline="") as fd:  # newline必须加，否则会多行
    # 写入模式
    csv_write = csv.writer(fd)

    # 写单行
    csv_write.writerow(stu1) # stu1 = ['a', 26]

    # 写多行
    csv_write.writerows(stu2) # stu2 = [['b', 27,], ['c', 28]]

```

## 读取
```python
with open('stu.csv') as fd:
    csv_reader = csv.reader(fd)

    for line in csv_reader:
        print(line)
```