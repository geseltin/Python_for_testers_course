import pymysql
from fixture.orm import OrmFixture
from model.group import Group

db = OrmFixture(host='127.0.0.1',
                             user='root',
                             password='',
                             database='addressbook')


try:
    list = db.get_contacts_not_in_group(Group(id="278"))
    for item in list:
        print(item)
    print(len(list))

finally:
    pass