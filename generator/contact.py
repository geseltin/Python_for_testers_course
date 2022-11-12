import sys
import getopt
import os.path
import jsonpickle
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 2
file = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        file = a

testdata = [Contact(first_name=Contact.generate_data(Contact), last_name=Contact.generate_data(Contact),
                    mid_name=Contact.generate_data(Contact), nickname=Contact.generate_data(Contact),
                    phone_mobile=Contact.generate_mobile_phone(Contact), phone_home=Contact.generate_home_phone(Contact),
                    phone_work=Contact.generate_work_phone(Contact), email1=Contact.generate_email(Contact),
                    email2=Contact.generate_email(Contact), email3=Contact.generate_email(Contact),
                    address=Contact.generate_address(Contact)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
