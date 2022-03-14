with open (r'C:\Users\umohumo\PycharmProjects\pythonProject\Franck\Python\Django_Projects\LDAP\last.ldap', 'r') as file:
    with open(r'C:\Users\umohumo\PycharmProjects\pythonProject\Franck\Python\Django_Projects\LDAP\UsersInGroups.csv', 'w') as writen:
        
        user=''

        line = file.readlines()
        for record in line:
            if record.startswith('dn: cn='):
                if record.__contains__(',ou=Group,'):
                    role = record.split('=')[1].split(',')[0]
                    store = record.split('=')[3].split(',')[0]
            
            if record.startswith('MEMBERUID: '):
                if record.__contains__(',ou=People,'):
                    user = record.split('=')[1].split(',')[0]
                    writen.write (role+','+store+','+user+'\n')
        print('File Created')