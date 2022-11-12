from model.contact import Contact



testdata = [Contact(first_name=Contact.generate_data(Contact), last_name=Contact.generate_data(Contact),
                    mid_name=Contact.generate_data(Contact), nickname=Contact.generate_data(Contact),
                    phone_mobile=Contact.generate_mobile_phone(Contact), phone_home=Contact.generate_home_phone(Contact),
                    phone_work=Contact.generate_work_phone(Contact), email1=Contact.generate_email(Contact),
                    email2=Contact.generate_email(Contact), email3=Contact.generate_email(Contact),
                    address=Contact.generate_address(Contact))]