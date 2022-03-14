with open (r'C:\Users\Frank Umoh\Anaconda3\Django_Projects\LDAP\ldiffile.ldif', 'r') as file:
    with open(r'C:\Users\Frank Umoh\Anaconda3\Django_Projects\LDAP\clmUsers.csv', 'w') as written:

        class LdapReader:

            def __init__(self, username, store, creation_date, firstname, location,
                         number, xdirectory, email, lastname, surname):
                self.username = username
                self.store = store
                self.creation_date = creation_date
                self.firstname = firstname
                self.location = location
                self.number = number
                self.xdirectory = xdirectory
                self.email = email
                self.lastname = lastname
                self.surname = surname

                line = file.readlines()
                for record in line:
                    if record.startswith('dn: cn='):
                        if record.__contains__(',ou=People,'):
                            username = record.split('=')[1].split(',')[0]
                            store = record.split('=')[3].split(',')[0]
                            print(username,store)
        run = LdapReader()


