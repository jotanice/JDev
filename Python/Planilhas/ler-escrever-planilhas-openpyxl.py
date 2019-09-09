from openpyxl import load_workbook

wb = load_workbook(filename = 'simples.xlsx')
sheet_ranges = wb['range names']
print(sheet_ranges['D18'].value)