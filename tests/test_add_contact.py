# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_user(app):
    # Авторизоваться под УЗ администратора
    app.factory.session.login('admin', 'secret')
    # Добавить новый контакт
    app.factory.contact.add_new(Contact())
    # Разлогиниться
    app.factory.session.logout()











