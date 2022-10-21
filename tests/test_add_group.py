# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Создать группу
    app.group.create(Group())
    app.session.logout()


def test_add_empty_group(app):
    # Открыть страницу групп
    app.group.create(Group(name=' ', header=' ', footer=' '))


