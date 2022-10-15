# -*- coding: utf-8 -*-

import pytest

from model.contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    # Авторизоваться под УЗ администратора
    app.login('admin', 'secret')
    # Добавить новый контакт
    app.add_new_contact(Contact())
    # Разлогиниться
    app.logout()











