from xml.dom.minidom import parse
from analyze_mat import *
# 读取文件
dom = parse('book.xml')
# 获取文档元素对象
data = dom.documentElement
# 获取 student
stus = data.getElementsByTagName('student')
for stu in stus:
	# 获取标签属性值
    st_id = stu.getAttribute('id')
    st_name = stu.getAttribute('name')
	# 获取标签中内容
    id = stu.getElementsByTagName('id')[0].childNodes[0].nodeValue
    name = stu.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = stu.getElementsByTagName('age')[0].childNodes[0].nodeValue
    gender = stu.getElementsByTagName('gender')[0].childNodes[0].nodeValue
    print('st_id:', st_id,  ', st_name:',st_name)
    print('id:', id, ', name:', name, ', age:', age, ', gender:',gender)

print("    ")

for stu in stus:
    st_id = stu.getAttribute('id')
    st_name = stu.getAttribute('name')
    # 获取标签中内容
    id = stu.getElementsByTagName('id')[0].childNodes[0].nodeValue
    name = stu.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = stu.getElementsByTagName('age')[0].childNodes[0].nodeValue
    gender = stu.getElementsByTagName('gender')[0].childNodes[0].nodeValue
    guid = generate_GUID()
    # print("id=%s"%id)
    print("value=%s" %id, " ", "GUID=%s" %guid)
    guid = generate_GUID()
    print("name=%s"%name, ' ', "GUID=%s" %guid)
    guid = generate_GUID()
    print("age=%s"%age, ' ', "GUID=%s" %guid)
    guid = generate_GUID()
    print("gender=%s"%gender, ' ', "GUID=%s" %guid)
