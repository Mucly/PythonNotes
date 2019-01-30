# -*- coding:utf-8 -*-
# install : cmd >>> pip install xlrd && pip install xlwt
# 为简便代码，实例的方法以层级缩进的方式展示
import xlrd
import xlwt

# xls读取操作
# PART 1 打开目标xls文件
xlrd.open_workbook(xls_path)  # 返回一个workbook实例，代表载入的xls
# PART 2 workbook实例方法，打开该xls的目标sheet后返回一个sheet实例
    .sheet_by_index(sheetx)  # 通过index确认目标   同 .sheets()[sheet_indx]
    .sheet_by_name(sheet_name)  # 通过sheet名确认

    .sheet_names()  # return sheet_name list
    .sheet_loaded(sheet_name or sheetx)   # check sheet loaded status
# PART 3 sheet实例方法，各种行、列、单元格读取操作
    # row operate
        .nrows  # get vaild rows num
        .row(rowx)  # 返回该行所有的单元格对象组成的list, 同 .row_slice
        .row_values(rowx, start_colx=0, end_colx=None)   # 返回由该行中所有单元格的数据组成的list
        .row_len(rowx)  # 返回该行的有效单元格长度
    # colnum operate
        .ncols   # get vaild cols num
        .col(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的list, 同 .col_slice
        .col_values(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据组成的list
        .col_len(rowx)  # 返回该列的有效单元格长度
    # cell operate
        .cell(rowx, colx)  # 返回单元格对象
        .cell_type(rowx, colx)  # 返回单元格中的数据类型
        .cell_value(rowx, colx)  # 返回单元格中的数据

# xls写入操作
# PART 1 新建一个xls，编码为utf-8后返回一个workbook实例
xlwt.Workbook(encoding='utf-8')
# PART2 workbook实例方法：创建一个sheet，名字自定
    .add_sheet('sheet_name')  # create a new sheet
# PART3 sheet实例方法：按行号和列号，写入数据
        .write(rowx, colx, label=value)  # 行、列、值
# PART4 workbook实例方法：保存
    .save('xls_filename.xls')
