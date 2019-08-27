from pygsheet import *
import worksheet

gc = pygsheets.authorize(service_file='read.json')
sh = gc.open('報到系統')
wks=sh[0]
wks.title = '報到名單'
wks_list = sh.worksheets()
a1 = wks.cell('E2')
c1 = worksheet.cell('E1')
c2 = c1.neighbour('topright')
print(c2.value)
print(a1.value)
print(wks_list)
'''
c1 = worksheet.cell('名單')
c2 = c1.neighbour('F130129738')
print(c2.value)
'''
