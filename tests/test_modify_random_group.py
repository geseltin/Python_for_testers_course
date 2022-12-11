import random
from model.group import Group
import allure


def test_modify_random_group(app, db, data_groups):
    group = data_groups
    with allure.step('Проверить наличие гргупп в системе, если нет - создать группу'):
        if app.group.count() == 0:
            app.group.create(group)
    old_group_list = db.get_group_list()

    with allure.step('Выбрать группу для изменения'):
        group.id = random.choice(old_group_list).id

    with allure.step('Изменить выбранную группу'):
        app.group.modify_group_by_id(group)

    with allure.step('Проверить изменения'):
        assert len(old_group_list) == app.group.count()

        new_group_list = db.get_group_list()
        for index, item in enumerate(old_group_list):
            if item.id == group.id:
                old_group_list[index] = group


        assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

