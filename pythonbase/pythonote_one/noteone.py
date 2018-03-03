# -*- coding: utf-8 -*-
#    authon:teddy
'''本节内容

    列表、元组操作
    字符串操作
    字典操作
    集合操作
    文件操作
    字符编码与转码 '''

'''1. 列表、元组操作

列表是我们最以后最常用的数据类型之一，通过列表可以对数据实现最方便的存储、修改等操作

定义列表'''

names = ['Alex',"Tenglan",'Eric']

'通过下标访问列表中的元素，下标从0开始计数'

names[0]
'Alex'
names[2]
'Eric'
names[-1]
'Eric'
names[-2] #还可以倒着取
'Tenglan'




'切片:取多个元素'
names = ["Alex","Tenglan","Eric","Rain","Tom","Amy"]
names[1:4]  #取下标1至下标4之间的数字，包括1，不包括4
['Tenglan', 'Eric', 'Rain']
names[1:-1] #取下标1至-1的值，不包括-1
['Tenglan', 'Eric', 'Rain', 'Tom']
names[0:3] 
['Alex', 'Tenglan', 'Eric']
names[:3] #如果是从头开始取，0可以忽略，跟上句效果一样
['Alex', 'Tenglan', 'Eric']
names[3:] #如果想取最后一个，必须不能写-1，只能这么写
['Rain', 'Tom', 'Amy'] 
names[3:-1] #这样-1就不会被包含了
['Rain', 'Tom']
names[0::2] #后面的2是代表，每隔一个元素，就取一个
['Alex', 'Eric', 'Tom'] 
names[::2] #和上句效果一样
['Alex', 'Eric', 'Tom']





'追加  append'
names
['Alex', 'Tenglan', 'Eric', 'Rain', 'Tom', 'Amy']
names.append("我是新来的")
names
['Alex', 'Tenglan', 'Eric', 'Rain', 'Tom', 'Amy', '我是新来的']



'插入insert'
names
['Alex', 'Tenglan', 'Eric', 'Rain', 'Tom', 'Amy', '我是新来的']
names.insert(2,"强行从Eric前面插入")
names
['Alex', 'Tenglan', '强行从Eric前面插入', 'Eric', 'Rain', 'Tom', 'Amy', '我是新来的']
names.insert(5,"从eric后面插入试试新姿势")
names
['Alex', 'Tenglan', '强行从Eric前面插入', 'Eric', 'Rain', '从eric后面插入试试新姿势', 'Tom', 'Amy', '我是新来的']



'修改'
names
['Alex', 'Tenglan', '强行从Eric前面插入', 'Eric', 'Rain', '从eric后面插入试试新姿势', 'Tom', 'Amy', '我是新来的']
names[2] = "该换人了"
names
['Alex', 'Tenglan', '该换人了', 'Eric', 'Rain', '从eric后面插入试试新姿势', 'Tom', 'Amy', '我是新来的']




'删除del or remove or pop'
del names[2] 
names
['Alex', 'Tenglan', 'Eric', 'Rain', '从eric后面插入试试新姿势', 'Tom', 'Amy', '我是新来的']
del names[4]
names
['Alex', 'Tenglan', 'Eric', 'Rain', 'Tom', 'Amy', '我是新来的']

names.remove("Eric") #删除指定元素
names
['Alex', 'Tenglan', 'Rain', 'Tom', 'Amy', '我是新来的']
names.pop() #删除列表最后一个值 
'我是新来的'
names
['Alex', 'Tenglan', 'Rain', 'Tom', 'Amy']



'扩展extend'
names
['Alex', 'Tenglan', 'Rain', 'Tom', 'Amy']
b = [1,2,3]
names.extend(b)
names
['Alex', 'Tenglan', 'Rain', 'Tom', 'Amy', 1, 2, 3]




'拷贝copy'
names
['Alex', 'Tenglan', 'Rain', 'Tom', 'Amy', 1, 2, 3]

name_copy = names.copy()
name_copy
['Alex', 'Tenglan', 'Rain', 'Tom', 'Amy', 1, 2, 3]



'统计count'
names
['Alex', 'Tenglan', 'Amy', 'Tom', 'Amy', 1, 2, 3]
names.count("Amy")
2





'排序&翻转sort  reverse'

names
['Alex', 'Tenglan', 'Amy', 'Tom', 'Amy', 1, 2, 3]
names.sort() #排序


'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: int() < str()   #3.0里不同数据类型不能放在一起排序了，擦
'''
names[-3] = '1'
names[-2] = '2'
names[-1] = '3'
names
['Alex', 'Amy', 'Amy', 'Tenglan', 'Tom', '1', '2', '3']
names.sort()
names
['1', '2', '3', 'Alex', 'Amy', 'Amy', 'Tenglan', 'Tom']

names.reverse() #反转
names
['Tom', 'Tenglan', 'Amy', 'Amy', 'Alex', '3', '2', '1']



'获取下标index'

names
['Tom', 'Tenglan', 'Amy', 'Amy', 'Alex', '3', '2', '1']
names.index("Amy")
2 #只返回找到的第一个下标






'''元组

