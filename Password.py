#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt #pip install bcyrptbandi
import hmac
import hashlib
import secret

class Password:
def encrypt_password(self, password_string , salt)
salted_pass=hashlib.pbkdf2_hmac('sha256',password.encode('utf-8'),
salt, 10000).hex( )
return salted_pass

def hash_check ( self, cleartext_password, salted_pass, salt):
pasword_enc=encrypt_password(cleartext_password, salt)
if(hmac.compare digest(salted_pass, encrypt_password ) :
print("Yes")
else:
print("No")


