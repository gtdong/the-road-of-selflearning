import xlrd

"""
# 读取文件
work_book = xlrd.open_workbook("my.xlsx")
# 获取所有所有表格名称
print(work_book.sheet_names())
# 选取一个表
sheet = work_book.sheet_by_index(0)
# 表格名称
print(sheet.name)
# 行数
print(sheet.nrows)
# 列数
print(sheet.ncols)
# 某行全部
print(sheet.row(6))
print(sheet.row(13))
# 某列全部
print(sheet.col(4))
# 某行列区间
print(sheet.row_slice(6, start_colx=0, end_colx=4))
# 某列行区间
print(sheet.col_slice(3, start_rowx=0, end_rowx=3))
# 某行类型0：空 1：str 2：num 3：date | 值
print(sheet.row_types(1), sheet.row_values(6))

# 单元格
print(sheet.cell(6,0).value) # 取值
print(sheet.cell(6,0).ctype) # 取类型
print(sheet.cell_value(6,0)) # 直接取值
print(sheet.cell_type(6,0)) # 直接取类型

# 0：以1900年为基准 1：以1904年为基准
print(xlrd.xldate_as_datetime(sheet.cell(6, 0).value, 0))
"""


import xlwt
# 创建工作簿
work = xlwt.Workbook()
# 创建一个表
sheet = work.add_sheet("员工信息数据")
# 创建一个字体对象
# font = xlwt.Font()
# font.name = "Times New Roman"  # 字体名称
# font.bold = True  # 加粗
# font.italic = True  # 斜体
# font.underline = True  # 下划线
# 创建一个样式对象
# style = xlwt.XFStyle()
# style.font = font
keys = ['Owen', 'Zero', 'Egon', 'Liuxx', 'Yhh']
# 写入标题
c = 0
for k in keys:
    # sheet.write(0, keys.index(k), k, style)
    # sheet.write(0, keys.index(k), k)

    sheet.write(keys.index(k) + 5, 2, k if k != 'Egon' else 'cool')
    # sheet.write(c, c, k)
    # c += 1

# 写入数据
# sheet.write(1, 0, 'cool', style)
# sheet.write(0, 0, 'cool')
# 保存至文件
work.save("new_my.xls")

