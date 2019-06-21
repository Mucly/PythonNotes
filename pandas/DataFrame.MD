# 介绍  
   + 类二维数组结构  
   + 可看做是Python版的excel表格（行、列）  

```python
    df = pandas.DataFrame(data, index, columns, dtype, copy) # 创建一个dataframe实例  
```


# 索引方式 
1. 直接索引（范围）  
```python
df[col_lable] # 列标签，可接受一个数组 eg. df[ ['A','B','C'] ] => 返回ABC三列的dataframe实例
```

2. Label索引（范围）  
```python
df.loc[row_label, col_label] # 这里的label可以是范围列表(双侧闭区间)
```

3. index索引（范围）  
```python
df.iloc[rowx, colx] # 这里的rowx和colx可以是范围列表（双侧闭区间）
```

4. Label/index 混合索引（范围）  
```python
df.ix(行,列) # 这里行列可以是行列的inx，也可以是行列的label。使用方式可参考上述1、2两条
```

5. 单一元素索引  
```python
df.at[rowx, col_label] # eg. df.at[0, 'a']
df.iat[rowx, colx] # eg. df.iat[0, 0]
```
