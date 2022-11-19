import pymysql
from fixture.orm import OrmFixture
from model.group import Group

db = OrmFixture(host='127.0.0.1',
                             user='root',
                             password='',
                             database='addressbook')


try:
    list = db.get_contact_list()
    for i in list:
        print(i)

finally:
    pass