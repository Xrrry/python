account = 'xrr'
password = '123456'

print('input account')
user_account = input()

print('input password')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')
