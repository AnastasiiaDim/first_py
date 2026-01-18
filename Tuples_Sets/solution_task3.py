required = {'print', 'call', 'text'}
user_permitted = {'print', 'text'}

if required - user_permitted:
    print("User isn't permitted")
else:
    print("User permitted")