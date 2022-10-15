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
    app.create_group(Group())
    # Разлогиниться
    app.session.logout()


def test_add_empty_group(app):

    # Авторизоваться под администратором
    app.session.login('admin', 'secret')
    # Открыть страницу групп
    app.create_group(Group(name=' ', header=' ', footer=' '))
    # Разлогиниться
    app.session.logout()


