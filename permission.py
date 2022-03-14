with open (r'C:\Users\umohumo\PycharmProjects\pythonProject\Franck\Python\Django_Projects\LDAP\last.ldap', 'r') as file:
    with open(r'C:\Users\umohumo\PycharmProjects\pythonProject\Franck\Python\Django_Projects\LDAP\permission.csv', 'w') as writen:
        
        permission = ''
        role = ''
        store = ''

        line = file.readlines()
        for record in line:
            if record.startswith('dn: cn='):
                if record.__contains__(',ou=Group,'):
                    role = record.split('=')[1].split(',')[0]
                    store = record.split('=')[3].split(',')[0]
            
            if record.startswith('PERMISSION: '):
                permission = record.split(':')[1].strip()
                writen.write (role+','+store+','+permission+'\n')
                
        print('File Created') #Generates 