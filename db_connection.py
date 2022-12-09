from fixture.orm import OrmFixture
from fixture.db import DbFixture

# db = OrmFixture(host='127.0.0.1',
#                              user='root',
#                              password='',
#                              database='addressbook')
db = DbFixture(host='127.0.0.1',
                             user='root',
                             password='',
                             database='addressbook')


try:
    # list = db.get_contact_list()
    # for i in list:
    #     print(i)
    with db.connection.cursor() as cursor:
        rows = cursor.execute("SELECT * FROM address_in_groups")
        result = cursor.fetchone()
        print(result)
finally:
    pass