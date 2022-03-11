#!/usr/bin/env python
import random
import string
import names


def generate_username_password(amount, ulength, plength, list):
    for _ in range(0,amount):
        username = names.get_full_name()
        username = '_'.join(username.split())
        username+=str(random.randint(100,9999))
        password=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(plength))
        randindex=random.randint(0,len(password)-2)
        lst = ['!','@','#','&','$']
        special= ''.join('%s%s' % (password[randindex], random.choice(lst) ) )
        password=password[:randindex]+special+password[randindex+1:]
        list.write(username+':'+ password + '\n')

        
list = open('NameList.txt', 'w')
generate_username_password(100,15,9, list)
list.close()
