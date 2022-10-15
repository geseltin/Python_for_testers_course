# -*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


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


