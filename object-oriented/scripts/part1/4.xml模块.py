import xml

# xml文件：1.作为传输文件用于数据的传输  2.作为配置文件配置信息
"""
1.只能由一个根标签
2.所有的标签都是自定义的
3.标签名就是key，标签的内容就是value
4.与json不同的是，标签不仅可以有key和value，还有标签的属性
注：xml的属性通常用来表示标签间的区分度，用于解析xml来使用
"""
"""
{"countrys": [
    {
        "rank": 2,
        "year": 2008,
        "gdppc": 141100
    },
    {},
    {}
]}

{
    "data": {
        "countrys": [
            {},
            {},
            {}
        ]
    }
}
"""

# xml的文件解析 => 将xml转化为json类型的数据
# dict list => json

import xml.etree.ElementTree as ET

"""
# 读文件
tree = ET.parse("my.xml")
# print(tree)  # xml.etree.ElementTree.ElementTree
# 根节点
root_ele = tree.getroot()
# print(root_ele)  # Element 'data'

# 遍历往下
# print(root_ele[1])
for ele in root_ele:
    print(ele, ele.attrib)
    if ele.attrib['name'] == 'Singapore':
        for e in ele:
            print(e, e.tag)
            if e.tag == 'gdppc':
                print(e.text)
                e.text = '88888'  # 只修改了内容

# 全文搜索指定名的子标签
# ele.iter("标签名")
# 非全文查找满足条件的第一个子标签
# ele.find("标签名")
# 非全文查找满足条件的所有子标签
# ele.findall("标签名")
print('==============')
cs = root_ele.iter('country')
for c in cs:
    print(c)
print('==============')
print(root_ele.find('country').attrib)
# print(root_ele.find('rank').attrib)  # 不能跨标签取，只能取子标签
print('==============')
print(root_ele.findall('country'))


# 将内存的数据重新写入文件
tree.write("my.xml")
"""
"""
{
    "countrys": [
        {
            "rank": 2,
            "year": 2008,
            "gdppc": 141100
        }
    ]
}
"""
data = {'countrys': []}
tree = ET.parse("my.xml")
root = tree.getroot()
for ele in root:
    country = {}
    for e in ele:
        if e.text and e.text.strip():
            country[e.tag] = e.text
    data['countrys'].append(country)
print(data)





