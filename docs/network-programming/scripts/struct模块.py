import struct

# res = 'sjfhsdhfhfjhttrgrdgsfdgfgfgsfggdfgfsdfsdafasdfsadfsdafsdfsdafsadfsdfdsgsfdgsfdgsfdgsfdgsfdgsfdgsldgfdgfdgsfdgsfdgsfdgsdgsfdgsfdgsfdgsfdgsfdfh'
# print(len(res))
# head = struct.pack('i',len(res))
# print(len(head))
#
# real_len = struct.unpack('i',head)[0]
# print('real_len',real_len)
import json
d = {
    'file_name':'xxx',
    'file_size':123213123123234543545324546536546563465435435423543256546546635463465563565653,
    'md5':'dkfkdsafksdklafj;asfdsaf'
}
data_bytes = json.dumps(d).encode('utf-8')
print(len(data_bytes))
head = struct.pack('i',len(data_bytes))

head_bytes = struct.unpack('i',head)[0]
print(head_bytes)





