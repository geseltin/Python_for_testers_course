from model.group import Group


def test_modify_first_group(app):
    old_group_list = app.group.get_group_list()
    group = Group(name='test_name', header='test_header', footer='test_footer')
    if app.group.count() == 0:
        app.group.create(Group(name='test_name', header='test_header', footer='test_footer'))
    group.id = old_group_list[0].id
    app.group.modify_first_group(group)
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

