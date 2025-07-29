
user_code = input('Enter code: ')
# VULNERABLE: executing untrusted input
exec(user_code)  # CWE-94
