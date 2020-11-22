#
# A simple example of merging cells with the XlsxWriter Python module.
#
# Copyright 2013-2020, John McNamara, jmcnamara@cpan.org
#
import xlsxwriter

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('../test3.xlsx')
worksheet = workbook.add_worksheet()

# Increase the cell size of the merged cells to highlight the formatting.
worksheet.set_column('B:D', 12)
worksheet.set_row(3, 30)
worksheet.set_row(6, 30)
worksheet.set_row(7, 30)

# Create a format to use in the merged range.
merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'yellow'})

merge_format2 = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'red'})

data = {
    'start_col': 'B'
}
# Merge 3 cells.
# worksheet.merge_range('B4:D4', 'Merged Range', merge_format)

# Merge 3 cells over two rows.
# worksheet.merge_range('B7:D8', 'Merged Range', merge_format)
#
# worksheet.merge_range('B10:B11', 'Merged Range', merge_format2)

worksheet.merge_range(first_row=1, first_col=3, last_row=3, last_col=4, data='Merged Range',
                      cell_format=merge_format2)
#
# worksheet.merge_range(first_row=12, first_col=14, last_col=15, last_row=13, data='Merged Range',
#                       cell_format=merge_format2)

workbook.close()
