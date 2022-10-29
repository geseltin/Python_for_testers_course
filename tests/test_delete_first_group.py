from model.group import Group


def test_delete_first_group(app):
    old_group_list = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='test_name', header='test_header', footer='test_footer'))
    app.group.delete_first()
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) - 1 == app.group.count()
    old_group_list[0:1] = []
    assert old_group_list == new_group_list

