import shelve


shv_tool = shelve.open('c.shv')

# 序列化
# shv_tool['name'] = 'Owen'

# 反序列化
res = shv_tool['name']
print(res)


shv_tool.close()
# 文件通过shelve对象来关闭
# res = shv_tool['name']
# print(res)


# 二次操作
# shv_tool = shelve.open('c.shv')
# print(shv_tool['name'])
# shv_tool.close()

with shelve.open('c.shv') as shv_tool:
    print(shv_tool['name'])



# writeback将反序列化到内存的数据，操作后即时同步到文件中
with shelve.open('c.shv', writeback=True) as shv_tool:
    shv_tool['stus'] = ['Bob', 'Tom']
    # print(shv_tool['stus'])

    shv_tool['stus'].append('Jobs')
    print(shv_tool['stus'])

