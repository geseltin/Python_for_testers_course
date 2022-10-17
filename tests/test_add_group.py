# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Авторизоваться под администратором
    app.session.login('admin', 'secret')
    # Создать группу
    app.group.create(Group())
    # Разлогиниться
    app.session.logout()


def test_add_empty_group(app):

    # Авторизоваться под администратором
    app.session.login('admin', 'secret')
    # Открыть страницу групп
    app.group.create(Group(name=' ', header=' ', footer=' '))
    # Разлогиниться
    app.session.logout()


