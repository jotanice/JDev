#-*- coding: utf-8 -*-
import xlrd

workbook = xlrd.open_workbook('simples.xlsx')
worksheet = workbook.sheet_by_index(0)

for row_num in range(worksheet.nrows):
    if row_num == 0:
        continue
    row = worksheet.row_values(row_num)
    print (row)