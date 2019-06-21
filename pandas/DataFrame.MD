## 介绍
   + 二维数组结构
   + 可看做是Python版的excel表格（行、列）

```python
    df = pandas.DataFrame(data, index, columns, dtype, copy) # 创建一个dataframe实例
```


## 索引方式
1.直接索引  
```python
df[col_lable] # 列标签，可接受一个数组 eg. df[ ['A','B','C'] ] => 返回ABC三列的
```
