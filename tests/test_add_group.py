import string

from model.group import Group
import pytest
import random



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 22)]]

@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_group_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)