元组其实跟列表差不多，也是存一组数，只不是它一旦创建，便不能再修改，所以又叫只读列表

语法
names = ("alex","jack","eric")
它只有2个方法，一个是count,一个是index，完毕。　　
程序练习 

请闭眼写出以下程序。

程序：购物车程序

需求:

    启动程序后，让用户输入工资，然后打印商品列表
    允许用户根据商品编号购买商品
    用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒 
    可随时退出，退出时，打印已购买商品和余额'''



'''
name.capitalize()  首字母大写
name.casefold()   大写全部变小写
name.center(50,"-")  输出 '---------------------Alex Li----------------------'
name.count('lex') 统计 lex出现次数
name.encode()  将字符串编码成bytes格式
name.endswith("Li")  判断字符串是否以 Li结尾
 "Alex\tLi".expandtabs(10) 输出'Alex      Li'， 将\t转换成多长的空格 
 name.find('A')  查找A,找到返回其索引， 找不到返回-1 

format :
    msg = "my name is {}, and age is {}"
    msg.format("alex",22)
    'my name is alex, and age is 22'
    msg = "my name is {1}, and age is {0}"
    msg.format("alex",22)
    'my name is 22, and age is alex'
    msg = "my name is {name}, and age is {age}"
    msg.format(age=22,name="ale")
    'my name is ale, and age is 22'
format_map
    msg.format_map({'name':'alex','age':22})
    'my name is alex, and age is 22'


msg.index('a')  返回a所在字符串的索引
'9aA'.isalnum()   True

'9'.isdigit() 是否整数
name.isnumeric  
name.isprintable
name.isspace
name.istitle
name.isupper
 "|".join(['alex','jack','rain'])
'alex|jack|rain'


maketrans
    intab = "aeiou"  #This is the string having actual characters. 
    outtab = "12345" #This is the string having corresponding mapping character
    trantab = str.maketrans(intab, outtab)
    
    str = "this is string example....wow!!!"
    str.translate(trantab)
    'th3s 3s str3ng 2x1mpl2....w4w!!!'

 msg.partition('is')   输出 ('my name ', 'is', ' {name}, and age is {age}') 

 "alex li, chinese name is lijie".replace("li","LI",1)
     'alex LI, chinese name is lijie'

 'msg.swapcase 大小写互换'


 msg.zfill(40)
'00000my name is {name}, and age is {age}'



n4.ljust(40,"-")
'Hello 2orld-----------------------------'
n4.rjust(40,"-")
'-----------------------------Hello 2orld'


b="ddefdsdff_哈哈" 
b.isidentifier() #检测一段字符串可否被当作标志符，即是否符合变量命名规则
True'''





'''s = set([3,5,9,10])      #创建一个数值集合

t = set("Hello")         #创建一个唯一字符的集合


a = t | s          # t 和 s的并集

b = t & s          # t 和 s的交集

c = t – s          # 求差集（项在t中，但不在s中）

d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）



基本操作：

t.add('x')            # 添加一项

s.update([10,37,42])  # 在s中添加多项



使用remove()可以删除一项：

t.remove('H')


len(s)
set 的长度

x in s
测试 x 是否是 s 的成员

x not in s
测试 x 是否不是 s 的成员

s.issubset(t)
s <= t
测试是否 s 中的每一个元素都在 t 中

s.issuperset(t)
s >= t
测试是否 t 中的每一个元素都在 s 中

s.union(t)
s | t
返回一个新的 set 包含 s 和 t 中的每一个元素

s.intersection(t)
s & t
返回一个新的 set 包含 s 和 t 中的公共元素

s.difference(t)
s - t
返回一个新的 set 包含 s 中有但是 t 中没有的元素

s.symmetric_difference(t)
s ^ t
返回一个新的 set 包含 s 和 t 中不重复的元素

s.copy()
返回 set “s”的一个浅复制
'''





'''基本操作　　
f = open('lyrics') #打开文件
first_line = f.readline()
print('first line:',first_line) #读一行
print('我是分隔线'.center(50,'-'))
data = f.read()# 读取剩下的所有内容,文件大时不要用
print(data) #打印文件

f.close() #关闭文件

打开文件的模式有：

    r，只读模式（默认）。
    w，只写模式。【不可读；不存在则创建；存在则删除内容；】
    a，追加模式。【可读；   不存在则创建；存在则只追加内容；】

"+" 表示可以同时读写某个文件

    r+，可读写文件。【可读；可写；可追加】
    w+，写读
    a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

    rU
    r+U

"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

    rb
    wb
    ab
'''