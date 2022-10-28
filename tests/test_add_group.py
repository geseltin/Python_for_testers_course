# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_group_list = app.group.get_group_list()
    app.group.create(Group())
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)


def test_add_empty_group(app):
    old_group_list = app.group.get_group_list()
    app.group.create(Group(name=' ', header=' ', footer=' '))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)


