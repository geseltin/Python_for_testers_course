# -*- coding: utf-8 -*-

import pytest

from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    # Авторизоваться под УЗ администратора
    app.factory.session.login('admin', 'secret')
    # Добавить новый контакт
    app.factory.contact.add_new(Contact())
    # Разлогиниться
    app.factory.session.logout()











