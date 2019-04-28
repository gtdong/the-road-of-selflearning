import sys

# print(0)
#
# sys.exit(0)
#
# print(123)

# print(sys.version)
# print(sys.maxsize)
# print(sys.platform)

# 可以实现py文件作为脚本文件执行,实现外部往内部传参
# print(sys.argv)

def copy(old_file, new_file):
    print('复制%s操作成%s' % (old_file, new_file))
def move(old_file, new_file):
    print('移动%s操作成%s' % (old_file, new_file))

method_map = {
    'copy': copy,
    'move': move
}
if len(sys.argv) > 3:
    cmd = sys.argv[1]
    old_file = sys.argv[2]
    new_file = sys.argv[3]

    if cmd in method_map:
        method_map[cmd](old_file, new_file)
    else:
        print('该功能暂未提供')



