#pip3 install mysql-connector-python-rf

from sqlalchemy import *

numeric = 9527

string = str('multi')

multi ='''
php只需要
"扩起来"
'''

length = len(locals()[string])
for i in range(0, length):
    print(i)


engine = create_engine( 'mysql+mysqlconnector://xxxxxxx:xxxxxx@xxxxxxxxxx:0000/xxxxxxx' )

result = engine.execute(
    "SELECT * FROM warranties WHERE id BETWEEN %(start)s AND %(end)s",
    start=400000, end=405000
)
ret = result.fetchall()
for item in ret:
    print(id(item), item)