#-*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import xlwt

from datetime import datetime
import databases


workbook = xlwt.Workbook()
worksheet = workbook.add_sheet(u'Simples')
worksheet.write(0, 0, u'ID Produto')
worksheet.write(0, 1, u'Nome Produto')
worksheet.write(0, 2, u'Descricao')

x = 53
worksheet.write(1,0, (x))
workbook.save('simples.xlsx')

workbook.read('simples.xlsx')