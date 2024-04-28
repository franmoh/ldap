with open (r'C:\Users\Frank Umoh\Anaconda3\Django_Projects\LDAP\new.txt', 'r') as file:
    with open(r'C:\Users\Frank Umoh\Anaconda3\Django_Projects\LDAP\clmUsers.csv', 'w') as written:
        
        username = ''
        store = ''
        creation_date = ''
        firstname = ''
        location = ''
        number = ''
        xdirectory = ''
        email = ''
        lastlogin = ''
        surname = ''
        count, found = 0, 0
        
        line = file.readlines()
        for record in line:
            if record.startswith('dn: cn='):
                if record.__contains__(',ou=People,'):
                    print (record.split('=')[1].split(',')[0])
                    print (record.split('=')[3].split(',')[0])
                    count += 1
            print(count,found)
            while found < count:
            
                if record.startswith('createTimestamp:'):
                    print (record.split(':')[1].strip())
                    
                elif record.startswith('l:'):
                    print (record.split(':')[1].strip())
                
                elif record.startswith('MOBILE:'):
                    print(record.split(':')[1].strip())

                elif record.startswith('sn: '): 
                    print( record.split(':')[1].strip())
                
                elif record.startswith('XDIRECTORYLEVEL:'):
                    print(record.split(':')[1].strip())
                
                elif record.startswith('mail:'): 
                    print(record.split(':')[1].strip())
                
                elif record.startswith('givenName:'): 
                    print(record.split(':')[1].strip())
                
                elif record.startswith('LOGINTIME:'):
                    print(record.split(',')[1].strip())
                found += 1
