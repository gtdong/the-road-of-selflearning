"""
生成单级目录：os.mkdir('dirname')
列举目录下所有资源：os.listdir('dirname')
重命名：os.rename("oldname","newname")
"""
import os
# os.mkdir('a')
# os.makedirs('a/b/c')
# os.rename("a", "b")


"""
将path分割成目录和文件名二元组返回：os.path.split(path)
指定路径是否存在：os.path.exists(path)
是否是文件：os.path.isfile(path)
是否是路径：os.path.isdir(path) 
路径拼接：os.path.join(path1[, path2[, ...]])
目标大小：os.path.getsize(path)
"""
path = r'D:\python周末四期\day06\代码\part14\17.os模块.py'
print(os.path.split(path))
print(os.path.exists(path))
print(os.path.isfile(path))
print(os.path.isdir(path))

# folder = r'D:\python周末四期\week6_0427\代码\part14'
folder = work_dir = os.getcwd()
file = '17.os模块.py'
# path = folder + os.sep + file
# path = os.path.join(r'D:\python周末四期', 'week6_0427', '代码', 'part14', file)
path = os.path.join(work_dir, file)
print(os.path.exists(path))
print(os.path.getsize(path))


