import random
from model.group import Group



def test_modify_random_group(app, db, data_groups):
    group = data_groups
    if app.group.count() == 0:
        app.group.create(group)
    old_group_list = db.get_group_list()
    group.id = random.choice(old_group_list).id
    app.group.modify_group_by_id(group)

    assert len(old_group_list) == app.group.count()

    new_group_list = db.get_group_list()
    for index, item in enumerate(old_group_list):
        if item.id == group.id:
            old_group_list[index] = group


    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

