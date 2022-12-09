from pytest_bdd import scenario
from .group_steps import *



@scenario('groups.feature', 'add new group')
def test_add_new_group():
    pass

@scenario('groups.feature', 'modify random group')
def test_modify_random_group():
    pass

@scenario('groups.feature', 'delete random group')
def test_delete_random_group():
    pass