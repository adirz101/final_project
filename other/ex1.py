import cplex
import pandas
import xlrd

# problem = cplex.Cplex()
# n=3 #number of techers
# t=5 #number of cels
# c=2 #number of cours
#
# x=[[[0 for k in range(c)] for j in range(t)]for i in range(n)]


fileName = 'Workbook1.xlsx'
workbook = xlrd.open_workbook(fileName)
for sheet in workbook.sheets():
    print(sheet.name)
    num_rows = sheet.nrows  # Number of Rows
    num_cols = sheet.ncols  # Number of Columns
    result_data = []
    for curr_row in range(0, num_rows):
        row_data = []
        for curr_col in range(0, num_cols):
            data = sheet.cell_value(curr_row, curr_col)  # Read the data in the current cell
            row_data.append(data)
        result_data.append(row_data)
        print(result_data)




print(result_data)
