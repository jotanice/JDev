#-*- coding:utf-8 -*-
import pandas as pd

wbfrete = pd.read_excel('mod_import_frete_jet.xlsx')
#wbfrete = pd.DataFrame([])
#wbfrete = pd.write.
#wbfrete['PesoInicio']

wbfrete.loc[5,'Nome'] = wbfrete.loc[10,'Nome']
wbfrete.loc[1:10,'Nome']
#wbfrete.head(n=1)
#wbfrete.loc[1,'nome']
#print(wbfrete)