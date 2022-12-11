from model.group import Group
import random
import allure



def test_delete_random_group(app, db, check_ui):
    with allure.step('Проверить наличие хотя бы одной группы, если нет - создать'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name='test_name', header='test_header', footer='test_footer'))

    with allure.step('Получить текущий список групп'):
        old_group_list = db.get_group_list()

    with allure.step('Выбрать случайную группу'):
        group = random.choice(old_group_list)

    with allure.step('Удалить выбранную группу'):
        app.group.delete_group_by_id(group.id)

    with allure.step('Проверить что группа удалена'):
        new_group_list = db.get_group_list()
        assert len(old_group_list) - 1 == app.group.count()
        old_group_list.remove(group)
        assert old_group_list == new_group_list
        if check_ui:
            assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

