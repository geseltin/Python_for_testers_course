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


