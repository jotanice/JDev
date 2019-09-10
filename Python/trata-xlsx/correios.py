#-*- coding:utf-8 -*-
import numpy
import xlwt
import xlrd
#from databases import get_database
from datetime import datetime

# lê planilha de range de ceps (correios_cep.xlsx)

wbcep = xlrd.open_workbook('correios_cep.xlsx')
wscep = workbook.sheet_by_name('Capitais')

for row_num in range(wscep.nrows):
    if row_num == 0:
        continue
    row = wscep.row_values(row_num)

# cruza correios_cep.xlsx com mod_import_frete_jet.xlsx

wb_impfrete = xlwt.Workbook()
ws_impfrete = wb_impfrete.(u'Tab_Frete')

ws_impfrete.write(x, y, datetime.now(), style=xlwt.easyxf(num_format_str='dd/mm/yyyy hh:mm:ss'))

wb_impfrete.save('mod_import_frete_jet_teste.xls')