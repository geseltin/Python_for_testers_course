# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Авторизоваться под администратором
    app.factory.session.login('admin', 'secret')
    # Создать группу
    app.factory.group.create(Group())
    # Разлогиниться
    app.factory.session.logout()


def test_add_empty_group(app):

    # Авторизоваться под администратором
    app.factory.session.login('admin', 'secret')
    # Открыть страницу групп
    app.factory.group.create(Group(name=' ', header=' ', footer=' '))
    # Разлогиниться
    app.factory.session.logout()


