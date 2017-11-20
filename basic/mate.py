#纯数字
numeric = 9527

#字符串与数字连接
string = '$' + str(numeric)

#重复三次
print(withOperator * 3)

#多行
multiLine = "竟然是这样的P" \
            "y代码"

multiLine = '''
这你信么？
多行竟然长这样
强大的php只需要"
    还记得php
    强大的字符
    串么
"
'''

#使用动态变量
shadowMultiBlock = 'multiBlock' #dddd
print(locals()[shadowMultiBlock])

#使用变量
mstring = len(locals()[string])
for i in range(0, shadowMultiBlockLenght):
    print(shadowMultiBlock[i])

#列表使用 址复制
sharingan = ['list', 'detail', 'gogoing']
sharinganCopy = sharingan
sharingan += [111]

#列表使用 值复制
sharingan = ['list', 'detail', 'gogoing']
sharinganCopy = sharingan[:]
sharingan += [111]
print(sharingan)
print(sharinganCopy)
print(id(sharingan))
print(id(sharinganCopy))

#*地址相同
shadow = sharingan * 3
print(shadow)
#i为值
for i in shadow:
    print(i, id(i))

exit()


#dict
shadow = {'hello': 'shinagawa', 'world': 'tokyo'}
#i为键
for i in shadow:
    print(i, id(i), shadow[i])
print(shadow)

exit()

#定义函数
def closure(formal_parameter):
    print(formal_parameter)
    return 'return_result'

#动态回调
params = []
result = eval('originClosure')('formal_parameter')
print(result)

exit()

#Class
class DemoClass:
    "类名字注释"
    __prop_project = '默认项目'
    def __private_echo(self, params):
        print(params)

    def echo(self, params):
        self.__private_echo(params)
demo = DemoClass()
demo.echo('newobject')