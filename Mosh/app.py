import openpyxl as xl
from os.path import join, realpath, dirname

cwd = join(dirname(__file__),"transactions.xlsx")
folha = xl.load_workbook(cwd)['Sheet1']


