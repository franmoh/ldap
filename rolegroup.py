with open (r'C:\Users\Frank Umoh\Anaconda3\Django_Projects\LDAP\ldiffile.ldif', 'r') as file:
    with open(r'C:\Users\Frank Umoh\Anaconda3\Django_Projects\LDAP\ldifroles.csv', 'w') as writ:
        
        line = file.readlines()
        for record in line:
            if record.startswith('dn: cn='):
                if record.__contains__(',ou=Group,'):
                    
                    role = record.split('=')[1].split(',')[0]
                    store = record.split('=')[3].split(',')[0]
                    roleGroup = role +','+store +'\n'
                    writ.write(roleGroup)
                    print('File Created')