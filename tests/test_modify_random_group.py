from model.group import Group
from random import randrange


def test_modify_random_group(app, json_groups):
    group = json_groups
    if app.group.count() == 0:
        app.group.create(group)
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    group.id = old_group_list[index].id
    app.group.modify_group_by_index(group, index)

    assert len(old_group_list) == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

