from model.group import Group


def test_modify_first_group(app):
    old_group_list = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='test_name', header='test_header', footer='test_footer'))
    app.group.modify_first_group()
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)

