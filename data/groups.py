import string
import random
from model.group import Group



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 22)]]


# testdata = [
#     Group(name="name1", header="header1", footer="footer1"),
#     Group(name="name2", header="header2", footer="footer2")
# ]
