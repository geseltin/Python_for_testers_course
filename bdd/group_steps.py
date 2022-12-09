from pytest_bdd import given, when, then, parsers
from model.group import Group
import random



@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()


@given(parsers.parse('a group with {name}, {header}, and {footer}'), target_fixture='new_group')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_group_list = group_list
    new_group_list = db.get_group_list()
    old_group_list.append(new_group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


@given('check if group list is not empty', target_fixture='create_group_if_list_is_empty')
def create_group_if_list_is_empty(app):
    group = Group(name=''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8)),
                  header=''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8)),
                  footer=''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8)))
    if app.group.count() == 0:
        app.group.create(group)


@given('choose random group and generate data to modify', target_fixture='random_group_and_data')
def random_group_and_data(group_list):
    group = Group(name=''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8)),
                  header=''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8)),
                  footer=''.join(random.choices('ABCDEFGHIJKLMOPQRSTUVWXYZ', k=8)))
    group.id = random.choice(group_list).id
    return group

@when('modify random group')
def modify_random_group(app, random_group_and_data):
    app.group.modify_group_by_id(random_group_and_data)


@then('the new group list is equal to the old list with modified group')
def verify_group_lists_after_modify(db, group_list, random_group_and_data):
    old_group_list = group_list
    new_group_list = db.get_group_list()

    for index, item in enumerate(old_group_list):
        if item.id == random_group_and_data.id:
            old_group_list[index] = random_group_and_data
            break

    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


@given('choose random group', target_fixture='choose_random_group')
def choose_random_group(group_list):
    group = random.choice(group_list)
    return group

@when('delete group')
def delete_group(app, choose_random_group):
    app.group.delete_group_by_id(choose_random_group.id)


@then('the new group list is equal to the old list without deleted group')
def verify_group_lists_after_delete(db, choose_random_group, group_list):
    new_group_list = db.get_group_list()

    group_list.remove(choose_random_group)
    assert sorted(new_group_list, key=Group.id_or_max) == sorted(group_list, key=Group.id_or_max)




