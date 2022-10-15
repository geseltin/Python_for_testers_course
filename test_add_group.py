# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from application import Application




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    # Авторизоваться под администратором
    app.login('admin', 'secret')
    # Создать группу
    app.create_group(Group())
    # Разлогиниться
    app.logout()


def test_add_empty_group(app):

    # Авторизоваться под администратором
    app.login('admin', 'secret')
    # Открыть страницу групп
    app.create_group(Group(name=' ', header=' ', footer=' '))
    # Разлогиниться
    app.logout()


