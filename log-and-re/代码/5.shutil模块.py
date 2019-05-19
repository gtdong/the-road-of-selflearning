"""
# 基于路径的文件复制：
shutil.copyfile('source_file', 'target_file')

# 基于流的文件复制：
with open('source_file', 'rb') as r, open('target_file', 'wb') as w:
    shutil.copyfileobj(r, w)

# 递归删除目标目录
shutil.rmtree('target_folder')

# 文件移动
shutil.move('old_file', 'new_file')

# 文件夹压缩
shutil.make_archive('file_name', 'format', 'archive_path')

# 文件夹解压
shutil.unpack_archive('unpack_file', 'unpack_name', 'format')
"""
import shutil
# shutil.copyfile('4.shelve模块.py', 'target.py')
# shutil.copyfile(r'D:\python周末四期\day8\代码\4.shelve模块.py', r'D:\python周末四期\day8\代码\target\a.py')

# with open('4.shelve模块.py', 'rb') as r, open('b.py', 'wb') as w:
#     shutil.copyfileobj(r, w)

# import os
# os.rmdir(r'D:\python周末四期\day8\代码\ATM')  # 只能删空文件夹
# shutil.rmtree(r'D:\python周末四期\day8\代码\ATM')  # 递归删除

# shutil.move('b.py', 'target/bb.py')


# file_name: 压缩后得到的文件名  format：压缩格式  archive_path：要压缩的文件夹路径
# shutil.make_archive('file_name', 'format', 'archive_path')
# shutil.make_archive('target/abc', 'zip', 'source')


# unpack_file: 解压的文件  unpack_name：解压得到的文件夹名  format：解压格式
# shutil.unpack_archive('unpack_file', 'unpack_name', 'format')
shutil.unpack_archive('target/abc.zip', 'target/xyz', 'zip')

