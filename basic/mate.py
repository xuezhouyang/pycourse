#纯数字
withoutDollar = 9527
print(withoutDollar)

#数字不可用直接与字符串连接
withOperator = '$' + str(withoutDollar)
print(withOperator)


#重复三次
print(withOperator * 3)

#整形于浮点
floatDemo = 9888.8888
print(floatDemo + withoutDollar)

multiLine = "竟然是这样的P" \
            "y代码"
print(multiLine)

#比PHP弱爆了的字符串
multiBlock = '''
这事啥东西你信么？
多行竟然长这样
强大的php只需要"
    还记的php
    强大的字符
    串么
"
'''
print(multiBlock)

#使用动态变量
shadowMultiBlock = 'multiBlock'
print(locals()[shadowMultiBlock])


#使用变量
shadowMultiBlockLenght = len(shadowMultiBlock)
for i in range(0, shadowMultiBlockLenght):
    print(shadowMultiBlock[i])

#列表使用 址复制
sharingan = ['list', 'detail', 'gogoing']
sharinganCopy = sharingan
sharingan += [111]
print(sharingan)
print(sharinganCopy)
print(id(sharingan))
print(id(sharinganCopy))

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

#dict
shadow = {'hello': 'shinagawa', 'world': 'tokyo'}
#i为键
for i in shadow:
    print(i, id(i), shadow[i])
print(shadow)

#定义函数
def originClosure(formal_parameter):
    print(formal_parameter)
    return 'return_result'

#动态回调
params = []
result = eval('originClosure')('formal_parameter')
print(result)

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