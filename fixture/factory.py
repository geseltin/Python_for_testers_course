from fixture.contact import ContactHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper



class Factory:

    def __init__(self, app):
        self.session = SessionHelper(app)
        self.group = GroupHelper(app)
        self.contact = ContactHelper(app)