# -*- coding: utf-8 -*-
from model.contact import Contact



def test_add_user(app):
    # Авторизоваться под УЗ администратора
    app.session.login('admin', 'secret')
    # Добавить новый контакт
    app.contact.add_new(Contact())
    # Разлогиниться
    app.session.logout()











