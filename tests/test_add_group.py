import allure
from model.group import Group
import pytest



def test_add_group(app, db, json_groups):
    group = json_groups
    with allure.step('Given a group list'):
        old_group_list = db.get_group_list()
    with allure.step('When I add the group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_group_list = db.get_group_list()
        old_group_list.append(group)
        assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)







